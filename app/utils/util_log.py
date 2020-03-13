import logging.config
import os

logging.config.fileConfig(os.path.normpath(os.path.join(os.path.dirname(__file__), '../../config/logging.conf')))
log = logging.getLogger('PyApp')