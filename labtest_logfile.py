'''
Estimated time
30 min

Level of difficulty
Low

Objectives
improving the student's skills in creating logs;
improving the student's skills in creating their own handler and formatter.
Scenario
It's likely that the temperature of your phone battery can get pretty high. Check if that’s true. Write a program that will simulate the recording of battery temperatures with an interval of one minute. The simulation should contain 60 logs (the last hour).

To simulate temperatures, use one of the available random functions in Python. Temperatures should be drawn in the range of 20–40 degrees Celsius, and then saved in the following format:

LEVEL_NAME – TEMPERATURE_IN_CELSIUS UNIT => DEBUG – 20 C

The drawn temperatures should be assigned to the appropriate level depending on their value:

DEBUG = TEMPERATURE_IN_CELSIUS < 20
WARNING = TEMPERATURE_IN_CELSIUS >= 30 AND TEMPERATURE_IN_CELSIUS <= 35
CRITICAL = TEMPERATURE_IN_CELSIUS > 35

Put all logs in the battery_temperature.log file. The task will be completed when you implement your own handler and formatter.

'''

import logging
import random
import time

# Custom Formatter
class BatteryTempFormatter(logging.Formatter):
    def format(self, record):
        return f"{record.levelname} – {record.msg} C"

# Custom Handler
class BatteryTempHandler(logging.FileHandler):
    def __init__(self, filename):
        super().__init__(filename)
        formatter = BatteryTempFormatter()
        self.setFormatter(formatter)

# Create a logger
logger = logging.getLogger('BatteryTempLogger')
logger.setLevel(logging.DEBUG)

# Add our custom handler to the logger
handler = BatteryTempHandler('battery_temperature.log')
logger.addHandler(handler)

# Simulate recording temperatures for 60 minutes
for _ in range(60):
    temperature = random.uniform(20, 40)
    if temperature < 30:
        logger.debug(f"{temperature:.2f}")
    elif 30 <= temperature <= 35:
        logger.warning(f"{temperature:.2f}")
    else:
        logger.critical(f"{temperature:.2f}")
    time.sleep(1)  # Simulates the delay in real-time logging, optional

