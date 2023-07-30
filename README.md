# 🧅 🌗 Onion Moon

This project uses:

- VisualCrossing.com to query the current moonphase
- An Onion Omega 2 development board
- A 28BYJ-48 Stepper Motor and ULN2003 driver

## Setup and usage

1. Run `setup.sh`, which will use `opkg` to install:

- `python` v2.7
- A package to control the GPIO pins on the Onion Omega

2. Create an API key on VisualCrossing.com and store it in an `API_KEY`
   environment variable

3. Open `scripts/main.py` and ensure the `Stepper` object is configured with the
   correct settings for:

- `range` - The number of steps for a full 360 degree revolution
- `pins` - A list of GPIO pins to drive the stepper motor
- `half_stepping` - Whether or not to use half stepping
- `persist_to_file` - (Optional) file to store the state of the current position
- `dry_mode` - Whether to just write to STDOUT instead of the GPIO

4. Run `scripts/main.py`
