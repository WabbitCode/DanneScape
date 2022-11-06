class Weapon:
    def __init__(self, wName, wPower, wAim):
        self.name = wName
        self.pow = wPower
        self.aim = wAim


class Armor:
    def __init__(self, aName, aDefPoints):
        self.name = aName
        self.dp = aDefPoints


class Potion:
    def __init__(self, pName, multiplier):
        self.name = pName
        self.multiP = multiplier


class Armor_Misc:
    def __init__(self, amName, amPower):
        self.name = amName
        self.power = amPower
