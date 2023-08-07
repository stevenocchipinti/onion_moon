# 🧅 🌗 Onion Moon

This project uses:

- [VisualCrossing.com](https://www.visualcrossing.com/) to query the current moonphase
- An [Onion Omega 2](https://onion.io/omega2/) development board
- A 28BYJ-48 Stepper Motor and ULN2003 driver

## Setup

1. Run `setup.sh`, which will use `opkg` to install:

   - `python` v2.7
   - A package to control the GPIO pins on the Onion Omega
   - `curl`

2. Create an API key on VisualCrossing.com and store it in an `API_KEY`
   environment variable

3. Open `scripts/main.py` and ensure the `Stepper` object is configured with the
   correct settings for:
   - `range`
     - _Required_
     - The number of steps for a full 360 degree revolution
   - `pins`
     - _Required_
     - A list of GPIO pins to drive the stepper motor
   - `delay`
     - \_Defaults to `0.05`
     - The delay between each step in the sequence, controlling speed
   - `half_stepping`
     - _Defaults to `False`_
     - Whether or not to use half stepping
   - `persist_to_file`
     - _Defaults to not persisting to a file_
     - A file path to store the state of the current position.
   - `dry_mode`
     - _Defaults to `False`_
     - Whether to just write to STDOUT instead of the GPIO

## Usage

```
python scripts/main.py           # Sets the stepper motor based on the current moon phase
python scripts/main.py reset     # Sets the stepper motor to 0%
python scripts/main.py set 0.25  # Sets the stepper motor to 25%
```

## FAQ

**Why use `curl` instead of doing it all in python?**

There wasn't much space left on the onion after installing python and when I
tried using standard python 2.7 tools for making HTTP requests, it couldn't
understand the HTTPS protocol and I couldn't find a way to fix it.

The other option was to use `pip` to install a third party package for this, but
there wasn't enough space for `pip`. Luckily, `curl` was very small!

There is probably a better solution than this, but this works.
