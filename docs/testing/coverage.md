# Coverage

La cobertura de código es una práctica esencial en el desarrollo de software que permite evaluar qué parte de su código fuente se ha ejecutado durante la ejecución de pruebas. Cuanto mayor sea la cobertura, mayor será la confianza en la calidad de su código. En esta guía, exploraremos en detalle qué es la cobertura de código y cómo se puede medir utilizando Pytest, una herramienta popular en el mundo de las pruebas de Python.

## ¿Qué es la Cobertura de Código?

La cobertura de código es una medida que cuantifica la proporción del código fuente que se ha ejecutado al menos una vez durante la ejecución de las pruebas. En otras palabras, proporciona una idea de qué partes de su código han sido "visitadas" por las pruebas y qué partes aún no se han examinado.

Una alta cobertura de código no garantiza que su software sea libre de errores, pero ofrece varias ventajas clave:

1. **Identificación de Código No Utilizado**: La cobertura de código puede revelar partes de su código que no se utilizan y, por lo tanto, pueden eliminarse o refactorizarse para mejorar la eficiencia.

2. **Detección Temprana de Problemas**: Al medir la cobertura de código, puede descubrir áreas del código que no se prueban adecuadamente y, por lo tanto, tienen un mayor riesgo de contener errores.

3. **Confianza en las Pruebas**: Una alta cobertura de código proporciona una mayor confianza en la efectividad de sus pruebas. Si las pruebas han recorrido la mayoría de las rutas de su código, es más probable que detecten problemas.

4. **Documentación Implícita**: La cobertura de código puede servir como documentación implícita al mostrar qué partes del código son esenciales y se han probado.

## Cobertura de Código con Pytest

Pytest es un marco de prueba popular para Python que se integra bien con herramientas de cobertura de código como `coverage.py`. A continuación, veremos cómo configurar y utilizar Pytest para medir la cobertura de código.

### Configuración Inicial

Antes de comenzar a medir la cobertura de código con Pytest, asegúrese de tener instalados los siguientes componentes:

1. **Pytest**: Instale Pytest utilizando pip si aún no lo ha hecho:

   ```bash
   pip install pytest
   ```

2. **Coverage.py**: Instale la herramienta de cobertura de código coverage.py:

   ```bash
   pip install coverage
   ```

### Ejecución de Pruebas con Cobertura de Código

Para medir la cobertura de código con Pytest y `coverage.py`, siga estos pasos:

1. **Escriba sus pruebas**: Cree las pruebas unitarias para su código utilizando Pytest. Asegúrese de tener pruebas que cubran diferentes aspectos de su código.

2. **Ejecute Pytest con Coverage.py**: Utilice el comando `coverage run` para ejecutar Pytest y medir la cobertura de código. Reemplace `your_test_file.py` con el nombre de su archivo de pruebas.

   ```bash
   coverage run -m pytest your_test_file.py
   ```

3. **Genere un Informe de Cobertura**: Después de ejecutar sus pruebas, use `coverage report` para generar un informe detallado de la cobertura de código.

   ```bash
   coverage report -m
   ```

El informe de cobertura mostrará qué porcentaje del código fuente se ha ejecutado durante las pruebas. También proporcionará información sobre qué líneas de código se han ejecutado y cuáles no.

### Ejemplo de Cobertura de Código con Pytest

Para ilustrar cómo funciona la cobertura de código con Pytest, consideremos un ejemplo simple. Supongamos que tenemos una función en un módulo llamado `math_operations.py` que realiza operaciones matemáticas básicas:

```python
# math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Ahora, escribiremos pruebas para estas funciones en un archivo llamado `test_math_operations.py`:

```python
# test_math_operations.py
import math_operations

def test_add():
    result = math_operations.add(2, 3)
    assert result == 5

def test_subtract():
    result = math_operations.subtract(5, 3)
    assert result == 2
```

Luego, ejecutaremos Pytest con Coverage.py para medir la cobertura de código:

```bash
coverage run -m pytest test_math_operations.py
```

Finalmente, generaremos un informe de cobertura:

```bash
coverage report -m
```

El informe mostrará el porcentaje de cobertura de código y resaltará las líneas que se han ejecutado (en verde) y las que no (en rojo). Esto proporciona una visión clara de las áreas de su código que necesitan más pruebas.

## Conclusiones

La cobertura de código es una práctica fundamental en el desarrollo de software que ayuda a garantizar que su código sea robusto y libre de errores. Pytest y `coverage.py` son herramientas poderosas que facilitan la medición de la cobertura de código en proyectos de Python.

Al utilizar Pytest junto con `coverage.py`, puede escribir pruebas efectivas y tener una visión clara de qué partes de su código necesitan una cobertura adicional. Esto conduce a un código más confiable y de mayor calidad en sus proyectos de desarrollo de software.