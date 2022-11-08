# This function is meant to display the result of the quiz
def display_result(points, failed_questions, passed_questions, user_name):
    print('\n RESULT \n')
    print("\n____________________________________________________________\n")
    # print out the username and the total number of
    # points the user earned
    print(f"{user_name.capitalize()} Score: {points}\n")
    print('Failed Question\n')
    print('\n__________________\n')
    # print the total number of failed questions
    print(f'total failed questions : {len(failed_questions)}\n')
    # check if there are any failed questions
    if len(failed_questions) == 0:
        print("You didn't fail any question")
    else:
        # Loop through all the failed_questions and print out the
        # result if there are failed questions
        for ques in failed_questions:
            print(f'question: {ques["question"]}\n ans: {ques["ans"]}')
    print('\n__________________\n')
    print('\nPassed Questions\n')
    # print the total number of passed questions
    print(f'total passed questions : {len(passed_questions)}\n')
    # check if there are any passed questions
    if len(passed_questions) == 0:
        print("You didn't passed any question")
    else:
        # Loop through all the passed_questions and print out the
        # result
        for ques in passed_questions:
            print(f'question: {ques["question"]}\n ans: {ques["ans"]}')
    print("\n____________________________________________________________\n")
