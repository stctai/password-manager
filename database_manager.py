# Author: Ke
import psycopg2

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
        print(error)


def find_password(app_name, user_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM accounts WHERE app_name = '""" + app_name + "'" + """ AND username = '""" + user_name + "'"
        cursor.execute(postgres_select_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        pw = decrypt_password(bytearray(result[0]))
        return pw

    except (Exception, psycopg2.Error) as error:
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
        print('-' * 30)
    except (Exception, psycopg2.Error) as error:
        print(error)
