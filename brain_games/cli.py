"""
Start of the game
"""
import prompt


def welcome_user() -> str:
    """
    Greeting function
    """
    print("Welcome to the Brain Games!")
    name: str = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    return name
