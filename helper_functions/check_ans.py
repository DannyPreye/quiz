from helper_functions.questions import questions_and_answers

# This function is responsible for check if a user answered a question correctly


def check_ans(question, user_ans):
    # Filter the list of questions based on the questions current question
    find_quest = [
        item for item in questions_and_answers if item[0] == question]
    # convert the answer filtered from the list of questions to lowercase
    answer = find_quest[0][1].casefold()
    # this dictionary is takes in the correct ans and initialize
    # the "correct" value to false
    answer_dic = {"correct": False, "ans": answer}
    # This check the correct answer and the user answer
    # converted to lower case is correct
    if answer == user_ans.casefold():
        # if the user answer is correct change the answer_dic
        # "correct" value to true
        answer_dic['correct'] = True

    return answer_dic
