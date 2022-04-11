class Figure:
    name = "Figure"

    @property
    def area(self):
        return None

    @property
    def perimeter(self):
        return None

    def add_area(self, figure):
        if not issubclass(type(figure), Figure):
            raise ValueError("Wrong class")
        return self.area + figure.area

