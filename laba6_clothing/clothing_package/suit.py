from .coat import CoatCalculator
from .trousers import TrousersCalculator

class SuitCalculator:
    """Расчёт для костюма-тройки (пиджак + брюки + жилет)"""
    
    VEST_FABRIC = 0.8  # жилет - 0.8 метра ткани
    
    @classmethod
    def calculate_price(cls, size: int) -> dict:
        # Получаем расчёты для пиджака и брюк
        coat_data = CoatCalculator.calculate_price(size)
        trousers_data = TrousersCalculator.calculate_price(size)
        
        # Расчёт для жилета
        vest_fabric = cls.VEST_FABRIC
        vest_fabric_cost = vest_fabric * CoatCalculator.PRICE_PER_METER
        vest_work_cost = vest_fabric * 1000  # работа для жилета
        vest_accessories = 200  # пуговицы для жилета
        vest_total = vest_fabric_cost + vest_work_cost + vest_accessories
        
        # Общая сумма
        total = coat_data['total'] + trousers_data['total'] + vest_total
        
        return {
            'type': 'Костюм-тройка',
            'size': size,
            'coat': coat_data,
            'trousers': trousers_data,
            'vest': {
                'fabric_meters': vest_fabric,
                'fabric_cost': round(vest_fabric_cost, 2),
                'work_cost': round(vest_work_cost, 2),
                'accessories': vest_accessories,
                'total': round(vest_total, 2)
            },
            'total': round(total, 2)
        }