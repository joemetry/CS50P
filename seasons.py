from datetime import date
import sys
import inflect

def main():
    # Prompt the user for their date of birth
    birth_date_str = input("Enter your date of birth (YYYY-MM-DD): ")
    
    # Convert the input string to a date object
    try:
        birth_date = date.fromisoformat(birth_date_str)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
        sys.exit(1)
    
    # Calculate the age in minutes
    age_in_minutes = calculate_age_in_minutes(birth_date)
    
    # Convert the age in minutes to English words
    age_in_words = convert_to_words(age_in_minutes)
    
    # Print the age in words with "minutes" at the end
    print(f"{age_in_words} minutes")

def calculate_age_in_minutes(birth_date):
    """Calculate the age in minutes given the birth date."""
    current_date = date.today()
    delta = current_date - birth_date
    age_in_days = delta.days
    age_in_minutes = age_in_days * 24 * 60
    return age_in_minutes

def convert_to_words(number):
    """Convert a number to English words."""
    p = inflect.engine()
    words = p.number_to_words(number, andword="")
    return words.capitalize()  # Capitalize the first letter

if __name__ == "__main__":
    main()
