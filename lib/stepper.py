import os

from .stepper_sequencer import StepperSequencer
from .gpio import GPIO


class Stepper:
    def __init__(
        self,
        range,
        pins,
        half_stepping=False,
        persist_to_file=None,
        dry_mode=False
    ):
        self.range = range
        self.pins = pins
        self.sequencer = StepperSequencer(len(self.pins), half_stepping)
        self.file = persist_to_file
        self.current_step = self._load_current_step_from_file()
        self.gpio = GPIO(dry_mode=dry_mode)

        self._initialize_gpio()

    def forward(self, steps=1):
        for _ in range(steps):
            self._step(1)

    def backward(self, steps=1):
        for _ in range(steps):
            self._step(-1)

    def set_percentage(self, percentage):
        desired_step = round(percentage * self.range)
        steps = desired_step - self.current_step
        if steps > 0:
            self.forward(steps)
        elif steps < 0:
            self.backward(abs(steps))

    def reset(self):
        self.set_percentage(0)

    # Private methods

    def _initialize_gpio(self):
        for pin in self.pins:
            self.gpio.set_output(pin)

    def _step(self, increment=1):
        self.current_step += increment
        self._set_pins(self.sequencer.pins_for_step(self.current_step))
        self._write_current_step_to_file()

    def _set_pins(self, pins):
        for value, index in zip(pins, range(len(self.pins))):
            self.gpio.set(self.pins[index], value)

    def _load_current_step_from_file(self):
        if self.file and os.path.exists(self.file):
            with open(self.file, 'r') as f:
                return int(f.read().strip())
        else:
            return 0

    def _write_current_step_to_file(self):
        if self.file:
            with open(self.file, 'w') as f:
                f.write(str(self.current_step))
