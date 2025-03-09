"""Test configuration.
These allow the mocking of various Python modules
that might otherwise have runtime side-effects.
"""
import sys

import mock
import pytest


@pytest.fixture(scope="function", autouse=False)
def st7735():
    import st7735
    yield st7735
    del sys.modules["st7735"]


@pytest.fixture(scope="function", autouse=False)
def lgpio():
    """Mock lgpio module."""
    sys.modules["lgpio"] = mock.MagicMock()
    sys.modules["lgpio.line"] = mock.MagicMock()
    yield sys.modules["lgpio"]
    del sys.modules["lgpio"]


@pytest.fixture(scope="function", autouse=False)
def spidev():
    """Mock spidev module."""
    spidev = mock.MagicMock()
    sys.modules["spidev"] = spidev
    yield spidev
    del sys.modules["spidev"]


@pytest.fixture(scope="function", autouse=False)
def numpy():
    """Mock numpy module."""
    numpy = mock.MagicMock()
    sys.modules["numpy"] = numpy
    yield numpy
    del sys.modules["numpy"]
