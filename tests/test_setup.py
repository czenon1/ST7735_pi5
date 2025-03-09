import mock

def test_setup(lgpio, spidev, numpy, st7735):
    _ = st7735.ST7735(port=0, cs=0, dc=24)

    lgpio.gpio_claim_output.assert_has_calls([
        mock.call(lgpio.gpiochip_open(0), 24, 0)
    ], any_order=True)


def test_setup_no_invert(lgpio, spidev, numpy, st7735):
    _ = st7735.ST7735(port=0, cs=0, dc=24, invert=False)


def test_setup_with_backlight(lgpio, spidev, numpy, st7735):
    display = st7735.ST7735(port=0, cs=0, dc=24, backlight=4)

    display.set_backlight(True)

    lgpio.gpio_claim_output.assert_has_calls([
        mock.call(lgpio.gpiochip_open(0), 4, 1)
    ], any_order=True)


def test_setup_with_reset(lgpio, spidev, numpy, st7735):
    _ = st7735.ST7735(port=0, cs=0, dc=24, rst=4)

    lgpio.gpio_claim_output.assert_has_calls([
        mock.call(lgpio.gpiochip_open(0), 4, 1)
    ], any_order=True)
