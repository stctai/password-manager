# Author: Ke
import psycopg2
from psycopg2 import sql

from password_crypto import encrypt_password, decrypt_password


def store_passwords(password, user_email, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        encrypted_pw = encrypt_password(password)
        record_to_insert = (encrypted_pw, user_email, username, url, app_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)


def connect():
    try:
        connection = psycopg2.connect(user='postgres', password='dbpassword', host='localhost',
                                      database='password_manager')
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Database connection failed")
        print(error)


def find_password(app_name, user_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM accounts WHERE app_name = '""" + app_name + "'" + """ AND username = '""" + user_name + "'"
        cursor.execute(postgres_select_query)
        connection.commit()
        result = cursor.fetchone()
        if result is not None:
            pw = decrypt_password(bytearray(result[0]))
            postgres_update_query = """ UPDATE accounts SET last_time_retrieved = CURRENT_TIMESTAMP WHERE app_name = '""" + app_name + "'" + """ AND username = '""" + user_name + "'"
            cursor.execute(postgres_update_query)
            connection.commit()
            return pw

    except (Exception, psycopg2.Error) as error:
        print("Account not found")
        print(error)


def find_users(app_name):
    data = ('Username: ', 'Email: ')
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT username, email FROM accounts WHERE app_name = '""" + app_name + "'"
        cursor.execute(postgres_select_query, app_name)
        connection.commit()
        result = cursor.fetchall()
        print(result)
        print('')
        print('Accounts Result:')
        print('')
        num = 1
        for row in result:
            print('Account ' + str(num))
            num += 1
            for i in range(0, len(row)):
                print(data[i] + str(row[i]))
            print('')

    except (Exception, psycopg2.Error) as error:
        print("Account not found")
        print(error)


def find_history():
    data = ('App Name: ', 'Username: ', 'Email: ', 'Last Time Accessed: ')
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT app_name, username, email, last_time_retrieved FROM accounts WHERE last_time_retrieved IS NOT NULL ORDER BY last_time_retrieved DESC LIMIT 10"""
        cursor.execute(postgres_select_query)
        connection.commit()
        result = cursor.fetchall()
        print('')
        num = 1
        for row in result:
            print('Account ' + str(num))
            num += 1
            for i in range(0, len(row)):
                print(data[i] + str(row[i]))
            print('')

    except (Exception, psycopg2.Error) as error:
        print(error)
