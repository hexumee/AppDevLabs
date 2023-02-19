from enum import Enum
from abc import ABC, abstractmethod


class FiguresEnum(Enum):
    Circle = "Круг"
    Triangle = "Треугольник"
    Square = "Квадрат"
    Rectangle = "Прямоугольник"

class Figure(ABC):
    _fig_type = FiguresEnum

    def __init__(self, figure_type: FiguresEnum):
        self._fig_type = figure_type

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def get_figure_info(self) -> dict:
        pass
