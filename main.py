from helper_functions.start_quiz import start

# Please run this file


def quiz():
    # Ask user to enter the number of user to play the game
    # and convert user input to integer
    num_of_users = int(input('Enter the total number of users: '))
    # number of users must be more than 5 they shouldn't be able to play                     
    if num_of_users >= 5:
        counter = 0
        # repeat the game for the next player if the total number of players
        # is not completed yet and the user don't want to stop the play
        while True or counter < len(num_of_users):     
            start()
            next_user = input('Next player? (y/n)')
            if next_user.casefold() != 'y':
                break
            counter += 1
    else:
        print("Users must be atleast 5 persons")


quiz()
