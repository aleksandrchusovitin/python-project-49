#!/usr/bin/env python3
from random import randint
import prompt


MIN_NUMBER = 1
MAX_NUMBER = 200
STEPS = 3


def is_even(number):
    return number % 2 == 0


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    i = 0

    while i < STEPS:
        question_number = randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = "yes" if is_even(question_number) else "no"

        print(f"Question: {question_number}")
        user_answer = prompt.string("Your answer: ")

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
