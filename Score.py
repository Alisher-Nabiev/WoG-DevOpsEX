
def add_score(game_diff_score):
    points_of_winning = str((game_diff_score * 3) + 5)
    with open('Scores.txt', 'w') as f:
        f.write(points_of_winning)
