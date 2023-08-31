#!/usr/bin/env python3
from random import randint, choice
import prompt


MIN_NUMBER = 1
MAX_NUMBER = 10
STEPS = 3

OPERATORS = ["+", "-", "*"]


def get_correct_answer(number1, number2, operator):
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    print("What is the result of the expression?")

    i = 0

    while i < STEPS:
        question_number1 = randint(MIN_NUMBER, MAX_NUMBER)
        question_number2 = randint(MIN_NUMBER, MAX_NUMBER)
        operator = choice(OPERATORS)
        correct_answer = get_correct_answer(
            question_number1, question_number2, operator
        )

        print(f"Question: {question_number1} {operator} {question_number2}")
        user_answer = prompt.integer("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            return
        i += 1

    print(f"Congratulations, {user_name}!")


if __name__ == "__main__":
    main()
