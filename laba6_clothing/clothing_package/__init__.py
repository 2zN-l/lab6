# Этот файл делает папку пакетом
from .coat import CoatCalculator
from .trousers import TrousersCalculator
from .suit import SuitCalculator

__all__ = ['CoatCalculator', 'TrousersCalculator', 'SuitCalculator']