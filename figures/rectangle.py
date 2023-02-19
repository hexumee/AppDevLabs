from math import *
from figures import Figure, FiguresEnum, Square


class Rectangle(Square):
    __rectangle_side_a = 0
    __rectangle_side_b = 0

    def __init__(self, side_a: float, side_b: float):
        self._fig_type = FiguresEnum.Rectangle
        self.__rectangle_side_a = side_a
        self.__rectangle_side_b = side_b
    
    def __str__(self):
        return f"{self._fig_type.value} со стороной А={self.__rectangle_side_a} и стороной В={self.__rectangle_side_b}, площадью {self.area()} и периметром {self.perimeter()}"

    def area(self) -> float:
        return self.__rectangle_side_a*self.__rectangle_side_b

    def perimeter(self) -> float:
        return 2*(self.__rectangle_side_a+self.__rectangle_side_b)
    
    def get_figure_info(self) -> dict:
        return {"type": self._fig_type.value, "area": self.area(), "perimeter": self.perimeter(), "side_a": self.__rectangle_side_a, "side_b": self.__rectangle_side_b}
    
    def get_side_a(self) -> float:
        return self.__rectangle_side_a

    def set_side_a(self, value: float):
        self.__rectangle_side_a = value
    
    def get_side_b(self) -> float:
        return self.__rectangle_side_b

    def set_side_b(self, value: float):
        self.__rectangle_side_b = value
    
    def get_sides(self) -> tuple:
        return (self.__rectangle_side_a, self.__rectangle_side_b)

    def set_sides(self, value_a: float, value_b: float):
        self.__rectangle_side_a = value_a
        self.__rectangle_side_b = value_b
