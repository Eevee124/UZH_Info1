#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        if not type(gas_capacity) == float or not type(gas_per_100km) == float or gas_capacity < 0.0 or gas_per_100km < 0.0:
            raise Warning("Invalid Input!")

        self.__gas: float = gas_capacity
        self.__gas_capacity: float = gas_capacity
        self.__gas_per_100km: float = gas_per_100km

    def fuel(self, f):
        if not type(f) == float or f <= 0.0:
            raise Warning("Invalid fuel input!")

        self.__gas += f
        if self.__gas > self.__gas_capacity:
            self.__gas = 0.0
            raise Warning("too much gas, tank flowed over")

    def get_gas_tank_status(self):
        return self.__gas, self.__gas_capacity

    def get_remaining_range(self):
        return self.__gas / self.__gas_per_100km * 100

    def drive(self, dist):
        if not type(dist) == float or dist <= 0.0:
            raise Warning("Invalid distance input!")

        if self.get_remaining_range() < dist:
            self.__gas = 0.0
            Warning("Gas tank fully depleted!")

        else: self.__gas -= (dist / 100.0) * self.__gas_per_100km
