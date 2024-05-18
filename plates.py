import sys

def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    sys.exit(0)  # Ensure exit code 0 regardless of plate validity

def is_valid(s):
    # Check the length of the plate
    if not 2 <= len(s) <= 6:
        return False

    # Check if the first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check if the plate contains only letters and numbers
    if not s.isalnum():
        return False

    # Check if the plate contains at least one digit
    if not any(char.isdigit() for char in s):
        return False

    # Check if there are no letters after the first digit
    first_digit_index = next((i for i, char in enumerate(s) if char.isdigit()), None)
    if first_digit_index is not None and any(char.isalpha() for char in s[first_digit_index:]):
        return False

    # Check if the plate does not contain a 0 as the first digit after letters
    if s[first_digit_index] == '0':
        return False

    return True

if __name__ == "__main__":
    main()
