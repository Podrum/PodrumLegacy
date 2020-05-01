from .utils import logger, config


def start(path):
    logger.log('info', 'Starting the server...')
    logger.log('info', path)
    config.Config.checkAllFiles(path)

