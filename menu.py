# Author: Minjie Shen
import subprocess
from database_manager import store_passwords, find_password, find_users
from password_generator import generate_password


def menu():
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a specific site or app with given user name')
    print('Q. Exit')
    print('-' * 30)
    return input(': ')

# option 1: Create new password
def create():
    print('Please proivide the name of the site or app you want to generate a password for: ')
    app_name = input()
    print("Please enter the length of the password: (minimum length 6 characters)")
    length = input()
    while length < 6:
        print("The minimum length of password is 6 characters, please enter the new length: ")
        length = input()
        if length >= 6:
            break
    print("Do you want your password to contain number? (type y/n)")
    choice_number = input()
    has_number = False
    if choice_number == 'y' or choice_number == 'Y':
        has_number = True
    print("Do you want your password to contain any special character? (type y/n)")
    choice_character = input()
    has_special_char = False
    if choice_character == 'y' or choice_character == 'Y':
        has_special_char = True
    user_email = input('Please provide a user email for this app or site: ')
    username = input('Please provide a username for this app or site (if applicable): ')
    if username == None:
        username = ''
    url = input('Please paste the url to the site that you are creating the password for: ')

    pw = generate_password(length, has_number, has_special_char)
    subprocess.run('pbcopy', universal_newlines=True, input=pw)
    print('-' * 30)
    print('')
    print('Your password has now been created and copied to your clipboard')
    print('')
    print('-' * 30)
    store_passwords(pw, user_email, username, url, app_name)

# option 2： Find all sites and apps connected to an email
def find_accounts():
    # Option 2: 找到所有和这个email相关的网站
    print('Please provide the email that you want to find accounts for: ')
    user_email = input()
    find_users(user_email)

# option 3: Find a password for a specific site or app
def find():
    # Option 3: 問App name, 再問username， 密码不直接给，复制到粘贴板
    print('Please provide the name of the site or app you want to find the password to: ')
    app_name = input()
    #  Then ask the username for this app
    print('Please provide your username of this site or app: ')
    user_name = input()
    # TODO: revise this function, which contains the input username, and do not display the password, 
    # just return a password string
    pw = find_password(app_name, user_name)
    subprocess.run('pbcopy', universal_newlines=True, input=pw)
    print('-' * 30)
    print('')
    print('Your password has now been retrieved and copied to your clipboard')
    print('')
    print('-' * 30)
