import numpy as np
import matplotlib.pyplot as plt
from lines import midpoint_algorithm
from general import normalizer, scale_for_resolution, plot_points


def scanline(points, resolution):
    width, height = resolution
    npArr = np.array(points)
    npArr = np.unique(npArr, axis=0)

    intersections = []
    for y in range(0, height):
        addPoint = 0
        lenPointsLine = len(npArr[npArr[:, 1] == y]) % 2
        for x in range(0, width):
            if addPoint == 1:
                intersections.append((x,y))

            if (x,y) in points and (x+1,y) not in points and lenPointsLine == 0:
                addPoint = 1 if addPoint == 0 else 0
    return intersections


#points = [(0, 4), (4, 4), (4,0), (0,0), (0, 4)]

points = [(0,0), (1,2), (2,0)]
#points = [(0, 0),  (0,8), (8, 8), (8,0)]
#points = [[-0.5, 0], [-0.25, -0.433], [0.25, -0.433], [0.5, 0], [0.25, 0.433], [-0.25, 0.433]]
resolution = (1920, 1080)

normalized_points = normalizer(points)
scaled_points = scale_for_resolution(normalized_points, resolution)

rasteirezed_points = []
for i in range(1,len(scaled_points)+1):
    if(i != len(scaled_points)):
        rasteirezed_points += midpoint_algorithm(scaled_points[i-1], scaled_points[i])
    else:
        rasteirezed_points += midpoint_algorithm(scaled_points[i-1], scaled_points[0])
rasteirezed_points += scanline(rasteirezed_points, resolution)
plot_points((rasteirezed_points), resolution)
