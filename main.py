import string
import random

characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")


def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)


option = input("Do you want to generate a password? (\033[1;32mYes\033[m/\033[1;31mNo\033[m): ").upper()[0]


if option in "Yy":
    generate_password()
elif option in "Nn":
    print("Program ended")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()
