import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler


logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

stream_h = logging.StreamHandler()
stream_h.setLevel(logging.WARNING)
stream_h.setFormatter(formatter)

file_h = logging.FileHandler('file.log')
file_h.setLevel(logging.ERROR)
file_h.setFormatter(formatter)


logger.addHandler(stream_h)
logger.addHandler(file_h)

# logger.propagate=False
logger.info('Hello Kaibo.')
logger.warning('this is warning')
logger.error('this is error')

# rotate file handler
rotate_file_h =RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(rotate_file_h)
for _ in range(10000):
    logger.error('Hello, Kaibo!')

import time
rotate_time_h = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(rotate_time_h)
for _ in range(6):
    logger.info('Hello time log.')
    time.sleep(5)