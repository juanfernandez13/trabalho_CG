import numpy as np
from lines import midpoint_algorithm
from general import normalizer, scale_for_resolution, plot_points

def curvaHermite(P0, T0, P1, T1, numeroDePontos):
    pontos = []

    for t in np.linspace(0, 1, numeroDePontos):
        H1 = 2 * t ** 3 - 3 * t ** 2 + 1  # P0
        H2 = t ** 3 - 2 * t ** 2 + t  # T0
        H3 = -2 * t ** 3 + 3 * t ** 2  # P1
        H4 = t ** 3 - t ** 2  # T1

        x = H1 * P0[0] + H2 * T0[0] + H3 * P1[0] + H4 * T1[0]
        y = H1 * P0[1] + H2 * T0[1] + H3 * P1[1] + H4 * T1[1]
        x_round = round(x)
        y_round = round(y)
        pontos.append((x_round, y_round))
    return pontos

points = [(100, 100), (40,10), (80, 50)]
tangents = [(20, 20), (-500, 60), (40,80)]
resolution = (100, 100)

te = curvaHermite(points[0], tangents[0], points[1], tangents[1], 3)
te += curvaHermite(points[1], tangents[1], points[2], tangents[2], 3)
xe = normalizer(te)
ce = scale_for_resolution(xe, resolution)
ne = []

for i in range(1,len(ce)):
   ne += midpoint_algorithm(ce[i-1], ce[i])


plot_points(ne, resolution)



