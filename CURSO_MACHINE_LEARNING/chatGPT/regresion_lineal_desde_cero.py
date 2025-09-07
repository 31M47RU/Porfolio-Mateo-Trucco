# -*- coding: utf-8 -*-
# Archivo espejo del notebook: 'regresion_lineal_desde_cero.ipynb'
# Contiene todo el código con explicaciones en comentarios/docstrings.

"""
# Regresión lineal **desde cero** con `numpy` y `matplotlib`

**Objetivo:** construir paso a paso modelos de regresión lineal sin usar librerías de alto nivel (nada de scikit-learn), entendiendo:

- Generación de datos sintéticos
- Función de coste MSE (Error Cuadrático Medio)
- Gradientes y Descenso de Gradiente (batch, mini-batch, estocástico)
- Vectorización con `numpy` y por qué acelera el código
- División train/valid y estandarización (feature scaling)
- Regresión lineal **multivariable** (con término de sesgo/bias)
- **Ecuación normal** (solución cerrada) y `np.linalg.pinv`
- **Regularización L2 (Ridge)** desde cero
- Métricas: MSE, MAE, RMSE, R²
- Curvas de pérdida y visualización con `matplotlib`

> Todo viene hiper comentado. Podés correr las celdas una por una y jugar con los hiperparámetros.

"""

"""
## 0) ¿Qué hacen `numpy` y `matplotlib` en este cuaderno?

- **`numpy`**: librería para computación numérica rápida. Ideas clave que vamos a usar:
  - `np.array([...])`: crea arreglos (vectores/matrices) eficientes.
  - **Broadcasting**: `numpy` puede extender dimensiones automáticamente para hacer operaciones elemento a elemento sin bucles explícitos.
  - `np.mean`, `np.sum`, `np.std`: estadísticas básicas eficientes.
  - `np.dot(A, B)` o `A @ B`: producto matricial/vectores.
  - `np.random`: generador de números aleatorios (por ej. ruido para simular datos reales).
  - `np.c_`/`np.hstack`: concatenar columnas (útil para agregar la columna de 1s del **bias**).
  - `np.linalg.pinv`: pseudoinversa (solución estable para la ecuación normal).

- **`matplotlib`**: librería para graficar.
  - `plt.scatter(x, y)`: puntos.
  - `plt.plot(x, y)`: líneas.
  - `plt.figure()`, `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.legend()`: composición de la figura.

> Consejo: corré cada celda y mirá salidas/errores. Cambiá parámetros y volvé a ejecutar.

"""

# Librerías base
import numpy as np
import matplotlib.pyplot as plt

# Hacer reproducibles los resultados
np.random.seed(42)


"""
## 1) Generemos un dataset sintético
Creamos una relación aproximadamente lineal con ruido. Así imitamos datos del mundo real.

**Parámetros a jugar:**
- `n`: cantidad de muestras
- `true_w`, `true_b`: parámetros "reales" de la relación
- `noise_std`: cuánta dispersión/ruido tienen los datos

"""

# Parámetros del dataset
n = 200
true_w = 2.5   # pendiente real
true_b = -1.0  # bias/intersección real
noise_std = 1.5

# Generamos X como 1 variable (x1) entre -3 y 3
X = np.linspace(-3, 3, n).reshape(-1, 1)  # shape (n, 1)
# y = w*x + b + ruido
y = true_w * X[:, 0] + true_b + np.random.normal(loc=0.0, scale=noise_std, size=n)  # vector shape (n,)

# Visualicemos
plt.figure()
plt.scatter(X[:,0], y, label="Datos (x, y)")
plt.title("Datos sintéticos con ruido")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


"""
## 2) Split: train / valid y (opcional) test
Separar datos para entrenar y evaluar generalización. Acá hacemos un split simple 80/20.

"""

# Índices y shuffle
idx = np.arange(n)
np.random.shuffle(idx)

train_frac = 0.8
n_train = int(n * train_frac)

train_idx = idx[:n_train]
valid_idx = idx[n_train:]

X_train, y_train = X[train_idx], y[train_idx]
X_valid, y_valid = X[valid_idx], y[valid_idx]

X_train.shape, X_valid.shape, y_train.shape, y_valid.shape


"""
## 3) Escalado de características (estandarización)

El descenso de gradiente suele converger mejor si las features están en una escala comparable.
Estandarizamos cada columna: `X_std = (X - mean) / std`.
Guardamos `mean` y `std` del **train** y los reutilizamos en valid/test.

"""

def standardize_fit(X):
    """Calcula media y std por columna y devuelve (X_std, mean, std)."""
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0) + 1e-8  # evitamos división por 0
    X_std = (X - mean) / std
    return X_std, mean, std

