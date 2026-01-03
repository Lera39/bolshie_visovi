import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Создаем тестовый звук
print('Введите частоту дискретизации')
fs = int(input())

print('Введите время')
tm = int(input())
t = np.linspace(0, tm, tm * fs)

print('Введите частоту звука в Герцах')
freq = int(input())
# Создаем звуковую волну
sound = np.sin(2 * np.pi * freq * t)

# 2. Создаем фигуру для анимации
fig, ax = plt.subplots(figsize=(10, 4))

# Сколько секунд показывать в одном кадре
window_seconds = 0.05
# Сколько точек в одном кадре
window_points = int(window_seconds * fs)

# Создаем линию для графика
x = np.linspace(0, window_seconds, window_points)
line, = ax.plot(x, sound[:window_points], 'b-', linewidth=2)

# Настраиваем график
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Время (секунды)')
ax.set_ylabel('Амплитуда')
ax.grid(True)
ax.set_title('Анимация звуковой волны')

# 3. Функция для обновления каждого кадра
def update(frame_num):
    # Сдвигаем окно
    start = (frame_num * 10) % (len(sound) - window_points)
    end = start + window_points
    
    # Обновляем данные линии
    line.set_ydata(sound[start:end])
    
    # Обновляем заголовок
    ax.set_title(f'Звуковая волна {freq} Гц)')
    
    return line,

# 4. Создаем анимацию
print("Создаю GIF...")
anim = FuncAnimation(fig, update, frames=100, interval=50)

# 5. Сохраняем как GIF
anim.save('sound_wave.gif', writer='pillow', fps=20)
plt.show()