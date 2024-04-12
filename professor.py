import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        attempts = 0

        while attempts < 3:
            try:
                response = int(input(f"{x} + {y} = "))
                if response == answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            attempts += 1

        if attempts == 3:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be 1, 2, or 3")
    return random.randint(0, 10**level - 1)

if __name__ == "__main__":
    main()
