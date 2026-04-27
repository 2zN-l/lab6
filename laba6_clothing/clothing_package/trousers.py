class TrousersCalculator:
    def __init__(self):
        self.FABRIC_PER_SIZE = {
            44: 1.2, 46: 1.25, 48: 1.3, 50: 1.35, 52: 1.4, 54: 1.45,
        }
        self.PRICE_PER_METER = 800
        self.ACCESSORIES_PRICE = 300
        self.WORK_PRICE_PER_METER = 1000
    
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
            'type': 'Брюки',
            'size': size,
            'fabric_meters': round(fabric, 2),
            'fabric_cost': round(fabric_cost, 2),
            'work_cost': round(work_cost, 2),
            'accessories': self.ACCESSORIES_PRICE,
            'total': round(total, 2)
        }