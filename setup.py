from setuptools import setup, find_packages

setup(
    name='ST7735_pi5',
    version='0.1.5',
    description='A Python library to control the ST7735 display on a Raspberry Pi 5 using lgpio and spidev',
    author='Christopher Zénon-Fall',
    author_email='',
    url='https://github.com/czenon1/ST7735_pi5',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'spidev',
        'lgpio',
        'Pillow'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
)
