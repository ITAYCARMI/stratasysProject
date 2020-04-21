
def square_validation(square):
    """
    Check if square points is valid
    :param square: square object
    :return: true if valid else false
    """
    return 0 <= square['x1'] < square['x2'] and 0 <= square['y1'] < square['y2']


def circle_validation(circle):
    """
    Check if square circle is valid
    :param circle: circle object
    :return: true if valid else false
    """
    return not (circle['x'] < 0 or circle['y'] < 0 or circle['radius'] < 0
                or (circle['x'] - circle['radius']) < 0 or (circle['y'] - circle['radius']) < 0)


def squares_intersection(s1, s2):
    """
    Check intersection between two squares
    :param s1: first square object
    :param s2: second square object
    :return: "invalid" if one of the squares is invalid
             "separate"  if squares are separate
             "intersect" if squares are intersect
    """
    if not (square_validation(s1) and square_validation(s2)):
        return "invalid"
    # determine the coordinates of the intersection
    x_left = max(s1['x1'], s2['x1'])
    y_top = max(s1['y1'], s2['y1'])
    x_right = min(s1['x2'], s2['x2'])
    y_bottom = min(s1['y2'], s2['y2'])
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
    x_left = max(c1['x'] - c1['radius'], c2['x'] - c2['radius'])
    y_top = max(c1['y'] - c1['radius'], c2['y'] - c2['radius'])
    x_right = min(c1['x'] + c1['radius'], c2['x'] + c2['radius'])
    y_bottom = min(c1['y'] + c1['radius'], c2['y'] + c2['radius'])
    return "separate" if (x_right < x_left or y_bottom < y_top) else "intersect"


def others_intersection(s1, c2):
    """
    Check intersection between square and circle
    :param s1: square object
    :param c2: circle object
    :return: "invalid" if one of them is invalid
             "separate"  if they are separate
             "intersect" if they are intersect
    """
    if not (square_validation(s1) and circle_validation(c2)):
        return "invalid"
    # determine the coordinates of the intersection
    x_left = max(s1['x1'], c2['x'] - c2['radius'])
    y_top = max(s1['y1'], c2['y'] - c2['radius'])
    x_right = min(s1['x2'], c2['x'] + c2['radius'])
    y_bottom = min(s1['y2'], c2['y'] + c2['radius'])
    return "separate" if (x_right < x_left or y_bottom < y_top) else "intersect"


def compare_sort_array(arr):
    """
    This method find separate objects from a given array and return array of separate object sorted by key
    :param arr: given objects array
    :return: array of separate object sorted by key
    """
    sorted_array = []
    intersected_array = []
    for i in range(0, len(arr)):
        if arr[i] in intersected_array:
            continue
        type_i = arr[i]['type']
        if type_i == 'square' and not square_validation(arr[i]):
            continue
        elif type_i == 'circle' and not circle_validation(arr[i]):
            continue
        j = i + 1
        while j < len(arr):
            if type_intersection(type_i, arr[i], arr[j]) == "intersect":
                intersected_array.append(arr[i])
                intersected_array.append(arr[j])
            j += 1
        if not arr[i] in intersected_array:
            sorted_array.append(arr[i])
    return sorted_array


def type_intersection(type_obj1, obj1, obj2):
    """
    This method examines the type of objects and refers to the appropriate intersection method
    :param type_obj1: type of compared object
    :param obj1: compared object
    :param obj2: second object
    :return: "invalid" if one of them is invalid
             "separate"  if they are separate
             "intersect" if they are intersect
    """
    if type_obj1 == 'square' and obj2['type'] == 'square':
        ans = squares_intersection(obj1, obj2)
    elif type_obj1 == 'circle' and obj2['type'] == 'circle':
        ans = circles_intersection(obj1, obj2)
    else:
        if type_obj1 == 'circle':
            ans = others_intersection(obj2, obj1)
        else:
            ans = others_intersection(obj1, obj2)
    return ans
