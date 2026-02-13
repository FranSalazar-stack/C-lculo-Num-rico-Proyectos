"""
Método de Newton‑Raphson
Autor: Francisco Bravo (C.I 30008866)
"""

import math

def newton_raphson(f, x0, df=None, tol=1e-6, max_iter=100, verbose=True):
    """
    Encuentra una raíz de f(x)=0 mediante Newton‑Raphson.

    Parámetros:
        f: función
        x0: valor inicial
        df: derivada (opcional, si no se da se aproxima)
        tol: tolerancia para |x_nuevo - x_anterior|
        max_iter: número máximo de iteraciones
        verbose: muestra tabla si True

    Retorna:
        (raíz, error, iteraciones)
    """
    if df is None:
        h = 1e-6
        def df(x):
            return (f(x + h) - f(x - h)) / (2 * h)

    x_act = x0
    error = float('inf')
    iteracion = 0

    if verbose:
        print("\n" + "="*60)
        print("         NEWTON‑RAPHSON")
        print("="*60)
        print(f"{'Iter':^6} {'x':^16} {'f(x)':^14} {'df(x)':^14} {'Error':^12}")
        print("-" * 66)

    while iteracion < max_iter and error > tol:
        fx = f(x_act)
        dfx = df(x_act)

        if dfx == 0:
            raise ValueError(f"Derivada cero en x = {x_act}. No se puede continuar.")

        x_sig = x_act - fx / dfx
        error = abs(x_sig - x_act)

        if verbose:
            print(f"{iteracion:6d} {x_act:16.8f} {fx:14.6e} {dfx:14.6e} {error:12.2e}")

        x_act = x_sig
        iteracion += 1

        if abs(fx) < 1e-14:
            error = 0.0
            break

    if verbose:
        print("-" * 66)
        if error <= tol:
            print(f"✅ Convergencia en {iteracion} iteraciones.")
        else:
            print(f"⚠️  Límite de iteraciones alcanzado ({max_iter}).")
        print(f"Raíz aproximada: {x_act:.10f}")
        print(f"Error final: {error:.2e}")
        print("="*60 + "\n")

    return x_act, error, iteracion


def demo():
    """Ejemplos predefinidos."""
    print("\n🔬 EJEMPLOS DE DEMOSTRACIÓN")
    f1 = lambda x: x**2 - 2
    newton_raphson(f1, x0=1.5, tol=1e-8, verbose=True)

    f2 = lambda x: math.exp(x) - 3*x**2
    newton_raphson(f2, x0=0.8, tol=1e-6, verbose=True)

    f3 = lambda x: math.cos(x) - x
    df3 = lambda x: -math.sin(x) - 1
    newton_raphson(f3, x0=0.5, df=df3, tol=1e-10, verbose=True)


def interactivo():
    """Modo interactivo: ingreso de función y parámetros."""
    print("\n" + "="*60)
    print("      NEWTON‑RAPHSON - MODO INTERACTIVO")
    print("="*60)

    expr = input("f(x) = ")
    # Crear función con math
    def f(x_val):
        return eval(expr, {"x": x_val, "math": math, "__builtins__": {}})

    # Verificar que se puede evaluar
    try:
        f(0.5)
    except:
        print("❌ Error: no se puede evaluar la función.")
        return

    # Derivada opcional
    df = None
    if input("¿Ingresar derivada? (s/n): ").lower() == 's':
        df_expr = input("f'(x) = ")
        def df(x_val):
            return eval(df_expr, {"x": x_val, "math": math, "__builtins__": {}})
        try:
            df(0.5)
        except:
            print("⚠️  Derivada inválida, se usará numérica.")
            df = None

    try:
        x0 = float(input("Valor inicial x0: "))
        tol = float(input("Tolerancia (ej: 1e-6): "))
        max_iter = int(input("Máximo de iteraciones: "))
        if max_iter <= 0:
            max_iter = 100
    except ValueError:
        print("❌ Valor no válido, se usan valores por defecto.")
        x0, tol, max_iter = 0.0, 1e-6, 100

    mostrar = input("¿Mostrar tabla? (s/n): ").lower() == 's'

    try:
        raiz, error, it = newton_raphson(f, x0, df, tol, max_iter, verbose=mostrar)
        if not mostrar:
            print(f"\nRaíz aproximada: {raiz:.8f}")
            print(f"Error final: {error:.2e}")
            print(f"Iteraciones: {it}")
    except Exception as e:
        print(f"❌ {e}")


if __name__ == "__main__":
    print("MÉTODO DE NEWTON‑RAPHSON")
    print("1. Modo interactivo")
    print("2. Ejecutar ejemplos")
    op = input("Seleccione 1 o 2: ")

    if op == '2':
        demo()
    else:
        interactivo()

    while input("\n¿Otro cálculo? (s/n): ").lower() == 's':
        if input("¿Modo interactivo? (s/n): ").lower() == 's':
            interactivo()
        else:
            demo()