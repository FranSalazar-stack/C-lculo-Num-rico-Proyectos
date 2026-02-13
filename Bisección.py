"""
Método de bisección para encontrar raíces de una función continua.
Autor: Francisco Bravo (CI:30008866)
"""

import math

def biseccion(f, a, b, tol=1e-6, max_iter=100, verbose=True):
    """
    Encuentra una raíz de la función f en el intervalo [a, b] usando el método de bisección.

    Parámetros
    ----------
    f : function
        Función continua tal que f(a) * f(b) < 0.
    a : float
        Extremo izquierdo del intervalo.
    b : float
        Extremo derecho del intervalo.
    tol : float, opcional
        Tolerancia para el error relativo (por defecto 1e-6).
    max_iter : int, opcional
        Número máximo de iteraciones (por defecto 100).
    verbose : bool, opcional
        Si es True, imprime la tabla de progreso y resumen (por defecto True).

    Retorna
    -------
    raiz : float
        Aproximación de la raíz.
    error : float
        Error relativo estimado en la última iteración.

    Lanza
    -----
    ValueError
        Si f(a) * f(b) >= 0 (no hay cambio de signo).
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        raise ValueError("La función debe tener signo opuesto en los extremos del intervalo.")
    elif fa == 0:
        return a, 0.0
    elif fb == 0:
        return b, 0.0

    iteracion = 0
    error = float('inf')
    m_anterior = None

    if verbose:
        print("\n" + "=" * 70)
        print("MÉTODO DE BISECCIÓN")
        print("=" * 70)
        print(f"Intervalo inicial: [{a}, {b}]")
        print(f"Tolerancia: {tol}")
        print(f"Iteraciones máximas: {max_iter}")
        print("-" * 70)
        print(f"{'Iter':^5} | {'a':^12} | {'b':^12} | {'m':^12} | {'f(m)':^14} | {'Error':^12}")
        print("-" * 70)

    while error > tol and iteracion < max_iter:
        m_actual = (a + b) / 2.0
        fm = f(m_actual)

        if fm == 0:
            if verbose:
                print(f"{iteracion:5d} | {a:12.6f} | {b:12.6f} | {m_actual:12.6f} | {fm:14.6f} | {'0.0':<12}")
                print("\n✓ Raíz exacta encontrada (f(m) = 0).")
            return m_actual, 0.0

        if m_anterior is not None:
            error = abs((m_actual - m_anterior) / m_actual)
        else:
            error = float('inf')

        if verbose:
            error_str = f"{error:.2e}" if m_anterior is not None else "   ---   "
            print(f"{iteracion:5d} | {a:12.6f} | {b:12.6f} | {m_actual:12.6f} | {fm:14.6f} | {error_str:>12}")

        if fa * fm < 0:
            b = m_actual
            fb = fm
        else:
            a = m_actual
            fa = fm

        m_anterior = m_actual
        iteracion += 1

    if verbose:
        print("-" * 70)
        if error <= tol:
            print(f"\n✓ Convergencia alcanzada en {iteracion} iteraciones.")
        else:
            print(f"\n⚠ Límite de iteraciones alcanzado ({max_iter} iteraciones).")
        print(f"Raíz aproximada: {m_actual:.8f}")
        print(f"Error relativo estimado: {error:.2e}")
        print("=" * 70)

    return m_actual, error


def demo():
    """Ejemplos predefinidos para probar el método."""
    print("\n🔬 EJEMPLOS DE DEMOSTRACIÓN - BISECCIÓN")
    
    # Ejemplo 1: f(x) = e^x - 3x², intervalo [0,1], raíz ≈ 0.91, tolerancia 0.04
    f1 = lambda x: math.exp(x) - 3 * x**2
    print("\n--- Ejemplo 1: f(x)=e^x - 3x², [0,1], tol=0.04 ---")
    biseccion(f1, 0, 1, tol=0.04, max_iter=100, verbose=True)
    
    # Ejemplo 2: f(x) = x³ - x - 2, intervalo [1,2], raíz ≈ 1.521
    f2 = lambda x: x**3 - x - 2
    print("\n--- Ejemplo 2: f(x)=x³ - x - 2, [1,2], tol=1e-6 ---")
    biseccion(f2, 1, 2, tol=1e-6, max_iter=50, verbose=True)


def interactivo():
    """Modo interactivo: usuario ingresa su propia función y parámetros."""
    print("\n" + "=" * 60)
    print("        BISECCIÓN - MODO INTERACTIVO")
    print("=" * 60)
    
    # --- Entrada de la función ---
    expr = input("f(x) = ")
    try:
        import sympy as sp
        x = sp.symbols('x')
        f_expr = sp.sympify(expr)
        f = sp.lambdify(x, f_expr, modules=['math'])
        print("✓ Función interpretada con SymPy.")
    except:
        # Fallback con eval
        def f(x_val):
            namespace = {
                'x': x_val,
                'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                'exp': math.exp, 'log': math.log, 'sqrt': math.sqrt,
                'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
                'pi': math.pi, 'e': math.e
            }
            return eval(expr, {"__builtins__": None}, namespace)
        try:
            f(0.5)
            print("✓ Función interpretada con eval (math).")
        except:
            print("❌ Error: no se puede evaluar la función.")
            return

    # --- Límites ---
    try:
        a = float(input("Límite inferior a: "))
        b = float(input("Límite superior b: "))
        if a >= b:
            print("❌ Error: a debe ser menor que b.")
            return
    except ValueError:
        print("❌ Error: ingrese números válidos.")
        return

    # --- Tolerancia ---
    try:
        tol = float(input("Tolerancia (ej: 1e-6): "))
    except ValueError:
        print("❌ Error: tolerancia no válida. Se usará 1e-6.")
        tol = 1e-6

    # --- Máximo de iteraciones ---
    try:
        max_iter = int(input("Máximo de iteraciones: "))
        if max_iter <= 0:
            print("❌ Error: debe ser positivo. Se usará 100.")
            max_iter = 100
    except ValueError:
        print("❌ Error: valor no válido. Se usará 100.")
        max_iter = 100

    # --- Mostrar tabla? ---
    verbose = input("¿Mostrar tabla de iteraciones? (s/n): ").lower() == 's'

    # --- Calcular ---
    try:
        raiz, err = biseccion(f, a, b, tol, max_iter, verbose)
        print(f"\nResultado final:")
        print(f"  Raíz ≈ {raiz:.8f}")
        print(f"  Error ≈ {err:.2e}")
    except ValueError as e:
        print(f"❌ {e}")


# ================================
# INICIO DEL PROGRAMA
# ================================
if __name__ == "__main__":
    print("MÉTODO DE BISECCIÓN")
    print("1. Modo interactivo (ingresar su propia función)")
    print("2. Ejecutar ejemplos de demostración")
    opcion = input("Seleccione 1 o 2: ")
    
    if opcion == '2':
        demo()
    else:
        interactivo()
    
    while input("\n¿Realizar otro cálculo? (s/n): ").lower() == 's':
        if input("¿Usar modo interactivo? (s/n): ").lower() == 's':
            interactivo()
        else:
            demo()