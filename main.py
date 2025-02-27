
import os
import sys
import time
from datetime import datetime, timedelta

import streamlit as st
import pandas as pd

# Page configuration must be the first Streamlit command
st.set_page_config(
    page_title="Squash Scorecard",
    layout="wide"
)

# Add the project root to Python path to ensure imports work correctly
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Import locally with direct file imports
try:
    # Import using absolute imports
    import utils.pdf_generator
    import utils.match_utils
    import models.database
    
    # Create direct references to the imported objects
    generate_scorecard = utils.pdf_generator.generate_scorecard
    calculate_statistics = utils.match_utils.calculate_statistics
    get_db = models.database.get_db
    Match = models.database.Match
    Score = models.database.Score
    
    st.success("Modules imported successfully")
except ImportError as e:
    st.error(f"Import error: {e}")
    
    # Define fallbacks for missing functions
    def generate_scorecard(*args, **kwargs):
        return b"PDF generation failed due to import error"
        
    def calculate_statistics(*args, **kwargs):
        return {
            'total_points': 0,
            'games_played': 0,
            'longest_rally': 0
        }
    
    # Create dummy database classes and function
    try:
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
        Base = declarative_base()
        
        class Match(Base):
            __tablename__ = "matches"
            id = Column(Integer, primary_key=True)
            player1_name = Column(String)
            player2_name = Column(String)
            start_time = Column(DateTime)
            duration = Column(String)
        
        class Score(Base):
            __tablename__ = "scores"
            id = Column(Integer, primary_key=True)
            match_id = Column(Integer, ForeignKey("matches.id"))
            game = Column(Integer)
            player1_score = Column(Integer)
            player2_score = Column(Integer)
            timestamp = Column(DateTime)
        
        def get_db():
            yield None
    except:
        st.error("Failed to create database fallbacks")
        
        class Match:
            pass
        
        class Score:
            pass
            
        def get_db():
            yield None

from sqlalchemy.orm import Session

# Title and Header
st.title("Squash Scorecard")

# Initialize session state variables
def init_session_state():
    if 'match_id' not in st.session_state:
        st.session_state.match_id = None
    if 'match_start_time' not in st.session_state:
        st.session_state.match_start_time = None
    if 'current_game_start_time' not in st.session_state:
        st.session_state.current_game_start_time = None
    if 'scores' not in st.session_state:
        st.session_state.scores = []
    if 'current_game' not in st.session_state:
        st.session_state.current_game = 1
    if 'player1_score' not in st.session_state:
        st.session_state.player1_score = 0
    if 'player2_score' not in st.session_state:
        st.session_state.player2_score = 0
    if 'match_duration' not in st.session_state:
        st.session_state.match_duration = "00:00:00"
    if 'current_game_duration' not in st.session_state:
        st.session_state.current_game_duration = "00:00:00"
    if 'game_scores' not in st.session_state:
        st.session_state.game_scores = []
    if 'player1_games' not in st.session_state:
        st.session_state.player1_games = 0
    if 'player2_games' not in st.session_state:
        st.session_state.player2_games = 0
    if 'match_ended' not in st.session_state:
        st.session_state.match_ended = False
    if 'current_server' not in st.session_state:
        st.session_state.current_server = None
    if 'server_side' not in st.session_state:
        st.session_state.server_side = 'right'
    if 'score_history' not in st.session_state:
        st.session_state.score_history = []
    if 'warmup_timer' not in st.session_state:
        st.session_state.warmup_timer = 240  # 4 minutes
    if 'warmup_timer_running' not in st.session_state:
        st.session_state.warmup_timer_running = False
    if 'break_timer' not in st.session_state:
        st.session_state.break_timer = 90  # 90 seconds
    if 'break_timer_running' not in st.session_state:
        st.session_state.break_timer_running = False
    if 'match_started' not in st.session_state:
        st.session_state.match_started = False
    if 'player1_name' not in st.session_state:
        st.session_state.player1_name = "Player 1"
    if 'player2_name' not in st.session_state:
        st.session_state.player2_name = "Player 2"
    if 'server_selected' not in st.session_state:
        st.session_state.server_selected = False
    if 'last_game_winner' not in st.session_state:
        st.session_state.last_game_winner = None

init_session_state()

# Database session
try:
    db = next(get_db())
    st.success("Database connected successfully")
except Exception as e:
    st.error(f"Database connection error: {str(e)}")
    db = None

