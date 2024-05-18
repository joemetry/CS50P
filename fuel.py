def main():
    fraction = input("Fraction: ").strip()
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

def convert(fraction):
    try:
        numerator, denominator = map(int, fraction.split('/'))
        if numerator > denominator:
            raise ValueError("Numerator cannot be greater than denominator.")
        return round((numerator / denominator) * 100)
    except ValueError:
        raise ValueError("Invalid input. Both values should be integers.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator cannot be zero.")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
