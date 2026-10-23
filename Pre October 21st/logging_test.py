import logging

logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p'
)

print('Logging Demo')
logging.debug('Debug Information')
logging.info('Info Information')
logging.warning('Warning Information')
logging.error('Error Information')
logging.critical('Critical Information')
