from .utils import logger, config, fs
from threading import Thread

fs = fs.fs


class Server(Thread):
    def __init__(self):
        super().__init__()
        logger.log('info', 'Starting server...')
