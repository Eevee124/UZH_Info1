#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        if not type(battery_size) == float or not type(battery_range_km) == float or battery_size < 0.0 or battery_range_km < 0.0:
            raise Warning("Input of invalid type!")

        self.__battery_size = battery_size
        self.__battery = battery_size
        self.__battery_range_km = battery_range_km

    def charge(self, kwh):
        if not type(kwh) == float or kwh <= 0.0:
            raise Warning("Invalid charge input!")
        self.__battery += kwh
        if self.__battery > self.__battery_size:
            self.__battery = 0
            raise Warning("Battery exploded, overcharged")

    def get_battery_status(self):
        return self.__battery, self.__battery_size

    def get_remaining_range(self):
        return self.__battery / self.__battery_size * self.__battery_range_km

    def drive(self, dist):
        if not type(dist) == float or dist <= 0.0:
            raise Warning("Invalid distance input!")

        if self.get_remaining_range() < dist:
            self.__battery = 0.0
            raise Warning("Empty battery! Need to recharge!")
        
        else: self.__battery -= (dist / self.__battery_range_km) * self.__battery_size