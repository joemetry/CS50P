import emoji

def main():
    user_input = input("Enter a string in English: ")
    emojized_text = emoji.emojize(user_input, language='alias')
    print("Emojized version:", emojized_text)

if __name__ == "__main__":
    main()
