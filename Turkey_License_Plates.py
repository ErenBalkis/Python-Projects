# In Türkiye, license plate regulations are generally as follows:
# The license plate format is "XX ABC 123" or "XX A 1234."
# The first two digits are the provincial license plate code and indicate the province where the vehicle is registered.
# The number of letters in the middle generally ranges from 1 to 3. A minimum of 1 letter and a maximum of 3 letters can be present.
# The number of digits following each letter varies from 2 to 4.
# In the license plate system, letters are generally distributed according to the province and district where the vehicle is registered.
# Only letters from the Latin alphabet are used, and some letters, such as Q, W, and X, are not used.


INVALID_LETTERS = {"Ç", "Ğ", "İ", "Ş", "Ö", "Ü", "Q", "W", "X"}
MAX_PROVINCE_CODE = 81


def is_valid(plate_parts):
    """
    Checks whether the entered license plate parts form a valid format.
    plate_parts (list): Space-separated list of license plates. For example: ['34', 'ABC', '123']
    """
    if len(plate_parts) != 3:
        return False
        
    return (is_province_code_valid(plate_parts[0]) and
            is_middle_letters_valid(plate_parts[1]) and
            is_last_digits_valid(plate_parts[2]))


def is_province_code_valid(code):
    """Checks the validity of the first two digits (province code)."""
    return code.isdigit() and len(code) == 2 and 1 <= int(code) <= MAX_PROVINCE_CODE


def is_middle_letters_valid(letters):
    """Checks the validity of the middle letters."""
    if letters.isalpha() and letters.isupper() and 1 <= len(letters) <= 3:
        for letter in letters:
            if letter in INVALID_LETTERS:  # Invalid case check
                return False
        return True
    return False


def is_last_digits_valid(digits):
    """Checks the validity of the trailing numbers."""
    return digits.isdigit() and not digits.startswith("0") and 1 <= len(digits) <= 4


def main():
    """
    It repeatedly prompts the user to enter the license plate number and checks its validity.
    If the user enters 'q', the program terminates.
    """
    print("--- Türkiye License Plate Verification Program ---")
    print("Enter the license plate in capital letters with spaces (Ex: 34 ABC 123).")
    print("Type 'q' and press Enter to exit.")

    while True:
        user_input = input("\nPlate: ").strip()

        if user_input.lower() in ['q','Q']:
            print("Exiting the program...")
            break

        plate_parts = user_input.split()

        if is_valid(plate_parts):
            print("✅ Valid License Plate")
        else:
            print("❌ Invalid License Plate")


if __name__ == "__main__":
    main()