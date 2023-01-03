import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning('This is a Warning')

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')

name = "Ohad"
logging.error('%s raised an error', name)

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)

logger = logging.getLogger('example_logger')
logger.warning('This is a warning')

logger = logging.getLogger(__name__)
logger.warning('This is a warning')

# =======================================================================
# you can read more here: https://docs.python.org/3/library/logging.html
# ========================================================================