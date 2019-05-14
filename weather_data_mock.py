
import random
from datetime import datetime

class WeatherDataMock:
  def get(self):
    output = {
      "temperature": {
        "value": round((random.random() * 30), 2),
        "date": datetime.now()
      }
    }
    return output