import object_generator


def quadrangle_validation(quadrangle):
    """
    Check if quadrangle points is valid
    :param quadrangle: square object
    :return: true if valid else false
    """
    return 0 <= quadrangle.x1 < quadrangle.x2 and 0 <= quadrangle.y1 < quadrangle.y2


def circle_validation(circle):
    """
    Check if circle is valid
    :param circle: circle object
    :return: true if valid else false
    """
    return not (circle.x < 0 or circle.y < 0 or circle.radius < 0
                or (circle.x - circle.radius) < 0 or (circle.y - circle.radius) < 0)


def quadrangles_intersection(q1, q2):
    """
    Check intersection between two quadrangles
    :param q1: first quadrangle object
    :param q2: second quadrangle object
    :return: "invalid" if one of the quadrangles is invalid
             "separate"  if quadrangles are separate
             "intersect" if quadrangles are intersect
    """
    if not (quadrangle_validation(q1) and quadrangle_validation(q2)):
        return "invalid"
    # determine the coordinates of the intersection
    x_left = max(q1.x1, q2.x1)
    y_top = max(q1.y1, q2.y1)
    x_right = min(q1.x2, q2.x2)
    y_bottom = min(q1.y2, q2.y2)
    return "separate" if (x_right < x_left or y_bottom < y_top) else "intersect"


def circles_intersection(c1, c2):
    """
    Check intersection between two circles
    :param c1: first circle object
    :param c2: second circle object
    :return: "invalid" if one of the circles is invalid
             "separate"  if circles are separate
             "intersect" if circles are intersect
    """
    if not (circle_validation(c1) and circle_validation(c2)):
        return "invalid"
    # determine the coordinates of the intersection
    x_left = max(c1.x - c1.radius, c2.x - c2.radius)
    y_top = max(c1.y - c1.radius, c2.y - c2.radius)
    x_right = min(c1.x + c1.radius, c2.x + c2.radius)
    y_bottom = min(c1.y + c1.radius, c2.y + c2.radius)
    return "separate" if (x_right < x_left or y_bottom < y_top) else "intersect"


def others_intersection(q1, c2):
    """
    Check intersection between quadrangle and circle
    :param q1: quadrangle object
    :param c2: circle object
    :return: "invalid" if one of them is invalid
             "separate"  if they are separate
             "intersect" if they are intersect
    """
    if type(q1) is object_generator.BoundingBoxCircle:
        temp = c2
        c2 = q1
        q1 = temp
    if not (quadrangle_validation(q1) and circle_validation(c2)):
        return "invalid"
    # determine the coordinates of the intersection
    x_left = max(q1.x1, c2.x - c2.radius)
    y_top = max(q1.y1, c2.y - c2.radius)
    x_right = min(q1.x2, c2.x + c2.radius)
    y_bottom = min(q1.y2, c2.y + c2.radius)
    return "separate" if (x_right < x_left or y_bottom < y_top) else "intersect"


def compare_sort_array(arr):
    """
    This method find separate objects from a given array and return array of separate object sorted by key
    :param arr: given objects array
    :return: array of separate object sorted by key
    """
    sorted_array = []
    intersected_array = set()
    for i in range(0, len(arr)):
        type_i = type(arr[i])
        if (type_i is object_generator.BoundingBoxSquare or type_i is object_generator.BoundingBoxRectangle) \
                and not quadrangle_validation(arr[i]):
            continue
        elif type_i is object_generator.BoundingBoxCircle and not circle_validation(arr[i]):
            continue
        j = i + 1
        while j < len(arr):
            if type_intersection(arr[i], arr[j]) == "intersect":
                intersected_array.add(arr[i])
                intersected_array.add(arr[j])
            j += 1
        if arr[i] not in intersected_array:
            sorted_array.append(arr[i])
    return sorted(sorted_array, key=lambda obj: obj.area())


def type_intersection(obj1, obj2):
    """
    This method examines the type of objects and refers to the appropriate intersection method
    :param obj1: compared object
    :param obj2: second object
    :return: "invalid" if one of them is invalid
             "separate"  if they are separate
             "intersect" if they are intersect
    """
    if (type(obj1) is object_generator.BoundingBoxSquare or type(obj1) is object_generator.BoundingBoxRectangle) \
            and (type(obj2) is object_generator.BoundingBoxSquare
                 or type(obj2) is object_generator.BoundingBoxRectangle):
        ans = quadrangles_intersection(obj1, obj2)
    elif type(obj1) is object_generator.BoundingBoxCircle and type(obj2) is object_generator.BoundingBoxCircle:
        ans = circles_intersection(obj1, obj2)
    else:
        ans = others_intersection(obj1, obj2)
    return ans
