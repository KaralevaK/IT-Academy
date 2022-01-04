# HW8 task 2 - a random password generator-function.
from string import ascii_letters, digits
from random import SystemRandom 

def generate_password(len_password = 10, flag_special_characters = True):
    """
    This is a random password generator-function.
    """
    special_characters='~`!@#$%^&*()_-+={[}]|\:;"\'<,>.?/'
    alphabet = ascii_letters + digits
    if flag_special_characters:
        alphabet = alphabet + special_characters
    new_password = ""
    while True:
        new_password=''.join(SystemRandom().choices(alphabet,k=len_password))
        yield new_password

def get_len_password():
    """
    This is a function to get the password length value from the user.
    """
    while True:
        len_password = input("Enter password length: ")
        if len_password.isdigit() and int(len_password) != 0:
            return int(len_password)
        else:
            print("Password length can only be a positive integer.")

def include_special_characters():
    """
    This is a function to get information from the user about the need to enable special characters.
    """
    while True:
        flag_special_characters = input("Is it possible to use special characters(~`!@#$%^&*()_-+={[}]|\:;\"'<,>.?/) in a password?\
 Enter \"yes\" or \"no\": ")
        if flag_special_characters == "yes":
            flag_special_characters = True
            break
        elif flag_special_characters == "no":
            flag_special_characters = False
            break
        else:
            print("Please, enter \"yes\" or \"no\".")
    return flag_special_characters

def get_numbers_of_passwords():
    """
    This is a function to get information about the number of passwords a user needs.
    """
    while True:
        numbers_of_passwords = input("Enter the number of passwords you want to generate: ")
        if numbers_of_passwords.isdigit() and int(numbers_of_passwords) > 0:
            return int(numbers_of_passwords)
        else:
            print("Numbers of passwords can only be a positive integer.")

if __name__== "__main__":
    while True:
        choise = input("Do you want to generate new passwords? Enter \"yes\" or \"no\": ")
        if choise == "no":
            print("Have a good day!")
            break
        if choise == "yes":
            print("Let's set the rules.")
            len_password = get_len_password()
            flag_special_characters = include_special_characters()
            numbers_of_passwords = get_numbers_of_passwords()
            gen = iter(generate_password(len_password, flag_special_characters))
            for i in range(numbers_of_passwords):
                print(f"Password #{i+1}: ", next(gen))
        else:
            print("Incorrect input. Try again.")

