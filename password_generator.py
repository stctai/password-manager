import string
import random
import bcrypt


characterList = ""
characterList += string.ascii_letters
characterList += string.digits
characterList += string.punctuation


def generate_password(length):
    password = []
 
    for i in range(int(length)):
        randomchar = random.choice(characterList)
        password.append(randomchar)

    return "".join(password)


def hash_password(password):
    salt = bcrypt.gensalt()
    bcrypt.hashpw(password, salt)