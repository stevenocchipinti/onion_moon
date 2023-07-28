import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lib.stepper import Stepper

stepper = Stepper(
    range=100,
    pins=[17, 18, 22, 23],
    half_stepping=False,
    persist_to_file="current_step.txt",
    dry_mode=True
)

stepper.set_percentage(0.7)
