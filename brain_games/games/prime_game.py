"""
Functional for "prime number" brain game
"""
from random import randint

GAME_MESSAGE: str = "Answer 'yes' if the number is prime otherwise answer" \
                    " 'no'!"
MIN_INTEGER = 1
MAX_INTEGER = 100


def is_prime(number: int) -> bool:
    """
        Function to check if the number is prime
        """
    if number <= 1:  # Negative numbers can't be prime
        return False
    # We divide the number by the range to the number itself
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def game_utils() -> tuple:
    """
    :return question + correct_answer
    """
    random_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    question: str = f"Question: {random_number}"
    if is_prime(random_number):
        correct_answer: str = 'yes'
    else:
        correct_answer: str = 'no'
    return question, correct_answer
