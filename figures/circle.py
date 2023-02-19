from math import *
from figures import Figure, FiguresEnum
    

class Circle(Figure):
    __circle_radius = 0

    def __init__(self, radius: float):
        super(Circle, self).__init__(FiguresEnum.Circle)
        self.__circle_radius = radius

    def __str__(self):
        return f"{self._fig_type.value} радиуса {self.__circle_radius}, площадью {self.area()} и длиной окружности {self.perimeter()}"
    
    def area(self) -> float:
        return 3.14*(self.__circle_radius**2)

    def perimeter(self) -> float:
        return 2*3.14*self.__circle_radius
    
    def get_figure_info(self) -> dict:
        return {"type": self._fig_type.value, "area": self.area(), "perimeter": self.perimeter(), "radius": self.__circle_radius}
    
    def get_radius(self) -> float:
        return self.__circle_radius

    def set_radius(self, value: float):
        self.__circle_radius = value
