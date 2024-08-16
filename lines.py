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

def plot_points(points, resolution):
    width, height = resolution
    img = np.ones((height + 1, width + 1))
    for i in points:
        img[i[1]][i[0]] = 0

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(img, cmap='gray', origin='lower', vmin=0, vmax=1)
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    plt.grid()
    plt.show()


points = [(2, 1), (8, 8), (4,4), (5,8)]
resolution = (100, 100)

normalized_points = normalizer(points)
scaled_points = scale_for_resolution(normalized_points, resolution)
rasteirezed_points = midpoint_algorithm(scaled_points[0], scaled_points[1])
plot_points(rasteirezed_points, resolution)
