import sys
import os
from PIL import Image, ImageOps

def overlay_shirt(input_image_path, output_image_path, shirt_image_path):
    try:
        # Open the input image and shirt image
        input_image = Image.open(input_image_path)
        shirt_image = Image.open(shirt_image_path)

        # Resize and crop the input image to match the shirt image size
        resized_input = ImageOps.fit(input_image, shirt_image.size)

        # Overlay the shirt image on the resized input image
        resized_input.paste(shirt_image, (0, 0), shirt_image)

        # Save the result to the output image path
        resized_input.save(output_image_path)
    except FileNotFoundError:
        sys.exit(f"Error: {input_image_path} does not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_image output_image")
    else:
        input_image_path = sys.argv[1]
        output_image_path = sys.argv[2]

        # Check if input and output have valid extensions and match
        valid_extensions = ['.jpg', '.jpeg', '.png']
        input_ext = os.path.splitext(input_image_path)[1].lower()
        output_ext = os.path.splitext(output_image_path)[1].lower()

        if input_ext not in valid_extensions or output_ext not in valid_extensions:
            sys.exit("Error: Input and output files must be .jpg, .jpeg, or .png")
        if input_ext != output_ext:
            sys.exit("Error: Input and output files must have the same extension")

        # Path to the shirt image (assuming it's in the same directory as this script)
        shirt_image_path = 'shirt.png'

        overlay_shirt(input_image_path, output_image_path, shirt_image_path)
