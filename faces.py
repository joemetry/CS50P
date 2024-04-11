# faces.py

def convert(input_str):
    # Replace ':)' with '🙂' and ':(' with '🙁'
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    # Prompt the user for input
    user_input = input("Please enter some text: ")

    # Convert the input and print the result
    print(convert(user_input))

if __name__ == "__main__":
    main()
