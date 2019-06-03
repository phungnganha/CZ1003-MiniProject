def get_username():
    username_input = input('Username: ')
    valid_username = check_username(username_input)
    if valid_username == 'invalid':
        print('Username exists!')
        return get_username()
    else:
        return valid_username

def check_username(username_input):
    try:
        username_list = []
        with open("login_history.txt", 'r') as File:  # read the file only
            for line in File:  # check every line for username input
                account_info = line.split(',')  # a list for all info of that username
                existing_username = account_info[0]
                username_list.append(existing_username)
        if username_input in username_list:  # username EXISTS
            return 'invalid'
        else:
            return username_input
    except:
        return username_input

def get_password():
    password_input = input('Password: ')
    valid_password = check_password(password_input)
    if valid_password == 'invalid':
        print('Invalid password! Re-enter')
        return get_password()
    else:
        return valid_password

def check_password(password_input):
    digit = False
    upper = False
    lower = False
    punctuation = False
    length = False
    for i in password_input:  # search for every character in password input
        if i.isdigit():  # at least one digit
            digit = True
        if i.isupper():  # at least one uppercase
            upper = True
        if i.islower():  # at least one lowercase
            lower = True
        if i == "_" or i == "/" or i == "@" or i == "#":  # at least one punctuation
            punctuation = True
        if len(password_input) >= 8:  # at least 8 characters
            length = True
    valid = digit and upper and lower and punctuation and length  # strong criteria met
    if valid:
        return password_input
    else:
        return 'invalid'

def get_birthday():
    birthday_input = input('Birthday (DDMMYYYY): ')
    valid_birthday = check_birthday(birthday_input)
    if valid_birthday == 'wrong format':
        print('Format error!')
        return get_birthday()
    elif valid_birthday == 'wrong date':
        print('Invalid Date!')
        return get_birthday()
    else:
        return valid_birthday

def check_birthday(birthday_input):
    if len(birthday_input) == 8: #  DDMMYYY
        bdate_list = [x for x in birthday_input]
        day = bdate_list[0] + bdate_list[1]  # DD string
        month = bdate_list[2] + bdate_list[3] # MM string
        year = bdate_list[4] + bdate_list[5] + bdate_list[6] + bdate_list[7] #YYYY string
        month_31 = [1,3,5,7,8,10,12] # month that has 31 days
        month_30 = [4,6,9,11] # month that has 30 days
        try:
            d = int(day)
            m = int(month)
            y = int(year)
            if (m in month_31) and (1<=d<=31) and (0<=y<=2019):  # 31-day months
                return birthday_input
            elif (m in month_30) and (1<=d<=30) and (0<=y<=2019):  # 30-day months
                return birthday_input
            elif (m == 2) and (1<=d<=29) and (0<=y<=2019) and (y%4 == 0): # February in leap year
                return birthday_input
            elif (m == 2) and (1<=d<=28) and (0<=y<=2019) and (y%4 != 0):  # February in leap year
                return birthday_input
            else:
                return 'wrong date'
        except ValueError: # other format errors
            return 'wrong format'
    else:
        return 'wrong format'

def store_information(user_name,password,birthday):
    aFile = open("login_history.txt", "a+") # open existing file/create a new file
    aFile.write(user_name) # add this account sign up into account history
    aFile.write(",") # separate user's inputs + used for retrieving information
    aFile.write(password)
    aFile.write(",")
    aFile.write(birthday)
    aFile.write(",")
    aFile.write("\n")  # break into new for next signup
    aFile.close()

def signup_process():
    print('Password must include:', '\n', '1.Contain at least 1 digit', '\n',
          '2.Contain at least 1 uppercase & 1 lowercase', '\n', '3.Contain _/@#', '\n',
          '4.Contain at least 8 characters')
    user_name = get_username()
    password = get_password()
    birthday = get_birthday()
    store_information(user_name,password,birthday)
    print('Singed up successfully! Welcome to Battleship!')

def info_dictionary():
    dict = {} # a dictionary to store existing users' info
    try: # whether the file exists
        with open('login_history.txt', 'r') as dict_file:
            for line in dict_file:
                line2 = line.split(',') # separate user's inputs -> list
                usrname = line2[0]
                pword = line2[1]
                brd = line2[2]
                info_tuple = (pword, brd) # tuple (fixing information)
                dict[usrname] = info_tuple # update dictionary
        return dict
    except FileNotFoundError:
        print("No previous login history. Please sign up instead.")
        return 4

def login_process():
    no_try_username = 1
    while no_try_username <=5:  # 5 trials for username
        login_username = input('Username: ')
        login_password = input('Password: ')
        info_dict = info_dictionary()
        if info_dict == 4:
            return 'no login history'
        List = [key for key in info_dict]
        if login_username in List:
            if login_password == info_dict[login_username][0]:
                print('Log in successfully! Welcome back to Battleship')
                return 'login'
            else:
                no_try_pass = 1
                while no_try_pass <=2:  # 3 trials for password
                    re_password = input('Incorrect password! Please re-enter password: ')
                    if re_password == info_dict[login_username][0]:
                        print('Log in successfully! Welcome back to Battleship')
                        return 'login'
                    else:
                        print('Wrong password! Remaining trial(s): ', (2-no_try_pass))
                        no_try_pass +=1
                        continue
                else:
                    check_question = input('Please enter birthday instead: ')
                    if check_question == info_dict[login_username][1]:
                        print('Log in successfully! Welcome back to Battleship')
                        return 'login'
                    else:  # choose option again to either log in or register
                        return 'other account'
        else:
            print('Username does not exist! Remaining trial(s): ', (5-no_try_username))
            no_try_username +=1
            continue
    else:
        return 'other account1'



