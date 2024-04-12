import sys
import random
from pyfiglet import Figlet

def main():
    # Check command-line arguments
    if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]
    elif len(sys.argv) == 1:
        font = None
    else:
        sys.exit("Usage: figlet.py [-f FONT]")

    # Create a Figlet object
    figlet = Figlet()

    # If a font is specified, check if it's valid and set it
    if font:
        if font not in figlet.getFonts():
            sys.exit(f"Error: Font '{font}' not found")
        figlet.setFont(font=font)
    else:
        # If no font is specified, choose a random font
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
        print(f"Using random font: {font}")

    # Prompt the user for text
    text = input("Enter text: ")

    # Render and print the text in the specified font
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
