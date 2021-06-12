import random
import string


print("Hello, Welcome to Password generator!")

# ask the user for length of password
length = int(input("\nEnter the length of your password: "))
if length >= 20:
    print("The length must be smaller than 20 characters! Please try again. ")
else:
    # ask the user for preferences (numbers, symbols, letters)
    selection = ''

    numbers = str(input("\nDo you want your password to have numbers, yes or no ? "))
    if numbers == 'yes':
        selection += string.digits

    symbols = str(input("\nDo you want your password to have symbols, yes or no ? "))
    if symbols == 'yes':
        selection += string.punctuation

    lowercase = str(input("\nDo you want your password to have lowercase letters, yes or no ? "))
    if lowercase == 'yes':
        selection += string.ascii_lowercase

    uppercase = str(input("\nDo you want your password to have uppercase letters, yes or no ? "))
    if uppercase == 'yes':
        selection += string.ascii_uppercase

    if selection == '':
        print(" Attention: You need to select at least one option with yes! Please try again. ")

    else:
        # password will be generated now
        password = ''

        count = 0
        while count < length:
            password += random.choice(selection)
            count = count + 1

        print("\n Here is your password: " + password)
        print("\n The program ends ")

