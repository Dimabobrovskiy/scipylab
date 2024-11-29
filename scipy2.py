import numpy as np
import matplotlib.pyplot as plt

# Функция для чтения системы уравнений из файла
def read_system_from_file(filename):
    with open(filename, 'r') as f:
        # Читаем размерность системы
        N = int(f.readline().strip())
        
        # Читаем матрицу A
        A = []
        for _ in range(N):
            row = list(map(float, f.readline().strip().split()))
            A.append(row)
        A = np.array(A)
        
        # Читаем вектор b
        b = list(map(float, f.readline().strip().split()))
        b = np.array(b)
        
    return A, b

# Чтение данных из файла
A, b = read_system_from_file(r'C:\Users\dimab\OneDrive\Desktop\large.txt')  # Укажите путь к файлу

# Решение системы линейных уравнений
x = np.linalg.solve(A, b)

# Вывод решения
print("Решение системы x:", x)

# Построение графика
plt.bar(range(len(x)), x)
plt.xlabel('Индекс переменной')
plt.ylabel('Значение')
plt.title('Решение системы линейных уравнений')
plt.show()
