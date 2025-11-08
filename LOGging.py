import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

# Prints this
# 11/08/2025 17:20:02 - root - DEBUG - This is a debug message
# 11/08/2025 17:20:02 - root - INFO - This is an info message
# 11/08/2025 17:20:02 - root - WARNING - This is a warning message
# 11/08/2025 17:20:02 - root - ERROR - This is an error message
# 11/08/2025 17:20:02 - root - CRITICAL - This is a critical message

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical("This is a critical message")