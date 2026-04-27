from .coat import CoatCalculator
from .trousers import TrousersCalculator

class SuitCalculator:
    def __init__(self):
        self.VEST_FABRIC = 0.8
        self.VEST_WORK_PRICE = 1000
        self.VEST_ACCESSORIES = 200
    
    def calculate_price(self, size: int) -> dict:
        coat_calc = CoatCalculator()
        trousers_calc = TrousersCalculator()
        
        coat_data = coat_calc.calculate_price(size)
        trousers_data = trousers_calc.calculate_price(size)
        
        vest_fabric_cost = self.VEST_FABRIC * coat_calc.PRICE_PER_METER
        vest_work_cost = self.VEST_FABRIC * self.VEST_WORK_PRICE
        vest_total = vest_fabric_cost + vest_work_cost + self.VEST_ACCESSORIES
        
        total = coat_data['total'] + trousers_data['total'] + vest_total
        
        return {
            'type': 'Костюм-тройка',
            'size': size,
            'coat': coat_data,
            'trousers': trousers_data,
            'vest': {
                'fabric_meters': self.VEST_FABRIC,
                'fabric_cost': round(vest_fabric_cost, 2),
                'work_cost': round(vest_work_cost, 2),
                'accessories': self.VEST_ACCESSORIES,
                'total': round(vest_total, 2)
            },
            'total': round(total, 2)
        }