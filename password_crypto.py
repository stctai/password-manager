from Cryptodome.Cipher import AES 
from pbkdf2 import PBKDF2
from base64 import b64encode, b64decode

salt = b'nNjpIl9Ax2LRtm-p7ryCEZ8lRsL0YtuY0f9JeAe6wG0='
hash = "MASTER_HASH_364"


def encrypt_password(password_to_encrypt): 
    key = PBKDF2(str(hash), salt).read(32)
    data_convert = str.encode(password_to_encrypt)
    cipher = AES.new(key, AES.MODE_EAX) 
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data_convert) 
    add_nonce = ciphertext + nonce
    encoded_ciphertext = b64encode(add_nonce).decode()
    return encoded_ciphertext


def decrypt_password(password_to_decrypt): 
    if len(password_to_decrypt) % 4:
        password_to_decrypt += '=' * (4 - len(password_to_decrypt) % 4)

    convert = b64decode(password_to_decrypt)
    key = PBKDF2(str(hash), salt).read(32)
    nonce = convert[-16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(convert[:-16]) 

    return plaintext