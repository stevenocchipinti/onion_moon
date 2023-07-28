class GPIO:
    def __init__(self, dry_mode):
        self.dry_mode = dry_mode

    def set_output(self, pin):
        if self.dry_mode:
            print(f"Setting pin {pin} as output")
        else:
            print("TODO: Access GPIO")

    def set(self, pin, value):
        if self.dry_mode:
            print(f"Setting pin {pin} to value {value}")
        else:
            print("TODO: Access GPIO")
