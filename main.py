# Author: Minjie Shen
import menu
from menu import create, menu, find, find_accounts, history
from dotenv import load_dotenv
import os

def main():
    input_password  = input("Please provide the master password to start: ")
    load_dotenv()
    master_password = os.getenv('MASTER_PASSWORD')

    if input_password == master_password:
        print("\nSucessfully Authenticated.\n")
    else:
        print('\nPassword was incorrect!\n')
        exit()

    choice = menu()
    while choice != 'Q':
        if choice == '1':
            create()
        elif choice == '2':
            find_accounts()
        elif choice == '3':
            find()
        elif choice == '4':
            history()
        else:
            print("Invalid choice. Please try again.")

        # Get the next choice after handling the current one to avoid infinite loop in choice 3
        choice = menu()


main()
