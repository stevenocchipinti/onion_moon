import os
import json
import urllib


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
        resp = urllib.urlopen(endpoint)

        self.data = json.loads(resp.read())

    def current(self):
        return self.data["currentConditions"]["moonphase"]


# Manual test
if __name__ == "__main__":
    moonphase = Moonphase().current()
    print("Setting position to {}%".format(moonphase * 100))
