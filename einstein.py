# einstein.py

def main():
    # Prompt the user for mass as an integer (in kilograms)
    mass = int(input("m: "))

    # Use the approximate value of the speed of light c, which is 3 * 10^8 meters per second
    speed_of_light = 3 * 10**8

    # Calculate the equivalent number of Joules using E = mc^2 with the approximated speed of light
    energy = mass * (speed_of_light ** 2)

    # Output the equivalent number of Joules rounded to the nearest integer
    print(f"E: {round(energy)}")

if __name__ == "__main__":
    main()
