from colorama import init, Fore, Style

# Start Colorama
init()

INVALID_LETTERS = {"Ç", "Ğ", "İ", "Ş", "Ö", "Ü", "Q", "W", "X"}
MAX_PROVINCE_CODE = 81


def is_valid(plate_parts):
    # Checks whether the entered license plate parts form a valid format.
    # plate_parts (list): Space-separated list of license plates. For example: ['10', 'BAN', '155']
    if len(plate_parts) != 3:
        return False
    
    return (first_two_digits(plate_parts[0]) and  # Check the first two digits
            middle_letters(plate_parts[1]) and    # Check the middle letters
            last_four_digits(plate_parts[2]))     # Check the last four digits


def first_two_digits(code):
    # Checks the validity of the first two digits (province code).
    return code.isdigit() and 1 <= int(code) <= MAX_PROVINCE_CODE and len(code) == 2


def middle_letters(letters):
    # Checks the validity of the middle letters.
    if letters.isalpha() and letters.isupper() and 1 <= len(letters) <= 3:
        for letter in letters:
            if letter in INVALID_LETTERS:  # Invalid case check
                return False
        return True
    return False


def last_four_digits(digits):
    # Checks the validity of the trailing numbers.
    return digits.isdigit() and 0 < int(digits) and 1 <= len(digits) <= 4 and not digits.startswith("0")


def main():
    # It repeatedly prompts the user to enter the license plate number and checks its validity.
    # If the user enters 'q', the program terminates.
    print(Fore.RED + "\n----->‼️ 🚗 Türkiye License Plate Verification Program 🛻 ‼️ <-----" + Style.RESET_ALL)
    print("Enter the license plate in capital letters with spaces (Example: 10 BAN 123).")
    print("Type 'q' and press Enter to exit.")

    while True:
        user_input = input("\nPlate: ").strip()

        if user_input.lower() in ['q','Q']:
            print(Fore.YELLOW + "Exiting the program...👋👋\n" + Style.RESET_ALL)
            break

        plate_parts = user_input.split()

        if is_valid(plate_parts):
            print(Fore.GREEN + "✅ Valid License Plate" + Style.RESET_ALL)
        else:
            print(Fore.RED + "❌ Invalid License Plate" + Style.RESET_ALL)


if __name__== "__main__":
    main()
