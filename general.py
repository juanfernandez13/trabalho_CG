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
    x_scale = np.round(((points[:, 0] + 1) / 2) * width).astype(int)
    y_scale = np.round(((points[:, 1] + 1) / 2) * height).astype(int)

    # Criar matriz de pontos escalonados
    scale_points = np.column_stack((x_scale, y_scale))
    return scale_points

    return scale_points

def plot_points(points, resolution):
    width, height = resolution
    img = np.ones((height + 1, width + 1 ))

    for i in points:
        img[i[1]][i[0]] = 0

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(img, cmap='gray', origin='lower', vmin=0, vmax=1)
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    plt.grid()
    plt.show()