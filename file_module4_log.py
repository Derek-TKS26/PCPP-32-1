# Logging is a means of tracking events that happen when some software runs.
# The Python Standard Library provides a logging module which allows writing status messages to a file or any other output streams.
# Logs are most often used to find the cause of an error.

# ———————————————————————————— Python Logging Levels ——————————————————————————————————————————————

# Debug: These are used to give Detailed information, typically of interest only when diagnosing problems.
# Info: These are used to confirm that things are working as expected
# Warning: These are used as an indication that something unexpected happened, or is indicative of some problem in the near future
# Error: This tells that due to a more serious problem, the software has not been able to perform some function
# Critical: This tells serious error, indicating that the program itself may be unable to continue running

# Beyond the above five levels, developers can create own levels if required.

# ————————————————————————————— Basic Concepts ————————————————————————————————————————————————————

# Handlers in Python's logging module are used to send log messages to different destinations, such as the console, files, or even external systems.
# Formatter in logging module is a method to set log records' format.

import logging

logging.basicConfig(level=logging.CRITICAL, filename='prod.log', filemode='a')

# First argument:passes a logging level, the function similar to setLevel method. If the arg is omitted then
# the default level is warming.

# Second argument: creates a FileHandler object if omitted then the default Handler is StreamHandler which can
# produces a str in the console.

# Third argument: 'a' is the default model which means the new log will be appended in previous records.



logger = logging.getLogger() # Create a logger object which can set the logging levels for you.

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')

