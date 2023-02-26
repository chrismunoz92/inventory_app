class Ingredient:
    """An ingredient object"""
    
    def __init__(self, name: str = None, unitVolume: int = None, unitType: str = None):
        self.name = name
        self.unitNumber = unitVolume
        self.unitType = unitType

    def __str__(self):
        return f"({self.unitNumber} {self.unitType}) {self.name}"