import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formater = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

file_hanlder = logging.FileHandler('data.log')
file_hanlder.setLevel(logging.DEBUG)
file_hanlder.setFormatter(formater)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formater)

logger.addHandler(file_hanlder)
logger.addHandler(stream_handler)

def add(x: int, y: int) -> int:
    return x + y

def subtract(x: int, y: int) -> int:
    return x - y

def multiply(x: int, y: int) -> int:
    return x * y

def divide(x: int, y: int) -> float:
    return x / y

num1 = 15
num2 = 6

logger.debug(f'Add: {num1} + {num2} = {add(num1, num2)}')
logger.debug(f'Subtract: {num1} - {num2} = {subtract(num1, num2)}')
logger.debug(f'Multiply: {num1} * {num2} = {multiply(num1, num2)}')
logger.debug(f'Divide: {num1} / {num2} = {divide(num1, num2)}')