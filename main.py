import os
import time
from nyct_gtfs import NYCTFeed
from datetime import datetime
from trains import get_arrivals_at_station
from display import Display


def main():
    with open("/home/viraj/mta_api_key.txt") as f:
        mta_api_key=f.read().strip()
    direction = "N"
    stop_id = "L10N"
    train = "L"
    refresh_interval = 30
    feed = NYCTFeed(train, mta_api_key)
    display = Display()
    while True:
        arrivals = get_arrivals_at_station(feed, train, stop_id, direction)
        for t in range(refresh_interval):
            train_idx = 0 if t % 15 < 10 or len(arrivals) == 1 else 1
            if arrivals == "Error":
                display.write("Error!")
            elif len(arrivals) == 0:
                display.write("no trains")
            else:
                minutes, seconds = arrivals[train_idx].get_minutes_seconds()
                time_str = f"{minutes}:{seconds:02}"
                message = f"L{time_str:>5}"
                display.write(message)
            time.sleep(1)


if __name__ == "__main__":
    main()
