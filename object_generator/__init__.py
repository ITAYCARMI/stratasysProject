import random
from math import pi


class BoundingBox(object):
    def __init__(self):
        pass

    def area(self):
        pass


class BoundingBoxCircle(BoundingBox):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    @staticmethod
    def circle_generator(limit):
        """
        This method creates random circles
        :param limit: given reference range
        :return: circle object
        example: {'x': 3, 'y': 3, 'radius': 2}
        """
        if limit < 0:
            return "invalid"
        x_center = random.choice(range(0, limit))
        y_center = random.choice(range(0, limit))
        radius = random.choice(range(0, int(limit / 2)))
        return BoundingBoxCircle(x_center, y_center, radius)

    def area(self):
        return pi * (self.radius ** 2)


class BoundingBoxQuadrangle(BoundingBox):
    def __init__(self):
        super().__init__()
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

    def area(self):
        return (self.x1 - self.x2)*(self.y1 - self.y2)


class BoundingBoxRectangle(BoundingBoxQuadrangle):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @staticmethod
    def rectangle_generator(limit):
        """
        This method creates random rectangles
        :param limit: given reference range
        :return: rectangle object
        example: {'x1': 3, 'y1': 2, 'x2': 5, 'y2': 5}
        """
        if limit < 0:
            return "invalid"
        x_first_point = random.choice(range(0, limit))
        y_first_point = random.choice(range(0, limit))
        x_second_point = random.choice(range(0, limit))
        y_second_point = random.choice(range(0, limit))
        return BoundingBoxRectangle(x_first_point, y_first_point, x_second_point, y_second_point)


class BoundingBoxSquare(BoundingBoxQuadrangle):
    def __init__(self, x1, x2):
        super().__init__()
        self.x1 = x1
        self.y1 = x1
        self.x2 = x2
        self.y2 = x2

    @staticmethod
    def square_generator(limit):
        """
        This method creates random squares and rectangles
        :param limit: given reference range
        :return: square object
        example: {'x1': 3, 'y1': 3, 'x2': 5, 'y2': 5}
        """
        if limit < 0:
            return "invalid"
        first_point = random.choice(range(0, limit))
        second_point = random.choice(range(0, limit))
        return BoundingBoxSquare(first_point, second_point)


def generate_array(size, limit):
    """
    This method creates array of objects
    :param size: give size array, number of objects
    :param limit: given reference range
    :return: array of objects
    example: [square: {'x1': 3, 'y1': 3, 'x2': 5, 'y2': 5},
              rectangle: {'x1': 3, 'y1': 2, 'x2': 5, 'y2': 5},
              circle: {'x': 3, 'y': 3, 'radius': 2}]
    """
    if limit < 0 or size < 0:
        return "invalid"
    array = []
    for i in range(0, size):
        rnd = random.choice([0, 1, 2])
        if rnd == 0:
            obj = BoundingBoxSquare.square_generator(limit)
        elif rnd == 1:
            obj = BoundingBoxCircle.circle_generator(limit)
        else:
            obj = BoundingBoxRectangle.rectangle_generator(limit)
        array.append(obj)
    return array
