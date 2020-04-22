# stratasysProject

In this project, we generate random shapes and check if they separate.

The objects look like:

Square = {'type': 'square', 'x1': 3, 'y1': 3, 'x2': 5, 'y2': 5},

Rectangle = {'type': 'rectangle', 'x1': 3, 'y1': 2, 'x2': 5, 'y2': 5},

Circle = {'type': 'circle', 'x': 3, 'y': 3, 'radius': 2}.

I choose to sort the array by the object area order by ascending from smallest to largest with the complexity of O(n*log(n)) 
and the comparison will be O(n^2) because we need to compare between all the objects.

Run tests: you need to open project at the terminal->pytest test

At example.py you can change the params and check the project
