from figures import Circle, Triangle, Square, Rectangle


if __name__ == "__main__":
    circle = Circle(4)
    triangle = Triangle(8)
    square = Square(16)
    rectangle = Rectangle(4, 16)

    print(circle)
    print(triangle)
    print(square)
    print(rectangle, "\n")
    
    circle.set_radius(12)
    triangle.set_side(2)
    square.set_side(4)
    rectangle.set_sides(8, 12)

    print(circle)
    print(triangle)
    print(square)
    print(rectangle)
