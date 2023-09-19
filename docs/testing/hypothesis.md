# Hypothesis

## Introducción

Cuando escribes pruebas unitarias, es difícil estar seguro de que has cubierto todos los casos de prueba posibles. Puedes pensar en algunos casos obvios, pero es fácil pasar por alto casos extremos o situaciones inesperadas. El Property-based Testing (Pruebas basadas en propiedades) es una técnica de prueba que aborda este problema al permitirte definir propiedades generales que tu código debe cumplir y luego generar automáticamente una amplia variedad de casos de prueba para verificar esas propiedades.

En lugar de escribir casos de prueba específicos uno por uno, el Property-based Testing utiliza la generación automática de datos de prueba y las propiedades declarativas para evaluar la calidad de tu código. Esto ayuda a descubrir errores inesperados y a probar una variedad más amplia de escenarios que las pruebas tradicionales.

En Python, una de las bibliotecas más populares para realizar Property-based Testing es **Hypothesis**.

## Hypothesis: Una visión general

[Hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html) es una poderosa biblioteca de Property-based Testing para Python. Ofrece una amplia gama de estrategias de generación de datos y se integra bien con los sistemas de prueba existentes, como pytest.

### Ejemplo: Factorización de enteros

Para ilustrar cómo funciona Hypothesis en la práctica, consideremos un ejemplo simple: la factorización de enteros. Supongamos que tenemos una función `factorize(n: int) -> List[int]` que toma un número entero `n` y devuelve una lista de sus factores primos. Vamos a explorar cómo podemos usar Hypothesis para probar esta función.

```python
from typing import List
import math

def factorize(number: int) -> List[int]:
    if number in [-1, 0, 1]:
        return [number]
    if number < 0:
        return [-1] + factorize(-number)
    factors = []

    while number % 2 == 0:
        factors.append(2)
        number = number // 2

    if number == 1:
        return factors

    i = 3
    while i <= int(math.ceil(number ** 0.5)) + 1:
        while number % i == 0:
            factors.append(i)
            number = number // i
        i += 2

    return factors
```

### Escribiendo pruebas unitarias tradicionales

Enfoquémonos primero en escribir pruebas unitarias tradicionales para nuestra función `factorize`. Aquí hay algunas pruebas de ejemplo utilizando el módulo `unittest`:

```python
import unittest

class TestFactorize(unittest.TestCase):
    def test_factorize_zero(self):
        self.assertEqual(factorize(0), [0])

    def test_factorize_one(self):
        self.assertEqual(factorize(1), [1])

    def test_factorize_negative(self):
        self.assertEqual(factorize(-1), [-1])

    def test_factorize_negative_prime(self):
        self.assertEqual(factorize(-2), [-1, 2])

    def test_factorize_prime(self):
        self.assertEqual(factorize(2), [2])

    def test_factorize_another_prime(self):
        self.assertEqual(factorize(3), [3])

    def test_factorize_multiple_primes(self):
        self.assertEqual(factorize(6), [2, 3])

    def test_factorize_same_prime_multiple_times(self):
        self.assertEqual(factorize(8), [2, 2, 2])

if __name__ == '__main__':
    unittest.main()
```

Estas pruebas son específicas y están diseñadas para casos de entrada particulares. A medida que aumenta la complejidad de la función, escribir pruebas unitarias tradicionales para todos los casos posibles puede volverse tedioso y propenso a errores.

### Escribiendo pruebas basadas en propiedades con Hypothesis

Ahora, veamos cómo podemos usar Hypothesis para escribir pruebas basadas en propiedades para la función `factorize`. Definiremos una propiedad que debería cumplir esta función: el producto de los factores primos devueltos debe ser igual al número original.

```python
import hypothesis.strategies as st
from hypothesis import given

@given(st.integers(min_value=-(10 ** 6), max_value=10 ** 6))
def test_factorize_property(n):
    factors = factorize(n)
    product = 1
    for factor in factors:
        product *= factor
    assert product == n, f"factorize({n}) returned {factors}"
```

En este código:

- Utilizamos la decoración `@given` de Hypothesis para declarar una propiedad de prueba.
- Usamos la estrategia `st.integers` para generar enteros en un rango razonable de -1,000,000 a 1,000,000, lo que nos permite probar una amplia gama de valores.
- Luego, dentro de la prueba, factorizamos el número y calculamos el producto de los factores primos.
- Comparamos el producto con el número original y afirmamos que deben ser iguales.

### Ejecutando pruebas con Hypothesis

Para ejecutar las pruebas con Hypothesis, simplemente usamos un comando de prueba como `pytest`:

```bash
pytest nombre_del_archivo_de_prueba.py
```

Hypothesis generará automáticamente un conjunto diverso de ejemplos para probar nuestra propiedad. Si encuentra un caso que no cumple con la propiedad, lo informará, lo que nos ayudará a encontrar errores en nuestra función `factorize`.

### Beneficios de Property-based Testing con Hypothesis

Property-based Testing con Hypothesis ofrece varios beneficios:

1. **Cobertura exhaustiva**: Genera automáticamente una amplia gama de casos de prueba, lo que puede revelar problemas que no se encuentran en las pruebas tradicionales.

2. **Identificación de errores inesperados**: Puede descubrir errores que no habías considerado al probar casos específicos.

3. **Refactorización segura**: Cuando refactorizas o cambias el código, Hypothesis puede ayudarte a asegurarte de que las propiedades fundamentales de tu código aún se mantengan.

4. **Ahorro de tiempo**: Escritura menos pruebas específicas y más pruebas basadas en propiedades puede ahorrar tiempo en la escritura y mantenimiento de pruebas.

5. **Facilita la exploración de esquinas y casos límite**: Puedes probar casos que nunca habrías pens

ado en escribir manualmente.

## Conclusiones

Property-based Testing con Hypothesis es una técnica poderosa para mejorar la calidad de tus pruebas y encontrar errores difíciles de detectar. A medida que tu código crece en complejidad, las pruebas basadas en propiedades pueden convertirse en una parte esencial de tu proceso de desarrollo.

Recuerda que, aunque Hypothesis puede ayudarte a encontrar problemas, aún es importante usar tu juicio y experiencia para interpretar los resultados de las pruebas y corregir los errores de manera adecuada. Además, investiga más sobre Hypothesis y sus estrategias de generación de datos para aprovechar al máximo esta valiosa herramienta de pruebas.

## Referencias

- [Documentación oficial de Hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html)
- [Propiedades y generación de datos con Hypothesis](https://hypothesis.readthedocs.io/en/latest/stateful.html)
- [Estrategias de generación de datos en Hypothesis](https://hypothesis.readthedocs.io/en/latest/data.html)
- [Introducción a Property-based Testing con Python y Hypothesis](https://engineering.hellofresh.com/an-introduction-to-property-based-testing-with-python-and-hypothesis-5b0121d4e9db)
- [Property-Based Testing in Python with Hypothesis](https://semaphoreci.com/community/tutorials/property-based-testing-in-python-with-hypothesis)