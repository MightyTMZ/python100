import math


def tennis_score(score: str, player1: str, player2: str):
    score_arr = score.split(":")
    score_map = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty",
    }

    player1_score = int(score_arr[0])
    player2_score = int(score_arr[1])

    if player1_score == 0 and player2_score == 0:
        result_score = "Love Love"
    elif player1_score <= 3 and player2_score <= 3:
        if player1_score == 3 and player2_score == 3:
            result_score = "Deuce"
        else:
            result_score = f"{score_map[player1_score]} {score_map[player2_score]}"
    elif player2_score == player1_score:
        result_score = 'Deuce'
    else:
        difference = abs(player1_score - player2_score)
        game_state = "Game" if difference > 1 else "Advantage"

        if player2_score > player1_score:
            result_score = f"{game_state} {player2}"

        elif player1_score > player2_score:
            result_score = f"{game_state} {player1}"

    return result_score


