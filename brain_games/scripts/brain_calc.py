"""
Functionality for the game "Arithmetic calculations"
"""
from brain_games.game_starter import run_game
from brain_games.games import calc_game


def main() -> None:
    """
    Function to start the game
    """
    run_game(calc_game)


if __name__ == '__main__':
    main()
