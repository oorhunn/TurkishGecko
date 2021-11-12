from pydantic import BaseModel
from datetime import datetime


class CandleStickDto(BaseModel):
    open_time: int
    open: float
    high: float
    low: float
    close: float
    volume: float

    def __init__(self, tempdata):
        dd = datetime.utcfromtimestamp(tempdata[0] / 1000)
        self.open_time = dd
        self.open = tempdata[1]
        self.high = tempdata[2]
        self.low = tempdata[3]
        self.close = tempdata[4]
        self.volume = tempdata[5]
