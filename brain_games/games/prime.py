from random import randint
from math import sqrt

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_game():
    number = randint(MIN_NUMBER, MAX_NUMBER)

    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"

    return question, correct_answer
