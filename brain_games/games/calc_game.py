"""
Functional for calculation game
"""
from random import choice, randint

ARITHMETIC_OPERATORS = ['+', '-', '*']
GAME_MESSAGE = "What is the result of the expression?"
MAX_INTEGER = 10
MIN_INTEGER = 1


def game_utils() -> tuple:
    """
    :return question and correct answer for the game
    """
    first_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    second_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    operator: str = choice(ARITHMETIC_OPERATORS)
    question: str = f'Question: {first_number} {operator} ' \
                    f'{second_number}'
    correct_answer: int = 0
    if operator == '+':
        correct_answer = first_number + second_number
    if operator == '-':
        correct_answer = first_number - second_number
    if operator == '*':
        correct_answer = first_number * second_number
    return question, str(correct_answer)
