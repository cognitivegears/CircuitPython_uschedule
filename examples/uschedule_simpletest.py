# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2021 Nathan Byrd

# SPDX-License-Identifier: MIT

import time
import uschedule as schedule


def greet():
    print("Hello, world!")


# Note: pass functions, not function calls - i.e. "greet", not "greet()"

# schedule every 10 seconds
schedule.every(10).seconds.do(greet)

# schedule every 10 minutes
schedule.every(10).minutes.do(greet)

# schedule once a day
schedule.every().day.at("10:30").do(greet)

# schedule from 5 to 10 minutes
schedule.every(5).to(10).minutes.do(greet)

# schedule on a particular day
schedule.every().monday.do(greet)

# schedule day and time
schedule.every().wednesday.at("13:15").do(greet)

# schedule once a minute at seventeen seconds
schedule.every().minute.at(":17").do(greet)


while True:
    # Run any pending jobs
    schedule.run_pending()
    time.sleep(1)
