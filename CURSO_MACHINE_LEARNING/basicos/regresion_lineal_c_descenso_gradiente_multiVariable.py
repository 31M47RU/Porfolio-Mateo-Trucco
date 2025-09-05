import numpy as np
import matplotlib.pyplot as plt

# ---- Generar datos ----
np.random.seed(42)  # reproducibilidad
x = np.linspace(0, 50, 1000)
y =  3 * x + 7 + np.random.randn(1000) * 50  # línea + ruido

# ---- Funciones ----
def cost_function(x, y, w, b):
    m = x.shape[0]
    cost = 0.0
    for i in range(m):
        f_J = w * x[i] + b
        cost += (f_J - y[i])**2
    return cost / (2.0 * m)

def gradient_descend(x, y, w, b, a):
    m = x.shape[0]
    dJ_dw = 0.0
    dJ_db = 0.0
    
    for i in range(m):
        f_wb = w * x[i] + b
        dJ_dw += (f_wb - y[i]) * x[i]
        dJ_db += (f_wb - y[i])
        
    dj_dw = dJ_dw / m
    dj_db = dJ_db / m

    w -= a * dj_dw
    b -= a * dj_db
    
    return w, b

def predict(x_new, w, b):
    return w * x_new + b

# ---- Entrenamiento ----
w = 0.0
b = 0.0
a = 0.001
epochs = 5000

for epoch in range(epochs):
    w, b = gradient_descend(x, y, w, b, a)
    if epoch % 200 == 0:
        print(f"Epoch {epoch}: Cost = {cost_function(x, y, w, b):.4f}, w = {w:.4f}, b = {b:.4f}")

print("\nFinal:")
print(f"w = {w}, b = {b}")
print(f"Final cost = {cost_function(x, y, w, b)}")

# # ---- Graficar ----
# y_pred = w * x + b
# plt.scatter(x, y, s=10, color='blue', label='Datos')
# plt.plot(x, y_pred, color='red', label='Recta ajustada')

# # ---- Probar predicciones visualmente con anotaciones ----
# x_test_list = [5]
# for x_val in x_test_list:
#     y_val = predict(x_val, w, b)
#     plt.scatter(x_val, y_val, color='green', s=50, marker='X')
#     plt.annotate(f'{y_val:.2f}', (x_val, y_val),
#                  textcoords="offset points", xytext=(0,10), ha='center', color='green')

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Regresión Lineal con 1000 puntos y predicciones')
# plt.legend()
# plt.show()
