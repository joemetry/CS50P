# bank.py

def main():
    greeting = input("Enter a greeting: ").strip().lower()
    reward = get_reward(greeting)
    print(f"${reward}")

def get_reward(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
