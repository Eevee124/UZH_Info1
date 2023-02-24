#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from public.character import Character
class Mage(Character):

#mage does 25% more damage overall
    def _get_caused_dmg(self, other):
        return round(1.25 * super()._get_caused_dmg(other))

#mage does magical damage, not physical
    def attack(self, other):
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_magical_damage(self._get_caused_dmg(other))

#Mage takes 50% more damage from both physical damage and magical damage
    def _take_physical_damage(self, amount):
        return round(1.5 * super()._take_physical_damage(amount))

    def _take_magical_damage(self, amount):
       return round(1.5 * super()._take_magical_damage(amount))