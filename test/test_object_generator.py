import object_generator


def test_square_generator():
    """
    This method check the square_generator method
    """
    assert object_generator.BoundingBoxSquare.square_generator(5)
    assert object_generator.BoundingBoxSquare.square_generator(15)
    assert object_generator.BoundingBoxSquare.square_generator(-5)
    assert object_generator.BoundingBoxSquare.square_generator(-15)


def test_rectangle_generator():
    """
    This method check the rectangle_generator method
    """
    assert object_generator.BoundingBoxRectangle.rectangle_generator(5)
    assert object_generator.BoundingBoxRectangle.rectangle_generator(15)
    assert object_generator.BoundingBoxRectangle.rectangle_generator(-5)
    assert object_generator.BoundingBoxRectangle.rectangle_generator(-15)


def test_circle_generator():
    """
    This method check the circle_generator method
    """
    assert object_generator.BoundingBoxCircle.circle_generator(5)
    assert object_generator.BoundingBoxCircle.circle_generator(15)
    assert object_generator.BoundingBoxCircle.circle_generator(-5)
    assert object_generator.BoundingBoxCircle.circle_generator(-15)


def test_generate_array():
    """
    This method check the generate_array method
    """
    assert object_generator.generate_array(2, 5)
    assert object_generator.generate_array(2, 15)
    assert object_generator.generate_array(2, -5)
    assert object_generator.generate_array(2, -15)
    assert object_generator.generate_array(-2, 5)
    assert object_generator.generate_array(-2, 15)
    assert object_generator.generate_array(-2, -5)
    assert object_generator.generate_array(-2, -15)
