import sys

def count_lines_of_code(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            code_lines = 0
            for line in lines:
                stripped_line = line.strip()
                if stripped_line and not stripped_line.startswith("#"):
                    code_lines += 1
            return code_lines
    except FileNotFoundError:
        sys.exit(f"Error: {filename} does not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")
    elif not sys.argv[1].endswith('.py'):
        sys.exit("Error: File must be a Python file (.py)")
    else:
        filename = sys.argv[1]
        loc = count_lines_of_code(filename)
        print(f"Lines of Code: {loc}")
