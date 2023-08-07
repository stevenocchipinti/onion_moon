import time
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
    def __init__(self, pins, delay, dry_mode=False):
        self.delay = delay
        self.dry_mode = dry_mode
        if dry_mode:
            self.pins = [(pin, FakeOnionGpio(pin)) for pin in pins]
        else:
            self.pins = [(pin, OnionGpio(pin)) for pin in pins]

        for (pin, pinObj) in self.pins:
            pinObj.setOutputDirection(0)

    def set_all(self, values):
        if not len(values) == len(self.pins):
            raise ValueError("len(values) does not match len(pins)")
        time.sleep(self.delay)
        for (index, (pin, pinObj)) in enumerate(self.pins):
            pinObj.setValue(values[index])


# Manual test
if __name__ == "__main__":
    gpio = GPIO([0, 11, 2, 3], delay=0.05)
    gpio.set_all([0, 0, 0, 0])
