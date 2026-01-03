import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Параметры ДНК
num_points = 500  # количество точек
turns = 3        # количество витков
radius = 1.0     # радиус спирали
rise = 2.4       # подъем на один виток

# Создание фигуры
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Параметр для спирали
t = np.linspace(0, turns * 2 * np.pi, num_points)

# Две цепи ДНК (сдвинутые на 180 градусов)
x1 = radius * np.cos(t)
y1 = radius * np.sin(t)
z1 = rise * t / (2 * np.pi)

x2 = radius * np.cos(t + np.pi)
y2 = radius * np.sin(t + np.pi)
z2 = rise * t / (2 * np.pi)

# Соединяющие "ступеньки" (водородные связи)
connections = []
for i in range(0, len(t), 20):
    connections.append([x1[i], y1[i], z1[i]])
    connections.append([x2[i], y2[i], z2[i]])

connections = np.array(connections)

# Начальная отрисовка
line1, = ax.plot(x1, y1, z1, 'b-', linewidth=2, label='Цепь 1')
line2, = ax.plot(x2, y2, z2, 'r-', linewidth=2, label='Цепь 2')
scatter1 = ax.scatter(x1[::20], y1[::20], z1[::20], color='blue', s=20)
scatter2 = ax.scatter(x2[::20], y2[::20], z2[::20], color='red', s=20)

# Соединения (ступеньки)
if len(connections) > 0:
    connections_line = ax.plot(connections[:, 0], connections[:, 1], connections[:, 2], 
                              'g-', linewidth=1, alpha=0.5)[0]

# Настройка графика
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([0, max(z1)])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Модель ДНК')
ax.legend()
ax.grid(True)

# Функция анимации
def update(frame):
    # Вращение вокруг оси Z
    angle = frame * 2  # скорость вращения
    
    # Матрица вращения
    cos_angle = np.cos(np.radians(angle))
    sin_angle = np.sin(np.radians(angle))
    
    # Вращаем первую цепь
    x1_rot = x1 * cos_angle - y1 * sin_angle
    y1_rot = x1 * sin_angle + y1 * cos_angle
    
    # Вращаем вторую цепь
    x2_rot = x2 * cos_angle - y2 * sin_angle
    y2_rot = x2 * sin_angle + y2 * cos_angle
    
    # Обновляем данные
    line1.set_data(x1_rot, y1_rot)
    line1.set_3d_properties(z1)
    
    line2.set_data(x2_rot, y2_rot)
    line2.set_3d_properties(z2)
    
    # Обновляем точки
    scatter1._offsets3d = (x1_rot[::20], y1_rot[::20], z1[::20])
    scatter2._offsets3d = (x2_rot[::20], y2_rot[::20], z2[::20])
    
    # Обновляем соединения
    if len(connections) > 0:
        # Вращаем соединения
        xc = connections[:, 0] * cos_angle - connections[:, 1] * sin_angle
        yc = connections[:, 0] * sin_angle + connections[:, 1] * cos_angle
        connections_line.set_data(xc, yc)
        connections_line.set_3d_properties(connections[:, 2])
    
    return line1, line2, scatter1, scatter2

# Создание анимации
ani = FuncAnimation(fig, update, frames=360, interval=50, blit=False)

plt.tight_layout()
# Для сохранения анимации (раскомментируйте при необходимости)
ani.save('dna_animation.gif', writer='ffmpeg', fps=30)
plt.show()