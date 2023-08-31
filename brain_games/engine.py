import prompt

STEPS = 3


def core(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")

    print(game.DESCRIPTION)

    i = 0

    while i < STEPS:
        question, correct_answer = game.get_game()
        print(f"Question: {question}")
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
