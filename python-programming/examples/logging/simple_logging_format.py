import logging
    
logging.basicConfig( format = '%(asctime)s  %(levelname)-10s %(processName)s  %(name)s %(message)s')
    
logging.debug("debug") 
logging.info("info") 
logging.warning("warning") 
logging.error("error")
logging.critical("critical")