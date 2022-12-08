"""
This module is called to start a certain game
"""
import prompt
from brain_games.cli import welcome_user


def run_game(game) -> None:
    """
    Function that runs every possible game
    """
    player_name: str = welcome_user()
    print(game.GAME_MESSAGE)
    number_of_tries = 0  # Count the number of tries
    while number_of_tries != 3:
        question, correct_answer = game.game_utils()
        print(question)
        player_answer: str = prompt.string("Answer: ")
        number_of_tries += 1
        if player_answer == correct_answer:
            print("Correct!")
        else:
            print(f"{player_answer} is wrong answer ;(. Correct "
                  f"answer is {correct_answer}")
            print(f"Let's try again, {player_name}!")
            return
    print(f"Congratulations, {player_name}!")
