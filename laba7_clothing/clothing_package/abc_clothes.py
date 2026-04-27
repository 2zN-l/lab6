from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size: int, price_per_meter: float, 
                 work_price_per_meter: float, accessories_price: float):
        self._size = size
        self._price_per_meter = price_per_meter
        self._work_price_per_meter = work_price_per_meter
        self._accessories_price = accessories_price
        self._fabric_meters = None

    @property
    def size(self) -> int:
        return self._normalize_size(self._size)
    
    @size.setter
    def size(self, value: int):
        if value < 44 or value > 54:
            raise ValueError("Размер должен быть в диапазоне от 44 до 54.")
        self._size = value
        self._fabric_meters = None

    @property
    @abstractmethod
    def fabric_meters(self) -> float:
        pass

    @property
    def total_cost(self) -> float:
        if self._fabric_meters is None:
            self._fabric_meters = self.fabric_meters
        fabric_cost = self._fabric_meters * self._price_per_meter
        work_cost = self._fabric_meters * self._work_price_per_meter
        return fabric_cost + work_cost + self._accessories_price

    @property
    @abstractmethod
    def type(self) -> str:
        pass

    def _normalize_size(self, size: int) -> int:
        available_sizes = [44, 46, 48, 50, 52, 54]
        if size < 44:
            return 44
        if size > 54:
            return 54
        return min(available_sizes, key=lambda x: abs(x - size))

    def __str__(self) -> str:
        return f"{self.type} (Размер: {self.size}, Стоимость: {self.total_cost:.2f} руб.)"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(size={self.size!r})"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Clothes):
            return NotImplemented
        return self.total_cost == other.total_cost

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Clothes):
            return NotImplemented
        return self.total_cost < other.total_cost
    
    def get_result_dict(self) -> dict:
        fabric = self.fabric_meters
        fabric_cost = fabric * self._price_per_meter
        work_cost = fabric * self._work_price_per_meter
        return {
            'type': self.type,
            'size': self.size,
            'fabric_meters': round(fabric, 2),
            'fabric_cost': round(fabric_cost, 2),
            'work_cost': round(work_cost, 2),
            'accessories': self._accessories_price,
            'total': round(self.total_cost, 2)
        }