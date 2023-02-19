from math import *
from figures import Figure, FiguresEnum


class Square(Figure):
    __square_side = 0

    def __init__(self, side: float):
        super(Square, self).__init__(FiguresEnum.Square)
        self.__square_side = side
    
    def __str__(self):
        return f"{self._fig_type.value} со стороной {self.__square_side}, площадью {self.area()} и периметром {self.perimeter()}"
    
    def area(self) -> float:
        return self.__square_side**2

    def perimeter(self) -> float:
        return 4*self.__square_side
    
    def get_figure_info(self) -> dict:
        return {"type": self._fig_type.value, "area": self.area(), "perimeter": self.perimeter(), "side": self.__square_side}

    def get_side(self) -> float:
        return self.__square_side

    def set_side(self, value: float):
        self.__square_side = value
