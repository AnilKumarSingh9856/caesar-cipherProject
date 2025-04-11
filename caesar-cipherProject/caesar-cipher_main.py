from art import logo

# Colored print helper
def colored(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

alphabet = [chr(i) for i in range(97, 123)]  # a-z

def caesar(direction, text, shift):
    result = ""
    shift = shift % 26
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter.isalpha():
            pos = alphabet.index(letter.lower())
            new_pos = (pos + shift) % 26
            result += alphabet[new_pos]
        else:
            result += letter
    return result

def get_shift():
    while True:
        shift_input = input(colored("Type the shift number:\n", "94"))
        if shift_input.isdigit():
            return int(shift_input)
        else:
            print(colored("Invalid input! Please enter a valid integer.", "91"))

def get_continue_choice():
    while True:
        choice = input(colored("Type 'yes' to go again or 'no' to exit:\n", "95")).lower()
        if choice in ["yes", "no"]:
            return choice
        else:
            print(colored("Please choose either 'yes' or 'no'.", "91"))

# Start
print(colored(logo, "96"))
print(colored("Welcome to the Caesar Cipher Tool!", "92"))

while True:
    direction = input(colored("Type 'encode' to encrypt, 'decode' to decrypt:\n", "93")).lower()
    if direction not in ["encode", "decode"]:
        print(colored("Please choose 'encode' or 'decode'.", "91"))
        continue

    text = input(colored("Type your message:\n", "94")).lower()
    shift = get_shift()

    result = caesar(direction, text, shift)
    print(colored(f"The {direction}d text is: {result}", "92"))

    again = get_continue_choice()
    if again == "no":
        print(colored("Goodbye, Raja ji! 👋", "96"))
        break
