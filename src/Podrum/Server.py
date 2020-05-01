from .utils import logger, config, fs

fs = fs.fs


def start(path):
    logger.log('info', 'Starting the server...')
    logger.log('info', path)
    fs.checkAllFiles(path)