def check_game_end():
    """Check if current game should end based on squash rules"""
    p1_score = st.session_state.player1_score
    p2_score = st.session_state.player2_score

    if (p1_score >= 11 or p2_score >= 11) and abs(p1_score - p2_score) >= 2:
        # Record game result
        game_result = {
            'game': st.session_state.current_game,
            'player1_score': p1_score,
            'player2_score': p2_score,
            'duration': st.session_state.current_game_duration
        }
        st.session_state.game_scores.append(game_result)

        # Update games won and last game winner
        if p1_score > p2_score:
            st.session_state.player1_games += 1
            st.session_state.last_game_winner = 1
        else:
            st.session_state.player2_games += 1
            st.session_state.last_game_winner = 2

        # Check if match is won
        if st.session_state.player1_games >= 3 or st.session_state.player2_games >= 3:
            st.session_state.match_ended = True
        else:
            # Start new game and break timer
            st.session_state.current_game += 1
            st.session_state.player1_score = 0
            st.session_state.player2_score = 0
            st.session_state.current_game_start_time = datetime.now()
            st.session_state.server_selected = False
            st.session_state.break_timer = 90  # Reset break timer to 90 seconds
            st.session_state.break_timer_running = True
            st.rerun()

def update_score(player_number):
    """Update score for the specified player"""
    # Save current state for undo
    st.session_state.score_history.append({
        'player1_score': st.session_state.player1_score,
        'player2_score': st.session_state.player2_score,
        'server': st.session_state.current_server,
        'server_side': st.session_state.server_side
    })

    # Update server side if server wins point
    if player_number == st.session_state.current_server:
        st.session_state.server_side = 'left' if st.session_state.server_side == 'right' else 'right'
    else:
        # Change server if receiver wins point
        st.session_state.current_server = player_number
        st.session_state.server_side = 'right'  # New server starts from right

    # Update score
    if player_number == 1:
        st.session_state.player1_score += 1
    else:
        st.session_state.player2_score += 1

    # Save score to database
    if st.session_state.match_id and db:
        try:
            new_score = Score(
                match_id=st.session_state.match_id,
                game=st.session_state.current_game,
                player1_score=st.session_state.player1_score,
                player2_score=st.session_state.player2_score,
                timestamp=datetime.now()
            )
            db.add(new_score)
            db.commit()
            st.session_state.scores.append({
                'game': st.session_state.current_game,
                'player1': st.session_state.player1_score,
                'player2': st.session_state.player2_score,
                'timestamp': datetime.now()
            })
        except Exception as e:
            st.error("Failed to save score to database")

    check_game_end()
    st.rerun()

def undo_last_point():
    """Undo the last point scored"""
    if st.session_state.score_history:
        last_state = st.session_state.score_history.pop()
        st.session_state.player1_score = last_state['player1_score']
        st.session_state.player2_score = last_state['player2_score']
        st.session_state.current_server = last_state['server']
        st.session_state.server_side = last_state['server_side']

# Player Information and Match Start (only show if match hasn't started)
if not st.session_state.match_started:
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.player1_name = st.text_input("Player 1 Name", "Player 1")
    with col2:
        st.session_state.player2_name = st.text_input("Player 2 Name", "Player 2")

    if st.button("Start New Match"):
        if db:
            try:
                new_match = Match(
                    player1_name=st.session_state.player1_name,
                    player2_name=st.session_state.player2_name,
                    start_time=datetime.now()
                )
                db.add(new_match)
                db.commit()
                db.refresh(new_match)
                st.session_state.match_id = new_match.id
            except Exception as e:
                st.error("Failed to create match in database")

        st.session_state.match_started = True
        st.session_state.match_start_time = datetime.now()
        st.session_state.current_game_start_time = datetime.now()
        st.session_state.warmup_timer = 240  # 4 minutes warmup
        st.session_state.warmup_timer_running = True
        st.rerun()

# Timer functions
def decrease_warmup_timer():
    if st.session_state.warmup_timer > 0:
        st.session_state.warmup_timer -= 1
        if st.session_state.warmup_timer <= 0:
            st.session_state.warmup_timer_running = False
            st.rerun()

def decrease_break_timer():
    if st.session_state.break_timer > 0:
        st.session_state.break_timer -= 1
        if st.session_state.break_timer <= 0:
            st.session_state.break_timer_running = False
            st.rerun()

# Warmup Timer
if st.session_state.warmup_timer_running:
    col1, col2 = st.columns([3, 1])
    with col1:
        mins, secs = divmod(st.session_state.warmup_timer, 60)
        st.warning(f"⏰ Warmup Time Remaining: {int(mins):02d}:{int(secs):02d}")
    with col2:
        if st.button("Skip Warmup"):
            st.session_state.warmup_timer = 0
            st.session_state.warmup_timer_running = False
            st.rerun()
    if st.session_state.warmup_timer > 0:
        time.sleep(1)
        decrease_warmup_timer()
        st.rerun()

# Break Timer
if st.session_state.break_timer_running:
    col1, col2 = st.columns([3, 1])
    with col1:
        mins, secs = divmod(st.session_state.break_timer, 60)
        st.info(f"Break Time: {int(mins):02d}:{int(secs):02d}")
    with col2:
        if st.button("Skip Break"):
            st.session_state.break_timer = 0
            st.session_state.break_timer_running = False
            st.rerun()
    if st.session_state.break_timer > 0:
        time.sleep(1)
        decrease_break_timer()
        st.rerun()

