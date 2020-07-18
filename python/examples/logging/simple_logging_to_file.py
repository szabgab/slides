import logging
import time
 
logging.basicConfig(level = logging.INFO, filename = time.strftime("my-%Y-%m-%d.log"))
 
logging.debug("debug") 
logging.info("info") 
logging.warning("warning") 
logging.error("error")
logging.critical("critical")