import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lib.stepper import Stepper
from lib.moonphase import Moonphase

stepper = Stepper(
    range=2048,
    pins=[3, 2, 1, 0],
    delay=0.05,
    half_stepping=False,
    persist_to_file="current_step.txt"
)

try:
    if len(sys.argv) == 1:
        print("Querying the current moonphase")
        moonphase = Moonphase().current()
        print("Setting position to {}%".format(moonphase * 100))
        stepper.set_percentage(moonphase)

    elif len(sys.argv) == 2 and sys.argv[1] == "reset":
        print("Resetting back to 0%")
        stepper.set_percentage(0)

    elif len(sys.argv) == 3 and sys.argv[1] == "set":
        try:
            percentage = float(sys.argv[2])
            print("Setting position to {}%".format(percentage * 100))
            stepper.set_percentage(percentage)
        except ValueError:
            print("Invalid argument. Please provide a value floating-point number.")

except KeyboardInterrupt:
    print("Stopping")

finally:
    print("Turning off the GPIO pins")
    stepper.off()
