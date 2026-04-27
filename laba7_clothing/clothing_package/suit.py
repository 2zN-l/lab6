from .coat import CoatCalculator
from .trousers import TrousersCalculator

class SuitCalculator:
    """Класс для расчёта костюма-тройки."""
    
    def __init__(self, size: int):
        self.coat = CoatCalculator(size)
        self.trousers = TrousersCalculator(size)
        self._vest_fabric = 0.8
        self._vest_work_price = 1000
        self._vest_accessories = 200

    @property
    def total_cost(self) -> float:
        vest_fabric_cost = self._vest_fabric * self.coat._price_per_meter
        vest_work_cost = self._vest_fabric * self._vest_work_price
        vest_total = vest_fabric_cost + vest_work_cost + self._vest_accessories
        return self.coat.total_cost + self.trousers.total_cost + vest_total

    @property
    def type(self) -> str:
        return "Костюм-тройка"

    @property
    def size(self) -> int:
        return self.coat.size
    
    # Dunder-методы
    def __str__(self) -> str:
        return f"{self.type} (Размер: {self.size}, Стоимость: {self.total_cost:.2f} руб.)"

    def __repr__(self) -> str:
        return f"SuitCalculator(size={self.size!r})"
    
    def get_result_dict(self) -> dict:
        """Возвращает словарь с результатами."""
        coat_data = self.coat.get_result_dict()
        trousers_data = self.trousers.get_result_dict()
        
        vest_fabric_cost = self._vest_fabric * self.coat._price_per_meter
        vest_work_cost = self._vest_fabric * self._vest_work_price
        vest_total = vest_fabric_cost + vest_work_cost + self._vest_accessories
        
        return {
            'type': self.type,
            'size': self.size,
            'coat': coat_data,
            'trousers': trousers_data,
            'vest': {
                'fabric_meters': self._vest_fabric,
                'fabric_cost': round(vest_fabric_cost, 2),
                'work_cost': round(vest_work_cost, 2),
                'accessories': self._vest_accessories,
                'total': round(vest_total, 2)
            },
            'total': round(self.total_cost, 2)
        }