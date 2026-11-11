

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon=None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon, optional): Equipped weapon (default = None)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, damage) -> None:
        """Take damage when injured"""
        self._hp -= damage
        self._hp = max(self._hp, 0)

    def heal(self, healing : int) -> None:
        """"Add healing to health"""
        self._hp =min(self._hp + healing, self.hp_max)  

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon:
            damage_dealt = self.weapon.roll_damage()
        else:
            damage_dealt = self.damage

        target.take_damage(damage_dealt)


    @property
    def is_alive(self) -> bool:
        """Returns True if the character is alive, if not, it returns False"""
        return self._hp > 0

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    
    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"


class Warrior(Character):
    """Warrior subclass with armor defense"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon=None, armor: int = 5) -> None:
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.armor = armor

    def take_damage(self, damage) -> None:
        """Reduces incoming damage by armor before applying it"""
        effective_damage = max(0, damage - self.armor)
        super().take_damage(effective_damage)


class Mage(Character):
    """Mage subclass with mana-based spells"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon=None, mana: int = 30, mana_max: int = 30) -> None:
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target) -> None:
        """
        Uses spell attack for 10 mana dealing double base damage (ignoring weapon), 
        or falls back to base attack and restores 5 mana.
        """
        if self.mana >= 10:
            self.mana -= 10
            spell_damage = self.damage * 2
            target.take_damage(spell_damage)
        else:
            super().attack(target)
            self.mana = min(self.mana_max, self.mana + 5)