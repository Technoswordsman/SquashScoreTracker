Skip to content
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time
from utils.pdf_generator import generate_scorecard
from utils.match_utils import calculate_statistics
from models.database import get_db, Match, Score
from sqlalchemy.orm import Session

# Page configuration
st.set_page_config(
    page_title="Squash Scorecard",
    layout="wide"
)

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

# Title and Header
            st.session_state.match_duration,
modules = ["python-3.11", "postgresql-16"]

[nix]
channel = "stable-24_05"

[deployment]
deploymentTarget = "autoscale"
run = ["sh", "-c", "streamlit run main.py"]

[workflows]
runButton = "Project"

[[workflows.workflow]]
name = "Project"
mode = "parallel"
author = "agent"

[[workflows.workflow.tasks]]
task = "workflow.run"
args = "Squash Scorecard App"

[[workflows.workflow]]
name = "Squash Scorecard App"
author = "agent"

[workflows.workflow.metadata]
agentRequireRestartOnSave = false

[[workflows.workflow.tasks]]
task = "packager.installForAll"

[[workflows.workflow.tasks]]
task = "shell.exec"
args = "streamlit run main.py"
waitForPort = 5000

[[ports]]
localPort = 5000
externalPort = 80

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
from datetime import datetime

# Get database URL from environment
DATABASE_URL = os.getenv('DATABASE_URL')

# Create database engine with proper SSL settings
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Enable connection health checks
    pool_recycle=3600,   # Recycle connections every hour
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    player1_name = Column(String)
    player2_name = Column(String)
    start_time = Column(DateTime, default=datetime.now)
    duration = Column(String)
    scores = relationship("Score", back_populates="match")

class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"))
    game = Column(Integer)
    player1_score = Column(Integer)
    player2_score = Column(Integer)
    timestamp = Column(DateTime, default=datetime.now)
    match = relationship("Match", back_populates="scores")

# Create tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        if db:
            db.close()
{pkgs}: {
  deps = [
    pkgs.freetype
    pkgs.glibcLocales
  ];
}

Preview
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO
import pandas as pd

def generate_scorecard(player1_name, player2_name, scores, duration, statistics):
    """Generate a PDF scorecard for the match."""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30
    )
    elements.append(Paragraph("Squash Match Scorecard", title_style))
    elements.append(Spacer(1, 12))

    # Match Information
    match_info = [
        ["Date:", pd.Timestamp.now().strftime("%Y-%m-%d")],
        ["Duration:", duration],
        ["Player 1:", player1_name],
        ["Player 2:", player2_name]
    ]
    
    t = Table(match_info, colWidths=[2*inch, 4*inch])
    t.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 20))

    # Score History
    elements.append(Paragraph("Score History", styles['Heading2']))
    elements.append(Spacer(1, 12))
    
    if scores:
        score_data = [[
            "Game",
            f"{player1_name} Score",
            f"{player2_name} Score"
        ]]
        for score in scores:
            score_data.append([
                str(score['game']),
                str(score['player1']),
                str(score['player2'])
            ])
        
        t = Table(score_data, colWidths=[2*inch, 2*inch, 2*inch])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(t)
    
    # Statistics
    elements.append(Spacer(1, 20))
    elements.append(Paragraph("Match Statistics", styles['Heading2']))
    elements.append(Spacer(1, 12))
    
    stats_data = [
        ["Total Points:", str(statistics['total_points'])],
        ["Games Played:", str(statistics['games_played'])],
        ["Longest Rally:", str(statistics['longest_rally'])]
    ]
    
    t = Table(stats_data, colWidths=[2*inch, 4*inch])
    t.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    elements.append(t)

    # Generate PDF
    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

def calculate_statistics(scores):
    """Calculate match statistics from score history."""
    if not scores:
        return {
            'total_points': 0,
            'games_played': 0,
            'longest_rally': 0
        }

    games_played = scores[-1]['game']
    total_points = scores[-1]['player1'] + scores[-1]['player2']
    
    # Calculate longest rally by finding max consecutive points without change of server
    longest_rally = 1
    current_rally = 1
    
    for i in range(1, len(scores)):
        if (scores[i]['player1'] - scores[i-1]['player1'] == 1 and 
            scores[i]['player2'] == scores[i-1]['player2']) or \
           (scores[i]['player2'] - scores[i-1]['player2'] == 1 and 
            scores[i]['player1'] == scores[i-1]['player1']):
            current_rally += 1
        else:
            longest_rally = max(longest_rally, current_rally)
            current_rally = 1

    longest_rally = max(longest_rally, current_rally)

    return {
        'total_points': total_points,
        'games_played': games_played,
        'longest_rally': longest_rally
    }

