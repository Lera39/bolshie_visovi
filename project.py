import numpy as np
import matplotlib.pyplot as plt

# 1. Создаем звук (синусоида 440 Гц на 1 секунду)
sample_rate = 44100  # частота дискретизации
t = np.linspace(0, 1, sample_rate)  # ось времени
frequency = 440  # частота в Герцах (нота Ля)

# Создаем синусоидальный сигнал
sound = np.sin(2 * np.pi * frequency * t)

# 2. Рисуем график (первые 0.02 секунды для наглядности)
plt.figure(figsize=(10, 4))
plt.plot(t[:882], sound[:882])  # 882 отсчета = 0.02 секунды
plt.title(f'Звуковая волна: синус {frequency} Гц')
plt.xlabel('Время (секунды)')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.savefig("fig1.png")
plt.show()