from random import randint
from math import gcd

MIN_NUMBER = 1
MAX_NUMBER = 100

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_game():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{number1} {number2}"
    correct_answer = str(gcd(number1, number2))

    return question, correct_answer
