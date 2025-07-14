import logging
import logging.config



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
print(logging.__file__)

import logging_helper

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleExample')
logging.debug('this is a debug message')

# print exc_info(stack trace)
try:
    a=[1,2,3]
    val = a[4]
except Exception as e:
    logging.error(e, exc_info=True)

# trace back
import traceback
try:
    a=[1,2,3]
    val = a[4]
except:
    logging.error(f'This error is {traceback.format_exc()}')