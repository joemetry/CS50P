from seasons import calculate_age_in_minutes
from datetime import date

def test_calculate_age_in_minutes():
    # Test with a known date of birth and current date
    birth_date = date(1990, 1, 1)
    current_date = date(2024, 3, 22)
    expected_age_in_minutes = (current_date - birth_date).days * 24 * 60
    
    # Temporarily set the current date in the calculate_age_in_minutes function to the test current date
    original_date_today = date.today
    date.today = lambda: current_date
    try:
        assert calculate_age_in_minutes(birth_date) == expected_age_in_minutes
    finally:
        # Restore the original date.today function
        date.today = original_date_today

    # Add more tests as needed
