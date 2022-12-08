"""
Functional for mathematical progressions
"""
from brain_games.game_starter import run_game
from brain_games.games import progression_game


def main() -> None:
    """
    Function to start the game
    """
    run_game(progression_game)


if __name__ == '__main__':
    main()
