from threading import Thread
import time

from .utils import logger, fs


class Server(Thread):
    def __init__(self, path):
        super().__init__()
        fs.checkAllFiles(path)
        logger.log('info', 'Starting server...')

        ticking = True
        self.tickCount
        while ticking:
            time.sleep(0.002)
