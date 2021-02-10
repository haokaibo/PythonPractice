import logging

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