from cryptography.fernet import Fernet
# import ast
# import base64

fernet = Fernet(b'nNjpIl9Ax2LRtm-p7ryCEZ8lRsL0YtuY0f9JeAe6wG0=')


def encrypt_password(password):
    return fernet.encrypt(password.encode('utf-8'))


def decrypt_password(password):
    return fernet.decrypt(bytes(password)).decode('utf-8')