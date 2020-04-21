import random


def square_generator(limit):
    """
    This method creates random squares and rectangles
    :param limit: given reference range
    :return: square object
    example: {'type': 'square', 'x1': 3, 'y1': 2, 'x2': 5, 'y2': 5}
    """
    # if we want just squares need to change y = x, example: y_first_point = x_first_point
    x_first_point = random.choice(range(0, limit))
    y_first_point = random.choice(range(0, limit))
    x_second_point = random.choice(range(0, limit))
    y_second_point = random.choice(range(0, limit))
    return {'type': 'square', 'x1': x_first_point, 'y1': y_first_point, 'x2': x_second_point, 'y2': y_second_point}


def circle_generator(limit):
    """
    This method creates random circles
    :param limit: given reference range
    :return: circle object
    example: {'type': 'circle', 'x': 3, 'y': 3, 'radius': 2}
    """
    x_center = random.choice(range(0, limit))
    y_center = random.choice(range(0, limit))
    radius = random.choice(range(0, int(limit / 2)))
    return {'type': 'circle', 'x': x_center, 'y': y_center, 'radius': radius}


def generate_array(size, limit):
    """
    This method creates array of objects
    :param size: give size array, number of objects
    :param limit: given reference range
    :return: array of objects
    example: [{'type': 'square', 'x1': 3, 'y1': 2, 'x2': 5, 'y2': 5, 'key': 0},
              {'type': 'circle', 'x': 3, 'y': 3, 'radius': 2, 'key': 1}]
    """
    array = []
    for i in range(0, size):
        rnd = random.choice([0, 1])
        if rnd == 0:
            obj = square_generator(limit)
        else:
            obj = circle_generator(limit)
        obj['key'] = str(i)
        array.append(obj)
    return array
