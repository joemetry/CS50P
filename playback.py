# playback.py

def main():
    # Prompt the user for input
    user_input = input("Please enter some text: ")

    # Replace each space with three periods
    playback_output = user_input.replace(" ", "...")

    # Output the modified input
    print(playback_output)

if __name__ == "__main__":
    main()