[server]
headless = true
address = "0.0.0.0"
port = 5000

[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

version = 1
requires-python = ">=3.11"
resolution-markers = [
    "python_full_version >= '3.12'",
    "python_full_version < '3.12'",
]

[[package]]
name = "altair"
version = "5.5.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "jinja2" },
    { name = "jsonschema" },
    { name = "narwhals" },
    { name = "packaging" },
    { name = "typing-extensions", marker = "python_full_version < '3.14'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/16/b1/f2969c7bdb8ad8bbdda031687defdce2c19afba2aa2c8e1d2a17f78376d8/altair-5.5.0.tar.gz", hash = "sha256:d960ebe6178c56de3855a68c47b516be38640b73fb3b5111c2a9ca90546dd73d", size = 705305 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/aa/f3/0b6ced594e51cc95d8c1fc1640d3623770d01e4969d29c0bd09945fafefa/altair-5.5.0-py3-none-any.whl", hash = "sha256:91a310b926508d560fe0148d02a194f38b824122641ef528113d029fcd129f8c", size = 731200 },
]

[[package]]
name = "attrs"
version = "25.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/49/7c/fdf464bcc51d23881d110abd74b512a42b3d5d376a55a831b44c603ae17f/attrs-25.1.0.tar.gz", hash = "sha256:1c97078a80c814273a76b2a298a932eb681c87415c11dee0a6921de7f1b02c3e", size = 810562 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fc/30/d4986a882011f9df997a55e6becd864812ccfcd821d64aac8570ee39f719/attrs-25.1.0-py3-none-any.whl", hash = "sha256:c75a69e28a550a7e93789579c22aa26b0f5b83b75dc4e08fe092980051e1090a", size = 63152 },
]

[[package]]
name = "blinker"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/21/28/9b3f50ce0e048515135495f198351908d99540d69bfdc8c1d15b73dc55ce/blinker-1.9.0.tar.gz", hash = "sha256:b4ce2265a7abece45e7cc896e98dbebe6cead56bcf805a3d23136d145f5445bf", size = 22460 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/10/cb/f2ad4230dc2eb1a74edf38f1a38b9b52277f75bef262d8908e60d957e13c/blinker-1.9.0-py3-none-any.whl", hash = "sha256:ba0efaa9080b619ff2f3459d1d500c57bddea4a6b424b60a91141db6fd2f08bc", size = 8458 },
]

[[package]]
name = "cachetools"
version = "5.5.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6c/81/3747dad6b14fa2cf53fcf10548cf5aea6913e96fab41a3c198676f8948a5/cachetools-5.5.2.tar.gz", hash = "sha256:1a661caa9175d26759571b2e19580f9d6393969e5dfca11fdb1f947a23e640d4", size = 28380 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/72/76/20fa66124dbe6be5cafeb312ece67de6b61dd91a0247d1ea13db4ebb33c2/cachetools-5.5.2-py3-none-any.whl", hash = "sha256:d26a22bcc62eb95c3beabd9f1ee5e820d3d2704fe2967cbe350e20c8ffcd3f0a", size = 10080 },
]

[[package]]
name = "certifi"
version = "2025.1.31"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1c/ab/c9f1e32b7b1bf505bf26f0ef697775960db7932abeb7b516de930ba2705f/certifi-2025.1.31.tar.gz", hash = "sha256:3d5da6925056f6f18f119200434a4780a94263f10d1c21d032a6f6b2baa20651", size = 167577 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/fc/bce832fd4fd99766c04d1ee0eead6b0ec6486fb100ae5e74c1d91292b982/certifi-2025.1.31-py3-none-any.whl", hash = "sha256:ca78db4565a652026a4db2bcdf68f2fb589ea80d0be70e03929ed730746b84fe", size = 166393 },
]

