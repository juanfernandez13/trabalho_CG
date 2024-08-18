import numpy as np
def curvaHermite(P0, T0, P1, T1, num_points):
    points = []

    for t in np.linspace(0, 1, num_points):
        H1 = 2 * t ** 3 - 3 * t ** 2 + 1  # P0
        H2 = t ** 3 - 2 * t ** 2 + t  # T0
        H3 = -2 * t ** 3 + 3 * t ** 2  # P1
        H4 = t ** 3 - t ** 2  # T1

        x = H1 * P0[0] + H2 * T0[0] + H3 * P1[0] + H4 * T1[0]
        y = H1 * P0[1] + H2 * T0[1] + H3 * P1[1] + H4 * T1[1]

        points.append((x, y))
    return points
