def camel_to_snake(name):
    snake_case = ""
    for c in name:
        if c.isupper():
            snake_case += "_" + c.lower()
        else:
            snake_case += c
    return snake_case

def main():
    camel_case = input("Enter a variable name in camel case: ")
    snake_case = camel_to_snake(camel_case)
    print(f"The corresponding name in snake case is: {snake_case}")

if __name__ == "__main__":
    main()
