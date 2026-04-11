class CoatCalculator:
    """Расчёт для пиджака"""
    
    # Расход ткани (метров) на разные размеры
    FABRIC_PER_SIZE = {
        44: 2.2,   # XS
        46: 2.3,   # S
        48: 2.4,   # M
        50: 2.5,   # L
        52: 2.6,   # XL
        54: 2.7,   # XXL
    }
    
    PRICE_PER_METER = 800  # руб/метр
    ACCESSORIES_PRICE = 500  # фурнитура (пуговицы, нитки)
    WORK_PRICE_PER_METER = 1200  # руб/метр - работа
    
    @classmethod
    def calculate_fabric(cls, size: int) -> float:
        """Рассчитать расход ткани в метрах"""
        if size < 44:
            size = 44
        if size > 54:
            size = 54
        # Интерполяция между размерами
        if size in cls.FABRIC_PER_SIZE:
            return cls.FABRIC_PER_SIZE[size]
        # Для промежуточных размеров
        nearest = min(cls.FABRIC_PER_SIZE.keys(), key=lambda x: abs(x - size))
        return cls.FABRIC_PER_SIZE[nearest]
    
    @classmethod
    def calculate_price(cls, size: int) -> dict:
        """Рассчитать полную стоимость"""
        fabric = cls.calculate_fabric(size)
        fabric_cost = fabric * cls.PRICE_PER_METER
        work_cost = fabric * cls.WORK_PRICE_PER_METER
        total = fabric_cost + work_cost + cls.ACCESSORIES_PRICE
        
        return {
            'type': 'Пиджак',
            'size': size,
            'fabric_meters': round(fabric, 2),
            'fabric_cost': round(fabric_cost, 2),
            'work_cost': round(work_cost, 2),
            'accessories': cls.ACCESSORIES_PRICE,
            'total': round(total, 2)
        }