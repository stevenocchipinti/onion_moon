class StepperSequencer:
    def __init__(self, number_of_pins=4, half_stepping=False):
        self.number_of_pins = number_of_pins
        self.half_stepping = half_stepping

    def pins_for_step(self, step):
        pins = [0] * self.number_of_pins

        if not self.half_stepping:
            phase = step % self.number_of_pins
            return [
                1 if index == phase else 0
                for index in range(self.number_of_pins)
            ]

        else:
            phase = step % (self.number_of_pins * 2)
            return [
                1 if index * 2 in [
                    phase,
                    phase - 1,
                    (phase + 1) % (self.number_of_pins * 2)
                ]
                else 0 for index in range(self.number_of_pins)
            ]

        return pins


# Test cases
if __name__ == "__main__":
    # Test full stepping
    sequencer_full = StepperSequencer(number_of_pins=4, half_stepping=False)
    assert sequencer_full.pins_for_step(0) == [1, 0, 0, 0]
    assert sequencer_full.pins_for_step(1) == [0, 1, 0, 0]
    assert sequencer_full.pins_for_step(2) == [0, 0, 1, 0]
    assert sequencer_full.pins_for_step(3) == [0, 0, 0, 1]
    assert sequencer_full.pins_for_step(4) == [1, 0, 0, 0]
    assert sequencer_full.pins_for_step(5) == [0, 1, 0, 0]
    assert sequencer_full.pins_for_step(6) == [0, 0, 1, 0]
    assert sequencer_full.pins_for_step(7) == [0, 0, 0, 1]

    # Test half stepping
    sequencer_half = StepperSequencer(number_of_pins=4, half_stepping=True)
    assert sequencer_half.pins_for_step(0) == [1, 0, 0, 0]
    assert sequencer_half.pins_for_step(1) == [1, 1, 0, 0]
    assert sequencer_half.pins_for_step(2) == [0, 1, 0, 0]
    assert sequencer_half.pins_for_step(3) == [0, 1, 1, 0]
    assert sequencer_half.pins_for_step(4) == [0, 0, 1, 0]
    assert sequencer_half.pins_for_step(5) == [0, 0, 1, 1]
    assert sequencer_half.pins_for_step(6) == [0, 0, 0, 1]
    assert sequencer_half.pins_for_step(7) == [1, 0, 0, 1]
    assert sequencer_half.pins_for_step(8) == [1, 0, 0, 0]
    assert sequencer_half.pins_for_step(9) == [1, 1, 0, 0]
    assert sequencer_half.pins_for_step(10) == [0, 1, 0, 0]
    assert sequencer_half.pins_for_step(11) == [0, 1, 1, 0]
    assert sequencer_half.pins_for_step(12) == [0, 0, 1, 0]
    assert sequencer_half.pins_for_step(13) == [0, 0, 1, 1]
    assert sequencer_half.pins_for_step(14) == [0, 0, 0, 1]
    assert sequencer_half.pins_for_step(15) == [1, 0, 0, 1]

    print("All tests passed!")
