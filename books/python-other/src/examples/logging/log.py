import logging
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
 
fh = logging.FileHandler('my.log')
fh.setLevel(logging.INFO)
fh.setFormatter( logging.Formatter('%(asctime)s - %(name)s - %(levelname)-10s - %(message)s') )
logger.addHandler(fh)
 
 
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)-10s - %(message)s'))
logger.addHandler(sh)
 
 
 
log = logging.getLogger(__name__)
log.debug("debug") 
log.info("info") 
log.warning("warning") 
log.error("error")
log.critical("critical")