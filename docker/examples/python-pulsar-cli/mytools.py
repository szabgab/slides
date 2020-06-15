import logging
import os

def get_logger(name):
    log_file = name + '.log'
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-10s - %(message)s')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()
    sh.setLevel(logging.INFO)
    sh.setFormatter( log_format )
    logger.addHandler(sh)

    #if os.path.exists(log_file):
    #    os.unlink(log_file)
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)
    fh.setFormatter( log_format )
    logger.addHandler(fh)

    return logger

topic = 'text'
