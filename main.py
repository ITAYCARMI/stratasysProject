import utils
import object_generator

# objects look like
# square1 = {'type': 'square', 'key': 0, 'x1': 3, 'y1': 3, 'x2': 5, 'y2': 5}
# circle1 = {'type': 'circle', 'key': 1, 'x': 3, 'y': 3, 'radius': 2}

# array = []
# square1 = {'type': 'square', 'x1': 3, 'y1': 3, 'x2': 5, 'y2': 5}
# square2 = {'type': 'square', 'x1': 4, 'y1': 4, 'x2': 7, 'y2': 7}
# circle1 = {'type': 'circle', 'x': 3, 'y': 3, 'radius': 2}
# circle2 = {'type': 'circle', 'x': 20, 'y': 20, 'radius': 2}
# array.append(square1)
# array.append(square2)
# array.append(circle1)
# array.append(circle2)
# print(utils.squares_intersection(square1, square2))
# print(utils.circles_intersection(circle1, circle2))
# print(utils.others_intersection(square1, circle1))
# print(utils.others_intersection(square1, circle2))
# print(utils.others_intersection(square2, circle1))
# print(utils.compare_sort_array(array))


array = object_generator.generate_array(10, 50)
print(array)
print(utils.compare_sort_array(array))
