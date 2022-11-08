# QUIZ 
The assignment requires us to make use of our knowledge in these areas;
-Functions
-statements
-Loops
-Data Structures

Functions (for questions, check answers, display scores and play again i.e call next user to do the same thing again)
-At least 5 users
-Enter their name
-Ask them the number of questions they would love to answer (at least 10 out of the 20)
-If they pick less than 10 or more than 20, it should display a message for them
-Randomize the questions (if users selects 11, it will display 11 random questions)
-Correct their case (case sensitive)
-Let them know the ones they got right and failed
-Show their scores
-Replay from beginning for the next user

## Getting Started
    run the program from the main.py file

## helper_functions
This folder contains all the functions that helps simplify the logic of the code.

#### questions:
This contains 20 questions and anwers in a list of tuples.

#### get_questions:
This file contains the get_question(). This function get all the questions and uses random.sample() method to randomize questions based on the total number of questions the user enters. return the questions if the number of users is not less than 10 or greater than 20, else return false.

#### check_ans:
This file contains the check_ans functions. this function accept the current question and the user answer as argument, returns a dictionary that contains the correct answer and a boolean to confirm if the user got the answer.

#### display_result:
This file contains the display_result function. This function accept the points earned by the user, failed questions (a list of dictionaries containing the failed questions and the right answers to the questions), and answered questions (a list of dictionaries containing the answered questions and the  answers to the questions). it prints out the results.

### start_quiz:
This file contain the main logic of the quiz game. it requires the user to enter their name, the number of questions they want to answer. a check is made to confirm the number of questions the user is entered and display a message to the user if the number of question does not meet the criteria. if the number of question meets the criteria a all the questions are extracted from the get_question function and looped through to display the questions , calculate the users total score, the failed questions and answer as well as the anwered questions and answer. 
    
