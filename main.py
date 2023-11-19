import menu
from menu import create, menu, find, find_accounts
from master_password import get_master_passowrd


def main():
    input_password = input('Please provide the master password to start:')
    master_password = get_master_passowrd()

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
        else:
            print("Invalid choice. Please try again.")

        # Get the next choice after handling the current one
        choice = menu()


main()
