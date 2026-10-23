import logging
logger = logging.getLogger('demologger')
logger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler()
fileHandler= logging.FileHandler('abc.log',mode='w')

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s",
datefmt='%d/%m/%Y %I:%M:%S %p')

consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

logger.critical("critical message")
logger.error("error message")
logger.warning("warning message")
logger.info("info message")
logger.debug("debug message")
