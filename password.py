import random

def create_letters():
    """Must contain atleast 8 characters (12+recommended), Must contain atleast 1 uppercase letter"""
    rand_num = random.randint(10,12)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = random.sample(alphabet, rand_num)
    rand_upper = random.randint(0,len(letters) - 1)
    letters[rand_upper] = letters[rand_upper].upper()

    return letters


def create_numbers():
    """Must contain atleast 1 number"""
    rand_num = random.randint(2,5)
    number = random.sample(range(0,10), rand_num)
    return number


def create_special():
    """Must contain atleast one special character"""
    specical_char_list = ["!", "£", "$", "%", "^", "&", "*", "(", ")"]
    specical_char = random.sample(specical_char_list, 2)
    return specical_char


def generate_password():
    """Join all lists together to create password"""
    password = create_letters() + create_numbers() + create_special()
    random.shuffle(password)
    password = [str(char) for char in password]
    password = "".join(password)
    return password

generate_password()