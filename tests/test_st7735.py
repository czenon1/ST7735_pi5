import unittest
from st7735_pi5 import ST7735

class TestST7735(unittest.TestCase):
    def test_initialization(self):
        display = ST7735(port=0, cs=0, dc=24, backlight=18, rst=25)
        self.assertIsNotNone(display)

    def test_display_image(self):
        display = ST7735(port=0, cs=0, dc=24, backlight=18, rst=25)
        display.image(Image.new('RGB', (display.width, display.height), 'white'))
        # Add assertions to verify the image was displayed correctly

    def test_cleanup(self):
        display = ST7735(port=0, cs=0, dc=24, backlight=18, rst=25)
        display.cleanup()
        # Add assertions to verify resources were released correctly

if __name__ == '__main__':
    unittest.main()
