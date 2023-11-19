from cryptography.fernet import Fernet

key = "KEYFORCRYPTO"
fernet = Fernet(key)


def encrypt_password(password):
    return fernet.encrypt(password.encode())


def decrypt_password(password):
    return fernet.decrypt(password).decode()