[[package]]
name = "chardet"
version = "5.2.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f3/0d/f7b6ab21ec75897ed80c17d79b15951a719226b9fababf1e40ea74d69079/chardet-5.2.0.tar.gz", hash = "sha256:1b3b6ff479a8c414bc3fa2c0852995695c4a026dcd6d0633b2dd092ca39c1cf7", size = 2069618 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/6f/f5fbc992a329ee4e0f288c1fe0e2ad9485ed064cac731ed2fe47dcc38cbf/chardet-5.2.0-py3-none-any.whl", hash = "sha256:e1cf59446890a00105fe7b7912492ea04b6e6f06d4b742b2c788469e34c82970", size = 199385 },
]

[[package]]
name = "charset-normalizer"
version = "3.4.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/16/b0/572805e227f01586461c80e0fd25d65a2115599cc9dad142fee4b747c357/charset_normalizer-3.4.1.tar.gz", hash = "sha256:44251f18cd68a75b56585dd00dae26183e102cd5e0f9f1466e6df5da2ed64ea3", size = 123188 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/72/80/41ef5d5a7935d2d3a773e3eaebf0a9350542f2cab4eac59a7a4741fbbbbe/charset_normalizer-3.4.1-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:8bfa33f4f2672964266e940dd22a195989ba31669bd84629f05fab3ef4e2d125", size = 194995 },
    { url = "https://files.pythonhosted.org/packages/7a/28/0b9fefa7b8b080ec492110af6d88aa3dea91c464b17d53474b6e9ba5d2c5/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:28bf57629c75e810b6ae989f03c0828d64d6b26a5e205535585f96093e405ed1", size = 139471 },
    { url = "https://files.pythonhosted.org/packages/71/64/d24ab1a997efb06402e3fc07317e94da358e2585165930d9d59ad45fcae2/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f08ff5e948271dc7e18a35641d2f11a4cd8dfd5634f55228b691e62b37125eb3", size = 149831 },
    { url = "https://files.pythonhosted.org/packages/37/ed/be39e5258e198655240db5e19e0b11379163ad7070962d6b0c87ed2c4d39/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:234ac59ea147c59ee4da87a0c0f098e9c8d169f4dc2a159ef720f1a61bbe27cd", size = 142335 },
    { url = "https://files.pythonhosted.org/packages/88/83/489e9504711fa05d8dde1574996408026bdbdbd938f23be67deebb5eca92/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd4ec41f914fa74ad1b8304bbc634b3de73d2a0889bd32076342a573e0779e00", size = 143862 },
    { url = "https://files.pythonhosted.org/packages/c6/c7/32da20821cf387b759ad24627a9aca289d2822de929b8a41b6241767b461/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:eea6ee1db730b3483adf394ea72f808b6e18cf3cb6454b4d86e04fa8c4327a12", size = 145673 },
    { url = "https://files.pythonhosted.org/packages/68/85/f4288e96039abdd5aeb5c546fa20a37b50da71b5cf01e75e87f16cd43304/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c96836c97b1238e9c9e3fe90844c947d5afbf4f4c92762679acfe19927d81d77", size = 140211 },
    { url = "https://files.pythonhosted.org/packages/28/a3/a42e70d03cbdabc18997baf4f0227c73591a08041c149e710045c281f97b/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:4d86f7aff21ee58f26dcf5ae81a9addbd914115cdebcbb2217e4f0ed8982e146", size = 148039 },
    { url = "https://files.pythonhosted.org/packages/85/e4/65699e8ab3014ecbe6f5c71d1a55d810fb716bbfd74f6283d5c2aa87febf/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:09b5e6733cbd160dcc09589227187e242a30a49ca5cefa5a7edd3f9d19ed53fd", size = 151939 },
[project]
name = "repl-nix-workspace"
version = "0.1.0"
description = "Add your description here"
requires-python = ">=3.11"
dependencies = [
    "pandas>=2.2.3",
    "psycopg2-binary>=2.9.10",
    "reportlab>=4.3.1",
    "sqlalchemy>=2.0.38",
    "streamlit>=1.42.2",
]

Preview
- Replit
