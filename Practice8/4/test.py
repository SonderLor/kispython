import numpy as np
import matplotlib.pyplot as plt

# Предположим, что у нас есть функция передачи H(f)
# В данном примере используется просто случайная функция
def transfer_function(f):
    return 1 / (1 + 0.1j*f)

# Создаем массив частот от 0 до 1000 Гц
frequencies = np.linspace(0, 1000, 1000)

# Вычисляем значения функции передачи для каждой частоты
response = transfer_function(frequencies)

# Рисуем график частотной характеристики
plt.figure(figsize=(10, 6))
plt.plot(frequencies, 20 * np.log10(np.abs(response)))
plt.xscale('log')
plt.title('Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.show()
