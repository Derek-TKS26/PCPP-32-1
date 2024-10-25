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




import logging

logger = logging.getLogger() # root logger object
hello_logger = logging.getLogger('hello') # the child of root logger object
hello_world_logger = logging.getLogger('hello.world')  # the child logger of 'hello'
recommended_logger = logging.getLogger(__name__)