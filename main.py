import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define os vértices de um tesseract (4D hipercubo)
vertices = np.array([[1, 1, 1, 1],
                     [1, 1, 1, -1],
                     [1, 1, -1, 1],
                     [1, 1, -1, -1],
                     [1, -1, 1, 1],
                     [1, -1, 1, -1],
                     [1, -1, -1, 1],
                     [1, -1, -1, -1],
                     [-1, 1, 1, 1],
                     [-1, 1, 1, -1],
                     [-1, 1, -1, 1],
                     [-1, 1, -1, -1],
                     [-1, -1, 1, 1],
                     [-1, -1, 1, -1],
                     [-1, -1, -1, 1],
                     [-1, -1, -1, -1]])

# Define as arestas do tesseract
edges = [
    (0, 1), (0, 2), (0, 4), (0, 8),
    (1, 3), (1, 5), (1, 9),
    (2, 3), (2, 6), (2, 10),
    (3, 7), (3, 11),
    (4, 5), (4, 6), (4, 12),
    (5, 7), (5, 13),
    (6, 7), (6, 14),
    (7, 15),
    (8, 9), (8, 10), (8, 12),
    (9, 11), (9, 13),
    (10, 11), (10, 14),
    (11, 15),
    (12, 13), (12, 14),
    (13, 15),
    (14, 15)
]

# Projeção 4D para 3D (Simulação Interna)
def project_4d_to_3d(vertices, angle):
    # Rotação nos planos XY, XZ, YW e ZW
    rotation_xy = np.array([
        [np.cos(angle), -np.sin(angle), 0, 0],
        [np.sin(angle), np.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    rotation_xz = np.array([
        [np.cos(angle), 0, -np.sin(angle), 0],
        [0, 1, 0, 0],
        [np.sin(angle), 0, np.cos(angle), 0],
        [0, 0, 0, 1]
    ])

    rotation_yw = np.array([
        [1, 0, 0, 0],
        [0, np.cos(angle), 0, -np.sin(angle)],
        [0, 0, 1, 0],
        [0, np.sin(angle), 0, np.cos(angle)]
    ])

    rotation_zw = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, np.cos(angle), -np.sin(angle)],
        [0, 0, np.sin(angle), np.cos(angle)]
    ])

    # Aplicar rotações
    rotated_vertices = vertices @ rotation_xy @ rotation_xz @ rotation_yw @ rotation_zw

    # Projeção em 3D
    projection_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ])
    projected_vertices = rotated_vertices @ projection_matrix.T

    return projected_vertices

# Função para plotar o tesseract em 3D
def plot_tesseract(vertices_3d, edges, ax):
    ax.clear()  # Limpa o gráfico anterior
    for edge in edges:
        start = vertices_3d[edge[0]]
        end = vertices_3d[edge[1]]
        ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], color='b')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Tesseract Internal View')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    plt.draw()

# Configuração da plotagem
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

angle = 0
try:
    while True:
        vertices_3d = project_4d_to_3d(vertices, angle)
        plot_tesseract(vertices_3d, edges, ax)
        plt.pause(0.1)
        angle += 0.1
except KeyboardInterrupt:
    plt.close()

