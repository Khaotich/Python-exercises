import logging

#logowanie działa domyślnie z poziomem warning i wyżej
#ustawiamy podstawową konfigurację z plikiem i poziomem logów do zbierania
#sposoby formatowania z dokumentacji
logging.basicConfig(filename='data.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

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

logging.debug(f'Add: {num1} + {num2} = {add(num1, num2)}')
logging.debug(f'Subtract: {num1} - {num2} = {subtract(num1, num2)}')
logging.debug(f'Multiply: {num1} * {num2} = {multiply(num1, num2)}')
logging.debug(f'Divide: {num1} / {num2} = {divide(num1, num2)}')