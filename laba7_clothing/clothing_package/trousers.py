from .abc_clothes import Clothes

class TrousersCalculator(Clothes):
    """Класс для расчёта брюк."""
    
    _FABRIC_DICT = {
        44: 1.2, 46: 1.25, 48: 1.3, 50: 1.35, 52: 1.4, 54: 1.45,
    }
    
    def __init__(self, size: int):
        super().__init__(size=size, 
                         price_per_meter=800, 
                         work_price_per_meter=1000, 
                         accessories_price=300)

    @property
    def fabric_meters(self) -> float:
        """Расход ткани для брюк."""
        normalized_size = self.size
        return self._FABRIC_DICT.get(normalized_size, 1.3)
    
    @property
    def type(self) -> str:
        return "Брюки"