import numpy as np
import matplotlib.pyplot as plt

def normalizer(points):
    min_val, max_val = np.min(points), np.max(points)
    if min_val == max_val:
        return points - min_val
    # garantir que os pontos variem de -1 até 1
    normalized_points = ((2 * (points - min_val)) / (max_val - min_val)) - 1
    return normalized_points


def scale_for_resolution(points, resolution):
    width, height = resolution

    # Escalonar para a resolução
    x_scale = ((points[:, 0] + 1) / 2) * width
    y_scale = ((points[:, 1] + 1) / 2) * height

    # Criar matriz de pontos escalonados
    scale_points = np.column_stack((x_scale, y_scale))
    return scale_points

    return scale_points

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

def round_points(points):
    points_round = []
    for i in points:
        print(i)
        x, y = round(i[0]), round(i[1])
        points_round.append([x, y])
    return points_round

def plot_points(points, resolution):
    width, height = resolution
    img = np.ones((height + 15, width + 15))

    for i in points:
        img[i[1]][i[0]] = 0

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(img, cmap='gray', origin='lower', vmin=0, vmax=1)
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    plt.grid()
    plt.show()

points = [(100, 100), (40,10), (80, 50)]
tangents = [(20, 20), (-500, 60), (40,80)]
resolution = (100, 100)

te = curvaHermite(points[0], tangents[0], points[1], tangents[1], 3)
te += curvaHermite(points[1], tangents[1], points[2], tangents[2], 3)
xe = normalizer(te)
ce = scale_for_resolution(xe, resolution)
fe = round_points(ce)
print(fe)
ne = []

for i in range(1,len(fe)):
    ne += midpoint_algorithm(fe[i-1], fe[i])


plot_points(ne, resolution)



