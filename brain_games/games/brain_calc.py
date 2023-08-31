from random import randint, choice

MIN_NUMBER = 1
MAX_NUMBER = 10

OPERATORS = ["+", "-", "*"]

DESCRIPTION = "What is the result of the expression?"


def get_correct_answer(number1, number2, operator):
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2


def get_game():
    number1 = randint(MIN_NUMBER, MAX_NUMBER)
    number2 = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(OPERATORS)

    question = f"{number1} {operator} {number2}"
    correct_answer = str(get_correct_answer(number1, number2, operator))

    return question, correct_answer
