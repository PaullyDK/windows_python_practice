import logging
logger = logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)

consoleHandler = logging.StreamHandler()

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s",
datefmt='%d/%m/%Y %I:%M:%S %p')

consoleHandler.setFormatter(formatter)
logger.addHandler(consoleHandler)

logger.critical("critical message")
logger.error("error message")
logger.warning("warning message")
logger.info("info message")
logger.debug("debug message")