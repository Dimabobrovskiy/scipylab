import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Символьное решение с SymPy
x = sp.symbols('x')
y = sp.Function('y')
ode = sp.Eq(y(x).diff(x), -2 * y(x))  # дифференциальное уравнение dy/dx = -2y
initial_condition = {y(0): sp.sqrt(2)}  # начальное условие y(0) = sqrt(2)

# Решаем символически
sym_solution = sp.dsolve(ode, y(x), ics=initial_condition)
sym_solution_func = sp.lambdify(x, sym_solution.rhs, 'numpy')  # конвертируем решение в функцию для numpy

# Численное решение с SciPy
def model(t, y):
    return -2 * y

y0 = [np.sqrt(2)]
t_span = [0, 10]
t_eval = np.linspace(0, 10, 100)  # точность графика
numerical_solution = solve_ivp(model, t_span, y0, t_eval=t_eval)

# Построение графиков
t_values = t_eval
sym_values = sym_solution_func(t_values)
num_values = numerical_solution.y[0]

# График 1: Символьное и численное решение
plt.figure(figsize=(10, 5))
plt.plot(t_values, sym_values, label="SymPy Solution", color="blue")
plt.plot(t_values, num_values, label="SciPy Solution", color="orange", linestyle="dashed")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.legend()
plt.title("Символьное и численное решения дифференциального уравнения")
plt.grid()

# График 2: Разность решений
plt.figure(figsize=(10, 5))
plt.plot(t_values, sym_values - num_values, label="Difference (SymPy - SciPy)", color="green")
plt.xlabel("x")
plt.ylabel("Difference")
plt.legend()
plt.title("Разность между символьным и численным решениями")
plt.grid()

plt.show()

# Вывод символического решения
print("Символьное решение, найденное SymPy:", sym_solution)
