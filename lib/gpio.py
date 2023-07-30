from onionGpio import OnionGpio


class FakeOnionGpio:
    def __init__(self, pin):
        self.pin = pin

    def setOutputDirection(self, defaultVal):
        print(
            "#{}: Set to output direction with {}".format(self.pin, defaultVal)
        )

    def setValue(self, val):
        print("#{}: Set value to {}".format(self.pin, val))


class GPIO:
    def __init__(self, pins, dry_mode=False):
        self.dry_mode = dry_mode
        if dry_mode:
            self.pins = {pin: FakeOnionGpio(pin) for pin in pins}
        else:
            self.pins = {pin: OnionGpio(pin) for pin in pins}

        for pin in pins:
            self.pins.get(pin).setOutputDirection(0)

    def set_all(self, values):
        if not len(values) == len(self.pins):
            raise ValueError("len(values) does not match len(pins)")
        for pin, value in zip(self.pins.values(), values):
            pin.setValue(value)


# Manual test
if __name__ == "__main__":
    gpio = GPIO([17, 18, 22, 23], dry_mode=True)
    gpio.set_all([0, 1, 0, 1])
