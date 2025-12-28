import logging

logging.basicConfig(filename="log_01.log",
                    level=logging.WARNING,
                    format="%(asctime)s-%(levelname)s -%(message)s")

#%(asctime)s: Timestamp of the log.
#%(levelname)s: The severity level.
#%(message)s: The actual log message.

logging.debug("This is a debug message") #1
logging.info("This is info msg") #2
logging.warning("Warning msg")  #3
logging.error("Error msg")  #4
logging.critical("critical msg")  #5