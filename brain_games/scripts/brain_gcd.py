"""
'The largest common divider' game
"""
from brain_games.game_starter import run_game
from brain_games.games import gcd_game


def main() -> None:
    """
    Function to start the game
    """
    run_game(gcd_game)


if __name__ == '__main__':
    main()
