import utils
import object_generator

# squares
s1 = object_generator.BoundingBoxSquare(3, 5)
s2 = object_generator.BoundingBoxSquare(-3, 5)
s3 = object_generator.BoundingBoxSquare(5, 3)
s4 = object_generator.BoundingBoxSquare(-5, -3)
s5 = object_generator.BoundingBoxSquare(1, 2)
# rectangle
r1 = object_generator.BoundingBoxRectangle(3, 4, 4, 7)
r2 = object_generator.BoundingBoxRectangle(3, 4, 2, 7)
r3 = object_generator.BoundingBoxRectangle(-3, 4, 5, 7)
r4 = object_generator.BoundingBoxRectangle(-3, -4, -2, -4)
r5 = object_generator.BoundingBoxRectangle(6, 4, 7, 7)
r6 = object_generator.BoundingBoxRectangle(9, 2, 11, 6)

# circle
c1 = object_generator.BoundingBoxCircle(3, 5, 2)
c2 = object_generator.BoundingBoxCircle(3, 5, 4)
c3 = object_generator.BoundingBoxCircle(-3, 5, 2)
c4 = object_generator.BoundingBoxCircle(3, 5, -2)
c5 = object_generator.BoundingBoxCircle(5, 3, 2)
c6 = object_generator.BoundingBoxCircle(5, 10, 2)
c7 = object_generator.BoundingBoxCircle(10, 10, 1)

# array
array = [s1, s2, s3, s4, s5, r1, r2, r3, r4, r5, r6, c1, c2, c3, c4, c5, c6, c7]


def test_quadrangle_validation():
    """
    This method check the quadrangle_validation method
    """
    assert utils.quadrangle_validation(s1) is True
    assert utils.quadrangle_validation(s2) is False
    assert utils.quadrangle_validation(s3) is False
    assert utils.quadrangle_validation(s4) is False
    assert utils.quadrangle_validation(r1) is True
    assert utils.quadrangle_validation(r2) is False
    assert utils.quadrangle_validation(r3) is False
    assert utils.quadrangle_validation(r4) is False


def test_circle_validation():
    """
    This method check the circle_validation method
    """
    assert utils.circle_validation(c1) is True
    assert utils.circle_validation(c2) is False
    assert utils.circle_validation(c3) is False
    assert utils.circle_validation(c4) is False


def test_quadrangles_intersection():
    """
    This method check the quadrangles_intersection method
    """
    assert utils.quadrangles_intersection(s1, s2) is "invalid"
    assert utils.quadrangles_intersection(s2, s3) is "invalid"
    assert utils.quadrangles_intersection(s2, s5) is "invalid"
    assert utils.quadrangles_intersection(r1, r2) is "invalid"
    assert utils.quadrangles_intersection(s1, r1) is "intersect"
    assert utils.quadrangles_intersection(r1, r5) is "separate"
    assert utils.quadrangles_intersection(s5, r5) is "separate"
    assert utils.quadrangles_intersection(s5, r6) is "separate"
    assert utils.quadrangles_intersection(s1, s5) is "separate"
    assert utils.quadrangles_intersection(s1, r5) is "separate"


def test_circles_intersection():
    """
    This method check the circles_intersection method
    """
    assert utils.circles_intersection(c1, c2) is "invalid"
    assert utils.circles_intersection(c2, c3) is "invalid"
    assert utils.circles_intersection(c2, c6) is "invalid"
    assert utils.circles_intersection(c1, c5) is "intersect"
    assert utils.circles_intersection(c1, c6) is "separate"
    assert utils.circles_intersection(c6, c7) is "separate"


def test_others_intersection():
    """
    This method check the others_intersection method
    """
    assert utils.others_intersection(s1, c2) is "invalid"
    assert utils.others_intersection(c3, r1) is "invalid"
    assert utils.others_intersection(c5, r4) is "invalid"
    assert utils.others_intersection(s1, c4) is "invalid"
    assert utils.others_intersection(c1, r4) is "invalid"
    assert utils.others_intersection(s1, c5) is "intersect"
    assert utils.others_intersection(c5, r5) is "intersect"
    assert utils.others_intersection(c1, r1) is "intersect"
    assert utils.others_intersection(s1, c1) is "intersect"
    assert utils.others_intersection(r1, c5) is "intersect"
    assert utils.others_intersection(s1, c7) is "separate"
    assert utils.others_intersection(c1, s5) is "separate"
    assert utils.others_intersection(c6, r6) is "separate"
    assert utils.others_intersection(c6, s1) is "separate"
    assert utils.others_intersection(s1, c7) is "separate"


def test_compare_sort_array():
    """
    This method check the compare_sort_array method
    """
    assert utils.compare_sort_array([s1, s2, s3, s4, r1, r2, c1, c2, c3, c4]) == []
    assert utils.compare_sort_array([s2, s3, s4, r2, r3, r4, c2, c3, c4]) == []
    assert utils.compare_sort_array([s1, s2, s3, s4, s5, r1, r2, c1, c2, c3, c4]) == [s5]
    assert utils.compare_sort_array([s1, s2, s3, s4, s5, r1, r2, c1, c2, c3, c4]) == [s5]
    assert utils.compare_sort_array([s1, s2, s3, s4, s5, r1, r2, r3, r4, r5, r6, c1, c2, c3, c4, c5]) == [s5, r6]
    assert utils.compare_sort_array(array) == [s5, c7, r6, c6]


def test_type_intersection():
    """
    This method check the type_intersection method
    """
    assert utils.type_intersection(s2.type, s2, s3) is "invalid"
    assert utils.type_intersection(s2.type, s2, s5) is "invalid"
    assert utils.type_intersection(r1.type, r1, r2) is "invalid"
    assert utils.type_intersection(s1.type, s1, r1) is "intersect"
    assert utils.type_intersection(s1.type, s1, s5) is "separate"
    assert utils.type_intersection(s1.type, s1, r5) is "separate"
    assert utils.type_intersection(r1.type, r1, r5) is "separate"
    assert utils.type_intersection(c1.type, c1, c2) is "invalid"
    assert utils.type_intersection(c2.type, c2, c3) is "invalid"
    assert utils.type_intersection(c2.type, c2, c6) is "invalid"
    assert utils.type_intersection(c1.type, c1, c5) is "intersect"
    assert utils.type_intersection(c1.type, c1, c6) is "separate"
    assert utils.type_intersection(c6.type, c6, c7) is "separate"
    assert utils.type_intersection(s1.type, s1, c2) is "invalid"
    assert utils.type_intersection(c3.type, c3, r1) is "invalid"
    assert utils.type_intersection(c5.type, c5, r4) is "invalid"
    assert utils.type_intersection(s1.type, s1, c4) is "invalid"
    assert utils.type_intersection(c1.type, c1, r4) is "invalid"
    assert utils.type_intersection(s1.type, s1, c5) is "intersect"
    assert utils.type_intersection(c5.type, c5, r5) is "intersect"
    assert utils.type_intersection(c1.type, c1, r1) is "intersect"
    assert utils.type_intersection(s1.type, s1, c1) is "intersect"
    assert utils.type_intersection(r1.type, r1, c5) is "intersect"
    assert utils.type_intersection(s1.type, s1, c7) is "separate"
    assert utils.type_intersection(c1.type, c1, s5) is "separate"
    assert utils.type_intersection(c6.type, c6, r6) is "separate"
    assert utils.type_intersection(c6.type, c6, s1) is "separate"
    assert utils.type_intersection(s1.type, s1, c7) is "separate"
