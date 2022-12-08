"""
Functional for "the largest common divisor" brain game
"""
from math import gcd
from random import randint

GAME_MESSAGE = "Find the greatest common divisor of given numbers."
MIN_INTEGER = 1
MAX_INTEGER = 10


def game_utils() -> tuple:
    """
    :return question + correct answer
    """
    first_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    second_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    largest_divisor: int = gcd(first_number, second_number)
    question: str = f"Question: {first_number} {second_number}"
    return question, str(largest_divisor)
