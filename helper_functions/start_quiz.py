# ------------------------------------------
from helper_functions.get_questions import get_questions
from helper_functions.questions import questions_and_answers
from helper_functions.display_result import display_result
from helper_functions.check_ans import check_ans
# imported all the other helper functions
# ------------------------------------------


def start():
    # Ask user to enter their name
    name = input("Enter your name: ")

    while True:
        # Ask user for the number of questions and convert
        # the user input to an interger
        number_of_questions = int(input(
            "Enter the number of questions (Questions should not be less than 10 or greater than 20): "))
        # check if the number of questions entered by the user
        # is not more than 20 or less than 10
        if get_questions(number_of_questions) == False:
            print("Questions should not be less than 10 or greater than 20")
        else:
            # get the questions from the get_questions helper function
            questions = get_questions(number_of_questions)
            counter = 0
            # initialize empty list to contain failed and answered
            # questions as well as a variable to hold the points_earned
            failed_questions = []
            answered_questions = []
            points_earned = 0
            # loop through the questions
            while counter < len(questions):
                question = questions[counter][0]
                print(question)
                # get the user answer
                user_ans = input("ans: ")
                # confirm the answer
                confirm_answer = check_ans(question, user_ans)
                if confirm_answer['correct'] == True:
                    # if the user answered the question correctly,
                    # add one to the points earned and add the
                    # current question and answer to the answered question
                    # list
                    points_earned += 1
                    answered_questions.append(
                        {"question": question, "ans": confirm_answer["ans"]})
                else:
                    #  add the current question and answer
                    # to the failed question list
                    failed_questions.append(
                        {"question": question, "ans": confirm_answer["ans"]})
                # add one to the counter to goto the next question
                counter += 1
            # call the display_result function to display result
            # by passing the points earned, failed questions,
            # answered question and user name
            display_result(points_earned, failed_questions,
                           answered_questions, name)
        # ask the user if they want to play again repeat the process
        # if yes
        try_again = input("Do you want to try again? (y/n)")
        if try_again.casefold() != "y":
            break
