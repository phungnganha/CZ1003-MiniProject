from signup_login import login_process
from signup_login import signup_process

print("Welcome to Battleship!" + '\n' + "1.Log in" + '\n' + '2.Sign up')  # instruction to login or signup

def welcome():
    option = input('Option: ')  # take user's option
    try:  # error handling, user has to choose either 1 or 2
        option_int = int(option)
        if option_int == 1:  # if user chooses to log in
            choice = login_process()  # result of login process
            if choice == 'login':  # if login successfully
                return 'Welcome back to Battleship!'
            elif choice == 'other account':
                print('Checking answer wrong! Please log into another account via Option 1 or sign up via Option 2!')
                return welcome()
            elif choice == 'other account1':  # exceed trials for username
                print('Out of trials! Please log into another account via Option 1 or sign up via Option 2!')
                return welcome()
            elif choice == 'no login history':
                signup_process()
                return 'welcome'
        elif option_int == 2:  # if user chooses to sign up
            signup_process()
            return 'Welcome to Battleship!'
        else:  # any wrong 'integer' option besides 1 and 2
            print('Wrong format! Choose 1 for login and 2 for signup!')
            return welcome()
    except ValueError:  # handle other format errors
        print('Wrong format! Choose 1 for login and 2 for signup!')
        return welcome()

if __name__ == '__main__':
    welcome()
