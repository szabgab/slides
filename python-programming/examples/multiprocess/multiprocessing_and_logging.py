from multiprocessing import Pool
import os
import logging
import logging.handlers

count = 0
def f(x):
   global count
   count += 1
   #print("Input {} in process {}".format(x, os.getpid()))
   logger = logging.getLogger("app")
   logger.info("f({}) count {} in PID {}".format(x, count, os.getpid()))
   return x*x


def prt(z):
   print(z)

def setup_logger():
   level = logging.DEBUG
   logger = logging.getLogger("app")
   logger.setLevel(level)
   log_file = 'try.log'
   formatter = logging.Formatter('%(asctime)s - %(levelname)-8s - %(filename)-20s:%(lineno)-5d - %(funcName)-22s - %(message)s')
   ch = logging.FileHandler(log_file)
   #ch = logging.handlers.TimedRotatingFileHandler(log_file, when='D', backupCount=2)
   ch.setLevel(level)
   ch.setFormatter(formatter)
   logger.addHandler(ch)
   logger.info("Setup logger in PID {}".format(os.getpid()))

def main():
   logger = logging.getLogger('app')
   logger.info("main")

   with Pool(5) as p:
       results = p.imap(f, range(110)) # <multiprocessing.pool.IMapIterator object
       print(results)
       print('--')
       for r in results:
           print(r)

setup_logger()
if __name__ == '__main__':
   main()
