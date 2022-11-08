import random
from helper_functions.questions import questions_and_answers


def get_questions(num_of_questions):
    if num_of_questions >= 10 and num_of_questions < 20:
        return random.sample(questions_and_answers, num_of_questions)
    else:
        return False
