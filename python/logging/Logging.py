#!/usr/bin/python

'''
@package   2014.12_LoggingTemplate.Logging
@webpage   https://docs.python.org/2/library/logging.html
           https://docs.python.org/2/howto/logging.html#logging-basic-tutorial
@brief     Simple logging configuration.
@details   
@author    Remus Avram
@date      2014.12
'''


import logging, logging.config

# logging configuration
logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('LoggingTemplate.Logging')



# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
