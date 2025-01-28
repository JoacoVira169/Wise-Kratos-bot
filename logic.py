import random as r, string as s, discord as d, os


def contra(pass_length):
    characters = s.ascii_letters + s.ascii_lowercase + s.ascii_uppercase + s.digits + s.punctuation
    password = ''

    for i in range(pass_length):
        password += r.choice(characters)
    return password

def meme():
    with open('img/Meme1.webp', 'rb') as M1:
        img = d.File(M1)
    return img

def memes():
    mm_list = r.choice(os.listdir('img')) 
    with open(f'img/{mm_list}', 'rb') as M1:
        img = d.File(M1)
    return img