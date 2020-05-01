from threading import Thread

from .utils import logger, fs


class Server(Thread):
    def __init__(self):
        super().__init__()
        fs.checkAllFiles('../')
        logger.log('info', 'Starting server...')
