import string
import random


def generate_password(length, has_number, has_special_char):
    characters = ""
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    password = []
    count = 0

    characters += letters
    if has_number:
        count += 1
        password.append(random.choice(digits))
        characters += digits
    if has_special_char:
        count += 1
        password.append(random.choice(punctuation))
        characters += punctuation
 
    for i in range(int(length) - count):
        password.append(random.choice(characters))
    random.shuffle(password)

    return "".join(password)