class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin_number, car_numbers):
        self.model = model
        if self.__is_valid_vin(vin_number):
            self.__vin_number = vin_number
        if self.__is_valid_numbers(car_numbers):
            self.__car_numbers = car_numbers

    def __is_valid_vin(self, __vin_number):
        if not isinstance(__vin_number, int) or not 1000000 <= __vin_number <= 9999999:
            raise IncorrectVinNumber(
                'Некорректный тип vin номер' if not isinstance(__vin_number, int) else 'Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, __car_numbers):
        if not isinstance(__car_numbers, str) or len(__car_numbers) != 6:
            raise IncorrectCarNumbers(
                'Некорректный тип данных для номеров' if not isinstance(__car_numbers, str) else 'Неверная длина номера')
        return True


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