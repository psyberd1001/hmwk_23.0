class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin()
        self.__is_valid_numbers()

    def __is_valid_vin(self):
        min_vin = 1000000
        max_vin = 9999999
        vin_number = self.__vin
        if isinstance(vin_number, int) != True:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < min_vin or vin_number > max_vin:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self):
        numbers = self.__numbers
        if type(numbers) != str:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) > 6 or len(numbers) < 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')