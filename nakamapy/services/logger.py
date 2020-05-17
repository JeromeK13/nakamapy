import logging
import logging.handlers
import os
import sys


class Logger(logging.Logger):
    def __init__(self):
        logging.Logger.__init__(self, logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(
            logging.Formatter(f'%(asctime)s | [%(process_name)s-%(process_id)s] | [%(levelname)s] | %(message)s'))
        self.addHandler(handler)

    def _log(self, level, msg, args, exc_info=None, extra=None):
        if extra is None:
            extra = {'process_name': 'NAKAMAPY', 'process_id': os.getpid()}

        super(Logger, self)._log(level, msg, args, exc_info, extra)
