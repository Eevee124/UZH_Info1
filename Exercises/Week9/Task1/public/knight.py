#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from public.character import Character
class Knight(Character):
    
#reduces phys damage by 25% and deal 20% less damage

#dealt damage get the caused damage and reduce it by 20%
    def _get_caused_dmg(self, other):
        return round(0.8 * super()._get_caused_dmg(other))

#taken physical damage reduced by 25%
    def _take_physical_damage(self, amount):
        return round(0.75 * super()._take_physical_damage(amount))
