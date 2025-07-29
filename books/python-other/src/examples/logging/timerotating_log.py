import logging
import logging.handlers

log_file = "my.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.handlers.TimedRotatingFileHandler(log_file, when='M', backupCount=2)
ch.setLevel(logging.INFO)
ch.setFormatter( logging.Formatter('%(asctime)s - %(name)s - %(levelname)-10s - %(message)s') )
logger.addHandler(ch)


log = logging.getLogger(__name__)
log.debug("debug")
log.info("info")
log.warning("warning")
log.error("error")
log.critical("critical")
