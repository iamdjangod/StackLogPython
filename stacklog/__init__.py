from .stacklog import StackLogHandler
__all__ = ['StackLogHandler']

# Publish this class to the "logging.handlers" module so that it can be use
# from a logging config file via logging.config.fileConfig().
import logging.handlers

logging.handlers.StackLogHandler = StackLogHandler
