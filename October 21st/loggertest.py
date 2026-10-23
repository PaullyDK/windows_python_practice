import logging

#Logger
logger = logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)

#Handler
consoleHandler = logging.StreamHandler()

#Formatter
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                              datefmt='%d/%m/%Y %I:%M:%S %p')

#Formatter added to handler
consoleHandler.setFormatter(formatter)
#Handler added to logger
logger.addHandler(consoleHandler)

logger.critical('It is critical message')
logger.error('It is error message')
logger.warning('It is warning message')
logger.info('It is info message')
logger.debug('It is debug message')