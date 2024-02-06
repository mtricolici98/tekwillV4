speed_map = {
    'city': 50,
    'country': 70
}


class Car:

    def __init__(self):
        self._zone = 'city'
        self._overwrite_speed_limit = 0

    @property
    def speed_limit(self):
        if self._overwrite_speed_limit > 0:
            return min(speed_map.get(self._zone), self._overwrite_speed_limit)
        else:
            return speed_map.get(self._zone)

    @speed_limit.setter
    def speed_limit(self, new_value):
        self._overwrite_speed_limit = new_value

    def entered_city(self):
        self._zone = 'city'

    def left_city(self):
        self._zone = 'country'


car = Car()
print(car.speed_limit)
car.left_city()
print(car.speed_limit)

car.speed_limit = 10
print(car.speed_limit)
car.speed_limit = 100
print(car.speed_limit)
car.entered_city()
print(car.speed_limit)
car.speed_limit = 1
print(car.speed_limit)


class Temperature:

    def __init__(self):
        self._temperature = 0

    @property
    def temp(self):
        return self._temperature

    @temp.setter
    def temp(self, new_value):
        if not isinstance(new_value, (int, float)):
            raise TypeError("Invalid value")
        self._temperature = new_value
        self._log_temperature_change()

    def _log_temperature_change(self):
        with open('temp_history.txt', 'a') as file:
            file.write('{}\n'.format(self._temperature))


a = Temperature()
print(a.temp)
a.temp = 10
a.temp = 30
a.temp = 40
