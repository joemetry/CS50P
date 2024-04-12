def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(c for c in text if c not in vowels)

def main():
    text = input("Enter text: ")
    no_vowels_text = remove_vowels(text)
    print(f"Output: {no_vowels_text}")

if __name__ == "__main__":
    main()
