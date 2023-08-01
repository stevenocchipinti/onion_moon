import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lib.stepper import Stepper
from lib.moonphase import Moonphase

stepper = Stepper(
    range=2048,
    pins=[0, 11, 2, 3],
    half_stepping=False,
    persist_to_file="current_step.txt"
)

print("Querying the current moonphase")
moonphase = Moonphase().current()

print("Setting position to {}%".format(moonphase * 100))
stepper.set_percentage(moonphase)
