class Rectangle:
    def __init__(self, width=0, height=0):
        """
        Инициализация объекта треугольник

        >>> r = Rectangle(3, 4)
        >>> r.get_area()
        12
        >>> r.get_perimeter()
        14
        >>> r.set_dimensions(-1, -1)
        Traceback (most recent call last):
        ...
        ValueError: Высота и ширина должны быть больше 0
        """
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        if width < 0 or height < 0:
            raise ValueError('Высота и ширина должны быть больше 0')
        self.width = width
        self.height = height

    def get_area(self) -> int:
        if self.width < 0 or self.height < 0:
            raise ValueError('Высота и ширина должны быть больше 0')
        return self.width * self.height

    def get_perimeter(self) -> int:
        if self.width < 0 or self.height < 0:
            raise ValueError('Высота и ширина должны быть больше 0')
        return (self.width + self.height) * 2
