"""
Método de Sumas de Riemann para integración numérica.
Autor: Francisco Bravo (C.I. : 30008866)
"""

import math

def riemann(f, a, b, n=10, regla='medio', mostrar_tabla=False, valor_real=None):
    """
    Aproxima ∫_a^b f(x) dx usando sumas de Riemann.

    Parámetros:
        f : función a integrar
        a, b : límites de integración
        n : número de subintervalos
        regla : 'izquierda', 'derecha', 'medio' o 'trapecio'
        mostrar_tabla : muestra cada subintervalo si True
        valor_real : si se proporciona, calcula error relativo y lo muestra

    Retorna:
        aproximación (float), error_rel (float o None)
    """
    if n <= 0 or a >= b:
        raise ValueError("n debe ser >0 y a < b")
    
    h = (b - a) / n
    suma = 0.0

    if mostrar_tabla:
        print("\n--- Sumas de Riemann ---")
        print(f"Regla: {regla.capitalize()} | n={n} | h={h:.6f}")
        print(f"{'i':<4} {'x_i':<10} {'x_i+1':<10} {'f(x_i)':<10} {'f(x_i+1)':<10} {'Contrib':<12}")
        print("-" * 70)

    for i in range(n):
        xi = a + i * h
        xi1 = xi + h

        if regla == 'izquierda':
            contrib = f(xi) * h
        elif regla == 'derecha':
            contrib = f(xi1) * h
        elif regla == 'medio':
            xm = (xi + xi1) / 2
            contrib = f(xm) * h
        else:  # trapecio
            contrib = (f(xi) + f(xi1)) * h / 2

        suma += contrib

        if mostrar_tabla:
            print(f"{i:<4} {xi:<10.6f} {xi1:<10.6f} {f(xi):<10.6f} {f(xi1):<10.6f} {contrib:<12.8f}")

    error_rel = None
    if valor_real is not None:
        error_rel = abs(suma - valor_real) / abs(valor_real) if valor_real != 0 else float('inf')

    # Resultados: ahora muestra también el valor real si se conoce
    print("\n" + "="*60)
    print("RESULTADOS DE LA INTEGRACIÓN")
    print("="*60)
    print(f"Valor aproximado : {suma:.8f}")
    if valor_real is not None:
        print(f"Valor real       : {valor_real:.8f}")
        print(f"Error relativo   : {error_rel:.2%}")
    else:
        print("Valor real       : no proporcionado")
    print("="*60 + "\n")

    return suma, error_rel


def modo_interactivo():
    """Modo interactivo para ingresar función y parámetros."""
    print("\n=== MODO INTERACTIVO - SUMAS DE RIEMANN ===")
    expr = input("f(x) = ")
    
    # Crear función evaluable de forma segura
    def f(x_val):
        namespace = {
            'x': x_val,
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'exp': math.exp, 'log': math.log, 'sqrt': math.sqrt,
            'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
            'pi': math.pi, 'e': math.e
        }
        return eval(expr, {"__builtins__": None}, namespace)
    
    # Prueba de evaluación
    try:
        f(0.5)
    except:
        print("❌ Error: no se puede evaluar la función.")
        return
    
    # Límites
    try:
        a = float(input("Límite inferior a: "))
        b = float(input("Límite superior b: "))
        if a >= b:
            print("❌ Error: a debe ser menor que b.")
            return
    except ValueError:
        print("❌ Error: ingrese números válidos.")
        return
    
    # Subintervalos
    try:
        n = int(input("Número de subintervalos n: "))
        if n <= 0:
            print("❌ Error: n debe ser positivo.")
            return
    except ValueError:
        print("❌ Error: ingrese un entero.")
        return
    
    # Regla
    print("\nReglas disponibles:")
    print("  1. Izquierda")
    print("  2. Derecha")
    print("  3. Punto medio")
    print("  4. Trapecio")
    op = input("Seleccione regla (1-4): ")
    reglas = {'1': 'izquierda', '2': 'derecha', '3': 'medio', '4': 'trapecio'}
    regla = reglas.get(op, 'medio')
    print(f"✓ Regla: {regla.capitalize()}")
    
    # Valor real (opcional)
    valor_real = None
    if input("¿Conoce el valor exacto? (s/n): ").lower() == 's':
        try:
            valor_real = float(input("Valor exacto: "))
        except:
            print("Valor no válido, se omite.")
    
    # Mostrar tabla?
    mostrar_tabla = input("¿Mostrar tabla de subintervalos? (s/n): ").lower() == 's'
    
    # Calcular
    riemann(f, a, b, n, regla, mostrar_tabla, valor_real)


# ================================
# MENÚ PRINCIPAL
# ================================
if __name__ == "__main__":
    print("MÉTODO DE RIEMANN - Francisco Bravo")
    print("1. Ejecutar ejemplos de demostración")
    print("2. Modo interactivo (ingresar función propia)")
    opcion = input("Seleccione 1 o 2: ")
    
    if opcion == '2':
        modo_interactivo()
    else:
        # --- EJEMPLOS ORIGINALES (sin modificar) ---
        # Ejemplo 1: x² en [0,1]
        f1 = lambda x: x**2
        riemann(f1, 0, 1, n=10, regla='medio', mostrar_tabla=True, valor_real=1/3)
    
        # Ejemplo 2: 3x*sqrt(x²+1) en [0,1]
        f2 = lambda x: 3 * x * math.sqrt(x**2 + 1)
        print("\n--- Comparación de reglas (n=4) ---")
        for reg in ['izquierda', 'derecha', 'medio', 'trapecio']:
            aprox, err = riemann(f2, 0, 1, n=4, regla=reg, valor_real=1.828)
            print(f"{reg.capitalize():10s}: {aprox:.6f}  error {err:.2%}")
        print("-" * 40)
    
        # Ejemplo 3: sin(x) en [0,π]
        f3 = math.sin
        riemann(f3, 0, math.pi, n=8, regla='trapecio', mostrar_tabla=True, valor_real=2)
    
    # Opción de repetir
    while input("\n¿Realizar otro cálculo? (s/n): ").lower() == 's':
        if input("¿Usar modo interactivo? (s/n): ").lower() == 's':
            modo_interactivo()
        else:
            # Repetir un ejemplo rápido (solo el primero como muestra)
            f1 = lambda x: x**2
            riemann(f1, 0, 1, n=10, regla='medio', mostrar_tabla=False, valor_real=1/3)