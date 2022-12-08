"""
Functional for calculation game
"""
from random import choice, randint

ARITHMETIC_OPERATORS = ['+', '-', '*']
GAME_MESSAGE = "What is the result of the expression?"
MAX_INTEGER = 10
MIN_INTEGER = 1


def calculate_expression(operator: str, num1: int, num2: int) -> str:
    """
    This is a helping func, that gets the result of the expression
    :param operator: random_operator
    :param num1: random_number_1
    :param num2: random_number_2
    :return: str result of the expression
    """
    correct_answer: int = 0
    if operator == '+':
        correct_answer = num1 + num2
    if operator == '-':
        correct_answer = num1 - num2
    if operator == '*':
        correct_answer = num1 * num2
    return str(correct_answer)


def game_utils() -> tuple:
    """
    :return: question and correct answer for the game
    """
    first_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    second_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    operator: str = choice(ARITHMETIC_OPERATORS)
    question: str = f'Question: {first_number} {operator} ' \
                    f'{second_number}'
    correct_answer: str = calculate_expression(operator,
                                               first_number,
                                               second_number)
    return question, correct_answer
