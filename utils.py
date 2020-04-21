

# valid
def square_validation(square):
    return 0 <= square['x1'] < square['x2'] and 0 <= square['y1'] < square['y2']


# valid
def circle_validation(circle):
    return not (circle['x'] < 0 or circle['y'] < 0 or circle['radius'] < 0
                or (circle['x'] - circle['radius']) < 0 or (circle['y'] - circle['radius']) < 0)


def squares_intersection(s1, s2):
    if not (square_validation(s1) and square_validation(s2)):
        return "invalid"
    # determine the coordinates of the intersection
    x_left = max(s1['x1'], s2['x1'])
    y_top = max(s1['y1'], s2['y1'])
    x_right = min(s1['x2'], s2['x2'])
    y_bottom = min(s1['y2'], s2['y2'])
    return "separate" if (x_right < x_left or y_bottom < y_top) else "intersect"


def circles_intersection(c1, c2):
    if not (circle_validation(c1) and circle_validation(c2)):
        return "invalid"
    # determine the coordinates of the intersection
    x_left = max(c1['x'] - c1['radius'], c2['x'] - c2['radius'])
    y_top = max(c1['y'] - c1['radius'], c2['y'] - c2['radius'])
    x_right = min(c1['x'] + c1['radius'], c2['x'] + c2['radius'])
    y_bottom = min(c1['y'] + c1['radius'], c2['y'] + c2['radius'])
    return "separate" if (x_right < x_left or y_bottom < y_top) else "intersect"


def others_intersection(s1, c2):
    if not (square_validation(s1) and circle_validation(c2)):
        return "invalid"
    # determine the coordinates of the intersection
    x_left = max(s1['x1'], c2['x'] - c2['radius'])
    y_top = max(s1['y1'], c2['y'] - c2['radius'])
    x_right = min(s1['x2'], c2['x'] + c2['radius'])
    y_bottom = min(s1['y2'], c2['y'] + c2['radius'])
    return "separate" if (x_right < x_left or y_bottom < y_top) else "intersect"


# square1 = {'type': 'square', 'key': 0, 'x1': 3, 'y1': 3, 'x2': 5, 'y2': 5}
# circle1 = {'type': 'circle', 'key': 1, 'x': 3, 'y': 3, 'radius': 2}
def compare_sort_array(arr):
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
