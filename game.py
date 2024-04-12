import random

def main():
    # Prompt the user for a level (positive integer)
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            pass

    # Randomly generate an integer between 1 and level, inclusive
    secret_number = random.randint(1, level)

    # Prompt the user to guess the integer
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                raise ValueError
            if guess < secret_number:
                print("Too small!")
            elif guess > secret_number:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            pass

if __name__ == "__main__":
    main()
