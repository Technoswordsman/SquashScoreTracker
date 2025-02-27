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