def standardize_apply(X, mean, std):
    return (X - mean) / std

X_train_std, mean_, std_ = standardize_fit(X_train)
X_valid_std = standardize_apply(X_valid, mean_, std_)

X_train_std[:3], mean_, std_


"""
## 4) Agregar el **bias** como columna de 1s

Para trabajar de forma vectorizada, armamos la matriz de diseño `Φ` (phi):

```
Φ = [1, x1]
```

Así los parámetros se agrupan en `w = [b, w1]` y la predicción es `y_hat = Φ @ w`.

"""

def add_bias(X):
    """Agrega una columna de 1s al frente."""
    return np.c_[np.ones((X.shape[0], 1)), X]

Phi_train = add_bias(X_train_std)
Phi_valid = add_bias(X_valid_std)

Phi_train.shape, Phi_valid.shape


"""
## 5) Métricas + Coste (MSE) y otras

- **MSE**: `mean((y - y_hat)^2)` — lo usamos también como función de coste.
- **MAE**: `mean(|y - y_hat|)`.
- **RMSE**: `sqrt(MSE)` (en mismas unidades que y).
- **R²**: 1 - SSE/SST (cuánto explica el modelo, 1 es perfecto, 0 es baseline de la media).

"""

def predict(Phi, w):
    return Phi @ w  # producto matricial

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def mae(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def rmse(y_true, y_pred):
    return np.sqrt(mse(y_true, y_pred))

def r2_score(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - ss_res / (ss_tot + 1e-12)


"""
## 6) Gradientes (vectorizado)

Para MSE y predicción `y_hat = Φ @ w`:

- Error: `e = y_hat - y`
- Gradiente sin regularización: `∇w = (2/n) * Φᵀ @ e`

Con **L2 (Ridge)** con λ:
- Coste: `J = MSE + λ * ||w_no_bias||²`
- Gradiente: `∇w = (2/n) * Φᵀ @ e + 2λ * w_no_bias` (sin penalizar el bias `w[0]`).

"""

def compute_gradients(Phi, y, w, l2=0.0):
    n = Phi.shape[0]
    y_hat = predict(Phi, w)
    e = y_hat - y
    grad = (2.0 / n) * (Phi.T @ e)
    if l2 > 0.0:
        reg = 2.0 * l2 * w
        reg[0] = 0.0  # no regularizamos el bias
        grad = grad + reg
    return grad, y_hat


"""
## 7) Descenso de Gradiente (batch / mini-batch / estocástico)
Parámetros:
- `lr` (learning rate): tamaño del paso
- `epochs`: cuántas pasadas sobre el dataset
- `batch_size`: si `None` o `n`, es **batch**; si `1`, **estocástico**; intermedio: **mini-batch**
- `l2`: regularización Ridge

"""

def gradient_descent(Phi, y, lr=0.1, epochs=200, batch_size=None, l2=0.0, shuffle=True, verbose=False):
    n, d = Phi.shape
    if batch_size is None:
        batch_size = n  # batch completo
    
    # Inicializamos pesos a 0
    w = np.zeros(d)
    history = {"epoch": [], "train_mse": []}
    
    for epoch in range(1, epochs+1):
        indices = np.arange(n)
        if shuffle:
            np.random.shuffle(indices)
        
        # iterar en minibatches
        for start in range(0, n, batch_size):
            end = start + batch_size
            batch_idx = indices[start:end]
            Phi_b = Phi[batch_idx]
            y_b = y[batch_idx]
            
            grad, y_hat_b = compute_gradients(Phi_b, y_b, w, l2=l2)
            w = w - lr * grad
        
        # Log de entrenamiento (en batch completo calculamos mse sobre todo train)
        y_hat = predict(Phi, w)
        train_mse = mse(y, y_hat)
        history["epoch"].append(epoch)
        history["train_mse"].append(train_mse)
        
        if verbose and (epoch % max(1, epochs//10) == 0):
            print(f"Epoch {epoch:4d} | MSE: {train_mse:.4f}")
    
    return w, history


"""
## 8) Entrenemos y miremos curvas
Probamos batch GD con distintos `lr`. También graficamos el ajuste final en 1D.

"""

# Entrenamiento (batch)
w_gd, hist = gradient_descent(Phi_train, y_train, lr=0.1, epochs=300, batch_size=None, l2=0.0, verbose=True)

print("Pesos (w) [bias, w1]:", w_gd)
print("MSE train:", mse(y_train, predict(Phi_train, w_gd)))
print("MSE valid:", mse(y_valid, predict(Phi_valid, w_gd)))
print("R2   valid:", r2_score(y_valid, predict(Phi_valid, w_gd)))

# Curva de pérdida
plt.figure()
plt.plot(hist["epoch"], hist["train_mse"], label="MSE train")
plt.title("Curva de entrenamiento (MSE)")
plt.xlabel("Época")
plt.ylabel("MSE")
plt.legend()
plt.show()

# Visualizar ajuste en 1D (recordá que entrenamos con X estandarizado)
# Para dibujar la recta, generamos un rango en el espacio estandarizado y lo llevamos a x original para el scatter
plt.figure()
plt.scatter(X_train[:,0], y_train, label="Train")
# Generamos puntos uniformes en el espacio de X estandarizado
xs_std = np.linspace(X_train_std.min(), X_train_std.max(), 100).reshape(-1,1)
phi_xs = add_bias(xs_std)
ys_hat = predict(phi_xs, w_gd)

# Para graficar contra x original, convertimos xs_std a escala original inversa:
xs_orig = xs_std * std_ + mean_
plt.plot(xs_orig[:,0], ys_hat, label="Recta (pred)")
plt.title("Ajuste 1D")
plt.xlabel("x (original)")
plt.ylabel("y")
plt.legend()
plt.show()


"""
## 9) Ecuación normal (solución cerrada)

Para minimizar MSE sin regularización:

`w = (ΦᵀΦ)^(-1) Φᵀ y`  

Es más estable usar **pseudoinversa**: `w = pinv(Φ) @ y`.

Con **Ridge** (λ):

`w = (ΦᵀΦ + λI*)^(-1) Φᵀ y`  

donde `I*` es identidad con 0 en la posición del bias (para no regularizarlo).

"""

def normal_equation(Phi, y, l2=0.0):
    if l2 == 0.0:
        # Pseudoinversa estable
        return np.linalg.pinv(Phi) @ y
    # Ridge: (Phi^T Phi + lambda * I*)^{-1} Phi^T y
    d = Phi.shape[1]
    A = Phi.T @ Phi
    I = np.eye(d)
    I[0,0] = 0.0  # no penalizamos bias
    A_reg = A + l2 * I
    return np.linalg.inv(A_reg) @ Phi.T @ y

w_ne = normal_equation(Phi_train, y_train, l2=0.0)
print("NE pesos:", w_ne)
print("NE MSE valid:", mse(y_valid, predict(Phi_valid, w_ne)))


"""
## 10) Multivariable + Polinomios + Regularización

Agreguemos más features (x², x³) para simular polinomios y apliquemos Ridge.
Cuidado con el **overfitting**: regularización ayuda a controlar la complejidad.

"""

# Construimos features polinomiales hasta grado 3 a partir de X (1D)
def poly_features(x, degree=3):
    # x: shape (n,1) -> devuelve [x, x^2, ..., x^degree]
    feats = [x]
    for p in range(2, degree+1):
        feats.append(x**p)
    return np.hstack(feats)

X_train_poly = poly_features(X_train_std, degree=3)
X_valid_poly = poly_features(X_valid_std, degree=3)

Phi_train_poly = add_bias(X_train_poly)
Phi_valid_poly = add_bias(X_valid_poly)

# Entrenar con Ridge para evitar sobreajuste
w_poly, hist_poly = gradient_descent(Phi_train_poly, y_train, lr=0.05, epochs=500, batch_size=None, l2=0.1, verbose=False)

print("MSE train (poly+ridge):", mse(y_train, predict(Phi_train_poly, w_poly)))
print("MSE valid (poly+ridge):", mse(y_valid, predict(Phi_valid_poly, w_poly)))
print("R2   valid (poly+ridge):", r2_score(y_valid, predict(Phi_valid_poly, w_poly)))

plt.figure()
plt.plot(hist_poly["epoch"], hist_poly["train_mse"], label="MSE train (poly)")
plt.title("Curva de entrenamiento (polinomios + Ridge)")
plt.xlabel("Época")
plt.ylabel("MSE")
plt.legend()
plt.show()


"""
## 11) Para practicar (tareas sugeridas)
1. Cambiá `noise_std` y observá cómo afecta MSE y R².
2. Probá distintos `lr` (`0.001`, `0.01`, `0.1`, `0.3`) y explicá cuándo diverge.
3. Usá `batch_size=1` (SGD) y `batch_size=16` (mini-batch). ¿Cambia la curva de MSE?
4. Subí el grado del polinomio (`degree=5, 7, 10`). ¿Qué pasa sin regularización vs con `l2=1.0`?
5. Implementá **early stopping**: guardá el mejor MSE en valid y pará si no mejora en 50 épocas.
6. Agregá nuevas features manualmente (por ejemplo `sin(x)`) y compará.

"""

