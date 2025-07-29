import logging

logging.debug("debug") 
logging.info("info") 
logging.warning("warning") 
logging.error("error")
logging.critical("critical")

logging.log(logging.WARNING, "another warning")
logging.log(40, "another error")

