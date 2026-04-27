from .abc_clothes import Clothes

class CoatCalculator(Clothes):
    """Класс для расчёта пиджака."""
    
    _FABRIC_DICT = {
        44: 2.2, 46: 2.3, 48: 2.4, 50: 2.5, 52: 2.6, 54: 2.7,
    }
    
    def __init__(self, size: int):
        super().__init__(size=size, 
                         price_per_meter=800, 
                         work_price_per_meter=1200, 
                         accessories_price=500)

    @property
    def fabric_meters(self) -> float:
        """Расход ткани для пиджака."""
        normalized_size = self.size
        return self._FABRIC_DICT.get(normalized_size, 2.5)
    
    @property
    def type(self) -> str:
        return "Пиджак"