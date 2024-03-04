import os
from nyct_gtfs import NYCTFeed
from datetime import datetime
from trains import arrivals_generator_interval
from display import Display


def main():
    mta_api_key = os.getenv("MTA_API_KEY")
    direction = "N"
    stop_id = "L10N"
    train = "L"
    interval = 10
    feed = NYCTFeed(train, mta_api_key)
    display = Display()
    for arrivals in arrivals_generator_interval(
        feed, train, stop_id, direction, interval
    ):
        if arrivals == "Error":
            message = "Error!"
        elif len(arrivals) == 0:
            message = "no trains"
        else:
            minutes, seconds = arrivals[0].get_minutes_seconds()
            message = f"{minutes}m {seconds}s"
        display.write(message)


if __name__ == "__main__":
    main()
