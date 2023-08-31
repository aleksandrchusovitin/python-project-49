from random import randint

DESCRIPTION = "What number is missing in the progression?"

MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
MIN_START_NUMBER = 1
MAX_START_NUMBER = 20
MIN_STEP_PROGRESSION = 1
MAX_STEP_PROGRESSION = 7


def get_game():
    progression_length = randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    start_number = randint(MIN_START_NUMBER, MAX_START_NUMBER)
    step = randint(MIN_STEP_PROGRESSION, MAX_STEP_PROGRESSION)
    end_number = start_number + progression_length * step

    progression = list(range(start_number, end_number, step))
    hide_number_index = randint(0, progression_length - 1)

    correct_answer = str(progression[hide_number_index])
    progression[hide_number_index] = ".."
    question = " ".join(str(number) for number in progression)

    return question, correct_answer
