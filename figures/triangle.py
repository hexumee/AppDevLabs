from math import *
from figures import Figure, FiguresEnum


class Triangle(Figure):
    __triangle_side = 0

    def __init__(self, side: float):
        super(Triangle, self).__init__(FiguresEnum.Triangle)
        self.__triangle_side = side
    
    def __str__(self):
        return f"{self._fig_type.value} со стороной {self.__triangle_side}, площадью {self.area()} и периметром {self.perimeter()}"
    
    def area(self) -> float:
        return ((self.__triangle_side**2)*sqrt(3))/4

    def perimeter(self) -> float:
        return 3*self.__triangle_side
    
    def get_figure_info(self) -> dict:
        return {"type": self._fig_type.value, "area": self.area(), "perimeter": self.perimeter(), "side": self.__triangle_side}
    
    def get_side(self) -> float:
        return self.__triangle_side

    def set_side(self, value: float):
        self.__triangle_side = value
