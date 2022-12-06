#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from public.combustion_car import CombustionCar
from public.electric_car import ElectricCar

class HybridCar:

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__mode = True #default to electric

    def switch_to_combustion(self):
        self.__mode = False

    def switch_to_electric(self):
        self.__mode = True

    def get_remaining_range(self):
        return ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)

    def drive(self, dist):
        if not type(dist) == float or dist <= 0.0: raise Warning("Invalid distance for hybrid!")

        if self.__mode:
            remaining = dist - ElectricCar.get_remaining_range(self)
        
            try: ElectricCar.drive(self, dist)
            except: 
                
                if self.get_gas_tank_status()[0] != 0: 
                    self.switch_to_combustion()
                    if remaining == 0: return 
                    self.drive(remaining)
                else: raise Warning("No battery OR gas!!!!")

        else:
            remaining = dist - CombustionCar.get_remaining_range(self)
            
            try: CombustionCar.drive(self, dist)
            except: 
            
                if self.get_battery_status()[0] != 0:
                    self.switch_to_electric()
                    if remaining == 0: return 
                    self.drive(remaining)
                else: raise Warning("No battery OR gas!!!!")
