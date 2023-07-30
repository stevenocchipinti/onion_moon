import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lib.stepper import Stepper
from lib.moonphase import Moonphase

stepper = Stepper(
    range=8,
    pins=[17, 18, 22, 23],
    half_stepping=False,
    persist_to_file="current_step.txt",
    dry_mode=True
)

print("Querying the current moonphase")
moonphase = Moonphase().current()

print("Setting position to {}%".format(moonphase * 100))
stepper.set_percentage(moonphase)
