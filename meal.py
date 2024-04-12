# meal.py

def main():
    time_str = input("Enter the time in 24-hour format (e.g., 13:45): ")
    time = convert(time_str)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

if __name__ == "__main__":
    main()
