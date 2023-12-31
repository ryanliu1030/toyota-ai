
import random

from datetime import datetime
import uuid

class PosModel:

    def __init__(self, lon: float, lat: float,  ac: int, running : bool, prev_quote: str, range: int, mph: int):
        self.pos = {
            "_id": str(uuid.uuid4()),
            'pos': {             # Position as a subdocument
                    'lat': lat,  # Latitude
                     'lon': lon  # Longitude
            },
            "datetime": datetime.now(),
            "prev_quote": prev_quote,
            "AC": ac,
            "running": running,
            "range": range,
            "MPH": mph,
            "Mileage": random.randrange(1000,1000000)
        }
    def getData(self):
        return self.pos
