import re

phone_number_check = False

def phone_number_dashes(phone_number):
    def insert_letter(string, letter, position):
        return string[:position] + letter + string[position:]
    
    # Add dashes to the phone number at specific positions
    formatted_phone_number = phone_number
    formatted_phone_number = insert_letter(formatted_phone_number, "-", 3)
    formatted_phone_number = insert_letter(formatted_phone_number, "-", 7)
    return formatted_phone_number

import re

phone_number_check = False

def phone_number_dashes(phone_number):
    def insert_letter(string, letter, position):
        return string[:position] + letter + string[position:]
    
    # Add dashes to the phone number at specific positions
    formatted_phone_number = phone_number
    formatted_phone_number = insert_letter(formatted_phone_number, "-", 3)
    formatted_phone_number = insert_letter(formatted_phone_number, "-", 7)
    return formatted_phone_number

while not phone_number_check:
    phone_number = input("What is your phone number: ")
    # Remove unwanted characters
    phone_number = re.sub(r"[ \-\(\)]", "", phone_number)
    
    # Validate the phone number
    if len(phone_number) != 10:
        print("This phone number is not 10 digits.")
    elif not phone_number.isdigit():
        print("This phone number includes characters other than numbers.")
    else:
        # Phone number is valid
        phone_number_check = True
        formatted_phone_number = phone_number_dashes(phone_number)
        print(f"Formatted Phone Number: {formatted_phone_number}")
