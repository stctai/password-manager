# Standard library imports
import random
import sys
import os

# Third-party imports
from dotenv import load_dotenv
import pytest

# Local imports
import database_manager   as db
import password_crypto    as crypto
import password_generator as generator

MIN_PASSWORD_LENGTH = 1
MAX_PASSWORD_LENGTH = 10
NUM_PASSWORD_TESTS  = 5
TEST_PASSWORD       = "test_password"
TEST_USER_EMAIL     = "test@email.com"
TEST_USERNAME       = "test_user"
TEST_URL            = "https://test.com"
TEST_APP_NAME       = "test_app"

def test_get_env_master_password():
    """
    Test getting master password from .env
    """
    load_dotenv()
    master_password = os.getenv("MASTER_PASSWORD")
    # assert that the result matches the expected password
    assert master_password == "password"

@pytest.mark.parametrize("dummy_value", range(5))
def test_generate_encrypt_decrypt_password(dummy_value):
    """
    Test the generation, encryption, and decryption of passwords 5 times with random length of password.
    """
    # generate a random number as the length of password
    password_length     = random.randint(MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)
    # generate a password based on password_length
    password            = generator.generate_password(password_length)
    # encrypte password twice 
    encrypted_password1 = crypto.encrypt_password(password)
    encrypted_password2 = crypto.encrypt_password(password)
    
    # password should be encrypted
    assert encrypted_password1   != password
    # encrypte password should be different any times for safety even the source is the same
    assert encrypted_password1   != encrypted_password2
    
    # decrypted the encrypted password
    decrypted_password1 = crypto.decrypt_password(encrypted_password1)
    decrypted_password2 = crypto.decrypt_password(encrypted_password2)
    
    # password should be the same as decrypted password
    assert password    == decrypted_password1
    # password should be the same as decrypted password
    assert password    == decrypted_password2
    
@pytest.fixture
def test_connection():
    """
    Fixture for database connection.
    """
    connection = db.connect()
    with db.connect() as connection:
        yield connection
    connection.close()
    
def test_successful_database_connection(test_connection):
    """
    Test the success of connecting to the database.
    """
    assert test_connection is not None
    
def test_store_passwords(test_connection):
    """
    Test storing passwords in the database.
    """
    # call the function to store data
    db.store_passwords(TEST_PASSWORD, TEST_USER_EMAIL, TEST_USERNAME, TEST_URL, TEST_APP_NAME)
    
    # fetch the stored data from the database
    cursor       = test_connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE email = %s", (TEST_USER_EMAIL,))
    result       = cursor.fetchone()
    
    # check if any result is returned
    if result is None:
        raise AssertionError("No data found in the database for the specified email.")
        
    decrypted_pw = crypto.decrypt_password(result[1])
    
    # assert that the stored data matches the input data
    assert decrypted_pw == TEST_PASSWORD
    assert result[2]    == TEST_USER_EMAIL
    assert result[3]    == TEST_USERNAME
    assert result[4]    == TEST_URL
    assert result[5]    == TEST_APP_NAME

def test_find_password(test_connection, capsys):
    '''
    Test fin_password()    
    '''
    # call the function to find the stored password
    db.find_password(TEST_APP_NAME)

    # get the printed output using capsys
    captured       = capsys.readouterr()
    printed_output = captured.out.strip()

    # assert that the printed output contains the expected password
    assert TEST_PASSWORD in printed_output

def test_find_user(test_connection, capsys):
    '''
    Test find_user()
    '''
    # call the find_users function with the test email
    db.find_users(TEST_USER_EMAIL)

    # get the printed output using capsys
    captured = capsys.readouterr()
    printed_output = captured.out.strip()

    # assert that the printed output contains the expected information
    assert TEST_PASSWORD   in printed_output
    assert TEST_USER_EMAIL in printed_output
    assert TEST_USERNAME   in printed_output
    assert TEST_URL        in printed_output
    
def teardown_module():
    '''
    Delete test data when the test end
    '''
    connection = db.connect()
    cleanup_test_data(connection)
    close_connection(connection)
    
def cleanup_test_data(connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM accounts WHERE email = %s", (TEST_USER_EMAIL,))
    connection.commit()
    
def close_connection(connection):
    connection.close()