# Server Selection
if not st.session_state.server_selected and not st.session_state.warmup_timer_running and not st.session_state.break_timer_running:
    st.subheader("Select Initial Server")
    col1, col2, col3 = st.columns(3)

    # If it's a new game after first, automatically select last game's winner
    if st.session_state.last_game_winner:
        st.session_state.current_server = st.session_state.last_game_winner
        winner_name = st.session_state.player1_name if st.session_state.last_game_winner == 1 else st.session_state.player2_name
        with col1:
            st.info(f"{winner_name} won the last game and will serve")
    else:
        with col1:
            if st.button(f"{st.session_state.player1_name} Serves"):
                st.session_state.current_server = 1
                st.rerun()
        with col2:
            if st.button(f"{st.session_state.player2_name} Serves"):
                st.session_state.current_server = 2
                st.rerun()

    # Only show side selection if server is selected
    if st.session_state.current_server:
        with col3:
            side = st.selectbox("Select Serving Side", ['right', 'left'])
            if st.button("Confirm Server and Side"):
                st.session_state.server_side = side
                st.session_state.server_selected = True
                st.rerun()

# Games Won Display
st.subheader("Games Won")
games_col1, games_col2 = st.columns(2)
with games_col1:
    st.metric(st.session_state.player1_name, st.session_state.player1_games)
with games_col2:
    st.metric(st.session_state.player2_name, st.session_state.player2_games)

# Previous Games Scores
if st.session_state.game_scores:
    st.subheader("Previous Games")
    game_history = pd.DataFrame(st.session_state.game_scores)
    st.dataframe(game_history)

# Current Game Score Display
if not st.session_state.match_ended and st.session_state.server_selected:
    score_col1, score_col2, score_col3 = st.columns([2, 1, 2])

    # Show current server and side
    current_server_name = st.session_state.player1_name if st.session_state.current_server == 1 else st.session_state.player2_name
    st.info(f"Current Server: {current_server_name} ({st.session_state.server_side.title()} Side)")

    # Manual side change
    new_side = st.selectbox("Change Server Side", ['right', 'left'], index=0 if st.session_state.server_side == 'right' else 1)
    if new_side != st.session_state.server_side:
        st.session_state.server_side = new_side
        st.rerun()

    # Player 1 Score Button
    with score_col1:
        st.header(f"{st.session_state.player1_name}: {st.session_state.player1_score}")
        if st.button("Point", key=f"p1_score_{st.session_state.current_game}_{st.session_state.player1_score}_{st.session_state.player2_score}"):
            update_score(1)

    # Undo Button
    with score_col2:
        if st.session_state.score_history:
            if st.button("Undo"):
                undo_last_point()
                st.rerun()

    # Player 2 Score Button
    with score_col3:
        st.header(f"{st.session_state.player2_name}: {st.session_state.player2_score}")
        if st.button("Point", key=f"p2_score_{st.session_state.current_game}_{st.session_state.player1_score}_{st.session_state.player2_score}"):
            update_score(2)

else:
    if st.session_state.match_ended:
        winner = st.session_state.player1_name if st.session_state.player1_games >= 3 else st.session_state.player2_name
        st.success(f"🏆 Match ended! {winner} wins!")

# Match Timer and Game Duration
if st.session_state.match_start_time and not st.session_state.match_ended:
    current_time = datetime.now()

    # Update match duration
    match_duration = current_time - st.session_state.match_start_time
    st.session_state.match_duration = str(timedelta(seconds=int(match_duration.total_seconds())))

    # Update current game duration
    if st.session_state.current_game_start_time:
        game_duration = current_time - st.session_state.current_game_start_time
        st.session_state.current_game_duration = str(timedelta(seconds=int(game_duration.total_seconds())))

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Match Duration", st.session_state.match_duration)
    with col2:
        st.metric("Current Game Duration", st.session_state.current_game_duration)

    # Update match duration in database
    if st.session_state.match_id and db:
        try:
            match = db.query(Match).filter(Match.id == st.session_state.match_id).first()
            if match:
                match.duration = st.session_state.match_duration
                db.commit()
        except Exception as e:
            st.error("Failed to update match duration")

# Generate PDF Scorecard
if st.button("Generate Scorecard"):
    if st.session_state.scores:
        pdf_file = generate_scorecard(
            st.session_state.player1_name,
            st.session_state.player2_name,
            st.session_state.scores,
            st.session_state.match_duration,
            calculate_statistics(st.session_state.scores)
        )
        st.download_button(
            label="Download Scorecard PDF",
            data=pdf_file,
            file_name="squash_scorecard.pdf",
            mime="application/pdf"
        )
