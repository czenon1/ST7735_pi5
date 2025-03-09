# ST7735_pi5
[![PyPi Package](https://img.shields.io/pypi/v/st7735.svg)](https://pypi.python.org/pypi/st7735_pi5)
[![Python Versions](https://img.shields.io/pypi/pyversions/st7735.svg)](https://pypi.python.org/pypi/st7735_pi5)

A Python library to control the ST7735 display on a Raspberry Pi 5 using `lgpio` and `spidev`.
Allows simple drawing on the display without installing a kernel module.

Designed specifically to work with a ST7735 based 128x160 pixel TFT SPI display. (Specifically the 0.96" SPI LCD from Pimoroni).

## Installing

You can install this library via pip:

```bash
pip install -r requirements.txt
pip install ST7735_pi5
```

## Usage

```python
from st7735_pi5 import ST7735
from PIL import Image

# Initialize the display
display = ST7735(port=0, cs=0, dc=24, backlight=18, rst=25)

# Display an image
image = Image.open('path_to_image.jpg')
display.image(image)
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
