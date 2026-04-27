class CoatCalculator:
    def __init__(self):
        self.FABRIC_PER_SIZE = {
            44: 2.2, 46: 2.3, 48: 2.4, 50: 2.5, 52: 2.6, 54: 2.7,
        }
        self.PRICE_PER_METER = 800 
        self.ACCESSORIES_PRICE = 500 
        self.WORK_PRICE_PER_METER = 1200 
    
    def calculate_fabric(self, size: int) -> float:
        if size < 44:
            size = 44
        if size > 54:
            size = 54
        if size in self.FABRIC_PER_SIZE:
            return self.FABRIC_PER_SIZE[size]
        nearest = min(self.FABRIC_PER_SIZE.keys(), key=lambda x: abs(x - size))
        return self.FABRIC_PER_SIZE[nearest]
    
    def calculate_price(self, size: int) -> dict:
        fabric = self.calculate_fabric(size)
        fabric_cost = fabric * self.PRICE_PER_METER
        work_cost = fabric * self.WORK_PRICE_PER_METER
        total = fabric_cost + work_cost + self.ACCESSORIES_PRICE
        
        return {
            'type': 'Пиджак',
            'size': size,
            'fabric_meters': round(fabric, 2),
            'fabric_cost': round(fabric_cost, 2),
            'work_cost': round(work_cost, 2),
            'accessories': self.ACCESSORIES_PRICE,
            'total': round(total, 2)
        }