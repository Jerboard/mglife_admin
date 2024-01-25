import logging
import traceback
from datetime import datetime
from os import path

from forlife_admin.settings import BASE_DIR


logging.basicConfig(filename=path.join(BASE_DIR, 'log.log'), level=logging.INFO)


def save_log(message: str, is_error: bool = False):
    timestamp = datetime.now()
    filename = traceback.format_exc()[1]
    line_number = traceback.format_exc()[2]
    log_text = f'{timestamp} {filename} {line_number}: {message}'
    if is_error:
        logging.error(log_text)
    else:
        logging.info(log_text)
