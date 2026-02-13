Métodos Numéricos en Python

Este repositorio contiene tres programas en Python para métodos numéricos clásicos, diseñados para ser claros, interactivos y sin dependencias externas.

Bisección

Encuentra raíces de una función continua en un intervalo dado. El código pide la función, los límites, la tolerancia y el máximo de iteraciones. Muestra una tabla con cada iteración y entrega la raíz aproximada junto con el error relativo.

Newton‑Raphson

Aproxima raíces a partir de un valor inicial. Puede recibir la derivada de forma opcional; si no se entrega, la calcula numéricamente. Permite elegir el criterio de error (relativo, absoluto o residual) y muestra el progreso paso a paso. Devuelve la raíz, el error final y un historial completo de iteraciones.

Sumas de Riemann

Integración numérica mediante rectángulos o trapecios. Soporta cuatro reglas: izquierda, derecha, punto medio y trapecio. El usuario ingresa la función, los límites, el número de subintervalos y la regla. Si se conoce el valor exacto, también calcula y muestra el error relativo. Opcionalmente puede imprimir una tabla detallada de cada subintervalo.

Todos los programas incluyen un menú que permite elegir entre ejecutar ejemplos predefinidos o ingresar una función propia. Están escritos en Python puro, solo con la librería math, y son funcionales desde la primera ejecución.
