# ST7735_pi5
[![PyPi Package](https://img.shields.io/pypi/v/st7735.svg)](https://pypi.python.org/pypi/st7735_pi5)
[![Python Versions](https://img.shields.io/pypi/pyversions/st7735.svg)](https://pypi.python.org/pypi/st7735_pi5)

A Python library to control the ST7735 display on a Raspberry Pi 5 using `lgpio` and `spidev`.
Allows simple drawing on the display without installing a kernel module.

Designed specifically to work with a ST7735 based 128x160 pixel TFT SPI display. (Specifically the 0.96" SPI LCD from Pimoroni).
## Building
Instructions from Pypa's[guide](https://github.com/pypa/packaging.python.org/blob/main/source/tutorials/packaging-projects.rst?plain=true)

### Generating distribution archives

The next step is to generate :term:`distribution packages <Distribution Package>`
for the package. These are archives that are uploaded to the Python
Package Index and can be installed by :ref:`pip`.

Make sure you have the latest version of PyPA's :ref:`build` installed:

**Unix/macOS :**
```bash
    python3 -m pip install --upgrade build
```
**Windows :**
```bat
    py -m pip install --upgrade build
```
*If you have trouble installing these, see the *`installing-packages`*tutorial.*

Now run this command from the same directory where :file:`pyproject.toml` is located:

**Unix/macOS :**
```bash
        python3 -m build
```

**Windows :**
```bat
        py -m build
```

This command should output a lot of text and once completed should generate two
files in the :file:`dist` directory:

```text

    dist/
    ├── example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
    └── example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz

```

The ``tar.gz`` file is a :term:`source distribution <Source Distribution (or "sdist")>`
whereas the ``.whl`` file is a :term:`built distribution <Built Distribution>`.
Newer :ref:`pip` versions preferentially install built distributions, but will
fall back to source distributions if needed. You should always upload a source
distribution and provide built distributions for the platforms your project is
compatible with. In this case, our example package is compatible with Python on
any platform so only one built distribution is needed.

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
