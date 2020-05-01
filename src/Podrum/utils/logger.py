from datetime import datetime
from .TextFormat import TextFormat


TextFormat = TextFormat()


def log(type_, content):
    time = datetime.now()
    if type_ == 'info':
        print(f'{TextFormat.BLUE}[INFO: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == 'warn':
        print(f'{TextFormat.YELLOW}[WARNING: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == 'error':
        print(f'{TextFormat.RED}[ERROR: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    elif type_ == 'success':
        print(f'{TextFormat.GREEN}[: {time.strftime("%H:%M")}]{TextFormat.WHITE} {content}')
    else:
        print(f'[{type_}: {time.strftime("%H:%M")}]{content}')