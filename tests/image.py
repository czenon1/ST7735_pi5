import sys
from PIL import Image
from ST7735_pi5 import ST7735

def display_image(image_path):
    """
    Display an image on the ST7735 LCD.

    Parameters:
        image_path (str): Path to the image file.
    """
    # Initialize the display
    #display = ST7735(port=0, cs=0, dc=24, backlight=18, rst=25, invert=False, rotation=0, offset_left=0, offset_top=0)
    display = ST7735(port=0, cs=0, dc=24, rst=25, rotation=90, width=160, height=128)

    try:
        # Open and resize the image
        image = Image.open(image_path)
        image = image.resize((display.width, display.height))

        # Convert the image to RGB format
        image = image.convert('RGB')

        # Display the image
        display.image(image)
    finally:
        display.cleanup()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 image.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    display_image(image_path)
