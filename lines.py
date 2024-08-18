import numpy as np
import matplotlib.pyplot as plt
from general import normalizer, scale_for_resolution, plot_points
def midpoint_algorithm(p1, p2):
    if p1[0] > p2[0] or p1[1] > p2[1]:
        p1, p2 = p2, p1

    dx, dy = p1[0] - p2[0], p1[1] - p2[1]

    m = None if dx == 0 else dy / dx
    b = None if m is None else p1[1] - m * p1[0]

    points = []
    x1, y1 = p1
    x2, y2 = p2

    if (abs(dx) >= abs(dy)):
        if x1 > x2:
            x1, x2 = x2, x1
        while x1 <= x2:
            y = m * x1 + b if m is not None else y1
            points.append((round(x1), round(y)))
            x1 += 1
    else:
        if y1 > y2:
            y1, y2 = y2, y1
        while y1 <= y2:
            x = (y1 - b) / m if m is not None else x1
            points.append((round(x), round(y1)))
            y1 += 1

    return points

points = [(1,1), (1,10)]
resolution = (100,100)
normaliz = normalizer(points)
scale = scale_for_resolution(normaliz, resolution)
mid = midpoint_algorithm(scale[0], scale[1])
#plot_points(mid, resolution)

