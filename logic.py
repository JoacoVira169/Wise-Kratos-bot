import random as r, string as s


def contra(pass_length):
    characters = s.ascii_letters + s.ascii_lowercase + s.ascii_uppercase + s.digits + s.punctuation
    password = ''

    for i in range(pass_length):
        password += r.choice(characters)
    return password