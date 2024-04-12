import inflect

def main():
    names = []

    # Prompt the user for names until they input control-d
    while True:
        try:
            name = input()
            if name:
                names.append(name)
        except EOFError:
            break

    # Use inflect to format the list of names with commas and "and"
    p = inflect.engine()
    formatted_names = p.join(names)

    # Print the farewell message
    print(f"Adieu, adieu, to {formatted_names}")

if __name__ == "__main__":
    main()
