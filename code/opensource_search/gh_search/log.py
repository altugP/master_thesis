import logging


# basic logger that prints to std:out and to a file called 'search.log'
# use logger.(debug|info|warning|error|critical)() when calling
logger = logging.getLogger('search_logger')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - (%(process)d) %(levelname)s: '
                           '%(message)s',
                    handlers=[logging.FileHandler('search.log'),
                              logging.StreamHandler()])