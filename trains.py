import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional, List, Tuple


@dataclass
class StationStop:
    time: datetime
    name: str

    @property
    def time_left(self) -> timedelta:
        return self.time - datetime.now()

    @property
    def happened(self)-> bool:
        return self.time < datetime.now()

    def get_minutes_seconds(self) -> Tuple[int, int]:
        minutes = self.time_left.seconds // 60
        seconds = self.time_left.seconds % 60
        return minutes, seconds

    @property
    def formatted_time_left(self) -> str:
        minutes, seconds = self.get_minutes_seconds()
        return f"{minutes}m {seconds}s"

    def __str__(self):
        return f"Arriving at {self.name} in {self.formatted_time_left}"


def get_arrival_at_station(
    train, stop_id: str, direction: str
) -> Optional[StationStop]:
    if train.direction != direction:
        return None
    stop_time_updates = train.stop_time_updates
    for stop in stop_time_updates:
        if stop.stop_id == stop_id:
            return StationStop(stop.arrival, stop.stop_name)
    return None


def get_arrivals_at_station(
    feed, train: str, stop_id: str, direction: str
) -> List[StationStop]:
    feed.refresh()
    arrivals = [
        get_arrival_at_station(train, stop_id, direction) for train in feed.trips
    ]
    now = datetime.now()
    cleaned_arrivals = []
    for a in arrivals:
        if a and now < a.time:
            cleaned_arrivals.append(a)

    return cleaned_arrivals
