import object_generator


def test_square_generator():
    """
    This method check the square_generator method
    """
    assert object_generator.BoundingBoxSquare.generate(5)
    assert object_generator.BoundingBoxSquare.generate(15)
    assert object_generator.BoundingBoxSquare.generate(-5)
    assert object_generator.BoundingBoxSquare.generate(-15)


def test_rectangle_generator():
    """
    This method check the rectangle_generator method
    """
    assert object_generator.BoundingBoxRectangle.generate(5)
    assert object_generator.BoundingBoxRectangle.generate(15)
    assert object_generator.BoundingBoxRectangle.generate(-5)
    assert object_generator.BoundingBoxRectangle.generate(-15)


def test_circle_generator():
    """
    This method check the circle_generator method
    """
    assert object_generator.BoundingBoxCircle.generate(5)
    assert object_generator.BoundingBoxCircle.generate(15)
    assert object_generator.BoundingBoxCircle.generate(-5)
    assert object_generator.BoundingBoxCircle.generate(-15)


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
