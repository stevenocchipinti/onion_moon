import os
import json
import subprocess


class Moonphase:
    def __init__(self):
        location = "melbourne%2C%20australia"
        api_key = os.environ.get('API_KEY')

        if not api_key:
            raise KeyError(
                "Missing API key for visualcrossing.com - "
                "Please set an API_KEY envionment variable"
            )

        endpoint = (
            "https://weather.visualcrossing.com/"
            "VisualCrossingWebServices/rest/services/timeline/{}"
            "?unitGroup=metric&elements=moonphase&include=current"
            "&key={}&contentType=json"
        ).format(location, api_key)

        command = "curl -s '{}'".format(endpoint)
        output = subprocess.check_output(command, shell=True)
        self.data = json.loads(output)

    def current(self):
        return self.data["currentConditions"]["moonphase"]


# Manual test
if __name__ == "__main__":
    moonphase = Moonphase().current()
    print("Setting position to {}%".format(moonphase * 100))
