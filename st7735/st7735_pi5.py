import time
import numpy as np
import spidev
import lgpio  # Replaces gpiod with lgpio
from PIL import Image

__version__ = '0.1.0'

class ST7735:
    def __init__(self, port, cs, dc, backlight=None, rst=None, width=128, height=160, spi_speed_hz=5000000, invert=True, rotation=90, offset_left=0, offset_top=0):
        """
        Initialize the display with SPI and GPIO settings.

        Parameters:
            port (int): SPI port number.
            cs (int): SPI chip select.
            dc (int): Data/Command GPIO pin.
            backlight (int, optional): Backlight GPIO pin.
            rst (int, optional): Reset GPIO pin.
            width (int, optional): Display width.
            height (int, optional): Display height.
            spi_speed_hz (int, optional): SPI speed in Hz.
            invert (bool, optional): Invert display colors.
            rotation (int, optional): Display rotation (0, 90, 180, 270 degrees).
            offset_left (int, optional): Offset from the left.
            offset_top (int, optional): Offset from the top.
        """
        self._spi = spidev.SpiDev()
        try:
            self._spi.open(port, cs)
            self._spi.max_speed_hz = spi_speed_hz
        except Exception as e:
            raise RuntimeError(f"Failed to initialize SPI: {e}")

        self._h = lgpio.gpiochip_open(0)  # Open gpiochip0 with lgpio
        self._dc = dc
        self._rst = rst
        self._invert = invert  # Store the inversion state
        self.rotation = rotation  # Store the rotation state
        self.offset_left = offset_left  # Store the left offset
        self.offset_top = offset_top  # Store the top offset
        self.width = width  # Store the width of the display
        self.height = height  # Store the height of the display

        lgpio.gpio_claim_output(self._h, self._dc, 0)  # Set DC as output

        if backlight is not None:
            self._backlight = backlight
            lgpio.gpio_claim_output(self._h, self._backlight, 1)  # Enable backlight
        else:
            self._backlight = None

        if rst is not None:
            lgpio.gpio_claim_output(self._h, self._rst, 1)  # Set RST as output
        else:
            self._rst = None

        self.reset()
        self.init_display()

    def init_display(self):
        """ 
        Initialize the display with the basic configuration.
        """
        self.send(0x01, is_data=False)  # Software reset
        time.sleep(0.15)
        self.send(0x11, is_data=False)  # Sleep Out
        time.sleep(0.15)

        # Apply color inversion if necessary
        if self._invert:
            self.send(0x20, is_data=False)  # Color inversion on
        else:
            self.send(0x21, is_data=False)  # Color inversion off

        self.send(0x29, is_data=False)  # Display On

        # Apply initial rotation
        self.apply_rotation(self.rotation)

    def reset(self):
        """
        Perform a hardware reset of the display.
        """
        if self._rst is not None:
            lgpio.gpio_write(self._h, self._rst, 1)
            time.sleep(0.1)
            lgpio.gpio_write(self._h, self._rst, 0)
            time.sleep(0.1)
            lgpio.gpio_write(self._h, self._rst, 1)
            time.sleep(0.1)

    def send(self, data, is_data=True):
        """
        Send data or commands via SPI.

        Parameters:
            data (int or list): Data to send.
            is_data (bool, optional): True if sending data, False if sending command.
        """
        lgpio.gpio_write(self._h, self._dc, 1 if is_data else 0)
        if isinstance(data, int):
            data = [data & 0xFF]
        self._spi.xfer3(data)

    def apply_rotation(self, rotation):
        """
        Apply the display rotation.

        Parameters:
            rotation (int): Rotation angle (0, 90, 180, 270 degrees).
        """
        rotation_map = {
            0: 0x00,   # No rotation
            90: 0x60,  # 90° rotation
            180: 0xC0, # 180° rotation
            270: 0xA0  # 270° rotation
        }
        madctl = rotation_map.get(rotation, 0x00)
        self.send(0x36, False)  # MADCTL
        self.send(madctl)

    def set_window(self, x0, y0, x1, y1):
        """
        Set the window area for drawing.

        Parameters:
            x0 (int): Starting X coordinate.
            y0 (int): Starting Y coordinate.
            x1 (int): Ending X coordinate.
            y1 (int): Ending Y coordinate.
        """
        self.send(0x2A, False)  # CASET (Column Address Set)
        self.send([0x00, x0 + self.offset_left, 0x00, x1 + self.offset_left])
        self.send(0x2B, False)  # RASET (Row Address Set)
        self.send([0x00, y0 + self.offset_top, 0x00, y1 + self.offset_top])
        self.send(0x2C, False)  # RAMWR (Memory Write)

    def image(self, image):
        """
        Display an image on the screen.

        Parameters:
            image (PIL.Image): Image to display.
        """
        # Ensure the image is in RGB format
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Resize the image to match the display dimensions
        image = image.resize((self.width, self.height))

        # Convert image data to a format suitable for the display
        pixel_data = np.array(image)
        pixel_data = pixel_data.reshape(-1, 3)
        pixel_data = pixel_data.astype(np.uint8).tolist()

        # Send image data to display
        self.set_window(0, 0, self.width - 1, self.height - 1)
        for pixel in pixel_data:
            self.send(pixel[0])  # Red
            self.send(pixel[1])  # Green
            self.send(pixel[2])  # Blue

    def cleanup(self):
        """
        Release GPIO resources.
        """
        if self._backlight is not None:
            lgpio.gpio_write(self._h, self._backlight, 0)
        lgpio.gpiochip_close(self._h)

def main():
    """
    Main function to demonstrate the use of the ST7735 class.
    """
    try:
        display = ST7735(port=0, cs=0, dc=24, backlight=18, rst=25, invert=True, rotation=90, offset_left=0, offset_top=0)
        display.apply_rotation(90)
        
        # Example to draw a red rectangle
        display.set_window(10, 10, 60, 60)
        display.send([0xFF, 0x00, 0x00] * (50 * 50))  # Red color
        
        time.sleep(5)
    finally:
        display.cleanup()

if __name__ == "__main__":
    main()
