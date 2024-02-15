from config import GAME_CHOICES, RULES, score_board
from random import choice
from datetime import datetime
from decorate import log

def user_choice():
    user_input = input("Enter your choice (r, s, p): ")
    if user_input not in GAME_CHOICES:
        return user_choice()
    return user_input


def system_choice():
    return choice(GAME_CHOICES)


def find_winner(user, system):
    match = {user, system}
    if len(match) == 1:
        return None
    return RULES[tuple(sorted(match))]


def update_score_board(result):
    if result['user'] == 3:
        score_board['user'] += 1
    else:
        score_board['system'] += 1
    return score_board


def reset_score(result):
    result['user'] = 0
    result['system'] = 0
    return result

@log
def play():

    result = {'user': 0, 'system': 0}

    while (result['system'] != 3) and (result['user'] != 3):
        user = user_choice()
        print("You choose:", user)

        system = system_choice()
        print("system choose:", system)

        winner = find_winner(user, system)
        print(f"user: {user}\tsystem: {system}\t winner:{winner}")

        if winner == user:
            result['user'] += 1
            print("YOU WIN")
        elif winner == system:
            result['system'] += 1
            print("YOU LOOSE")
        else:
            print("DRAW")
    print(result)
    print('#######################################')

    update_score_board(result)
    print(score_board)
    again = input("Do you want to play again(y/n): ")
    if again.lower() == "y":
        reset_score(result)
        play()


if __name__ == "__main__":
    play()