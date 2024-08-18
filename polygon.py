import numpy as np
import matplotlib.pyplot as plt
from lines import midpoint_algorithm
from general import normalizer, scale_for_resolution, plot_points

from matplotlib.path import Path

def scanline(points):
    npArr = np.array(points)
    npArr = np.unique(npArr, axis=0)
    maxHeight = np.max(npArr[:,1])
    minHeight = np.min(npArr[:,1])
    maxWidth = np.max(npArr[:,0])
    minWidth = np.min(npArr[:,0])

    intersections = []
    for y in range(minHeight, maxHeight):
        addPoint = 0
        lenPointsLine = len(npArr[npArr[:, 1] == y]) >= 2
        for x in range(minWidth, maxWidth):
            if addPoint == 1:
                intersections.append((x,y))

            if (x,y) in points and (x+1,y) not in points and lenPointsLine == 1:
                addPoint = 1 if addPoint == 0 else 0
    return intersections


def scan2(points):
    npArr = np.array(points)
    npArr = np.unique(npArr, axis=0)

    path = Path(npArr)

    x, y = np.meshgrid(np.arange(np.max(npArr[:, 0])), np.arange(np.max(npArr[:, 1])))
    pointsT = np.vstack((x.ravel(), y.ravel())).T
    grid = path.contains_points(pointsT).astype(int)
    t = pointsT[grid]
    print(grid)
    return t

points = [(0,0), (1,2), (2,0)]
#points = [(0, 0),  (0,8), (8, 8), (8,0)]
#points =  [(0.866, 0.5), (0.866, -0.5), (0, -1), (-0.866, -0.5), (-0.866, 0.5), (0, 1) ]

#points = [[-0.5, 0], [-0.25, -0.433], [0.25, -0.433], [0.5, 0], [0.25, 0.433], [-0.25, 0.433]]
resolution = (10, 10)

normalized_points = normalizer(points)
scaled_points = scale_for_resolution(normalized_points, resolution)

rasteirezed_points = []
for i in range(1,len(scaled_points)+1):
    if(i != len(scaled_points)):
        rasteirezed_points += midpoint_algorithm(scaled_points[i-1], scaled_points[i])
    else:
        rasteirezed_points += midpoint_algorithm(scaled_points[i-1], scaled_points[0])
rasteirezed_points += scan2(rasteirezed_points)
plot_points((rasteirezed_points), resolution)