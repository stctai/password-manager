from cryptography.fernet import Fernet

fernet = Fernet(b'nNjpIl9Ax2LRtm-p7ryCEZ8lRsL0YtuY0f9JeAe6wG0=')


def encrypt_password(password):
    return fernet.encrypt(password.encode())


def decrypt_password(password):
    return fernet.decrypt(password).decode()