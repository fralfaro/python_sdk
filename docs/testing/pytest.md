# Pytest
## Introducción

Pytest es un framework de pruebas en Python que simplifica el proceso de escribir y ejecutar pruebas de unidad y funcionales. A lo largo de este artículo, exploraremos en detalle cómo usar Pytest para escribir pruebas, organizarlas y aprovechar algunas de sus características avanzadas. También se proporcionarán ejemplos concretos para ilustrar cada concepto.

## Instalación

Para comenzar, debes asegurarte de tener Pytest instalado en tu entorno. Si aún no lo has hecho, puedes instalarlo utilizando pip:

```bash
pip install pytest
```

## Estructura de las pruebas

Antes de profundizar en el uso de Pytest, es importante comprender cómo se estructuran las pruebas en un proyecto. Pytest busca automáticamente archivos de prueba en directorios y archivos que sigan una convención específica. Aquí hay un ejemplo de una estructura de proyecto de prueba:

```
mi_proyecto/
|-- mi_modulo.py
|-- tests/
|   |-- test_mi_modulo.py
```

En este ejemplo:

- `mi_proyecto` es el directorio principal de tu proyecto.
- `mi_modulo.py` es el módulo que deseas probar.
- `tests` es un directorio que contiene archivos de prueba.
- `test_mi_modulo.py` es el archivo de prueba específico para `mi_modulo.py`.

Pytest busca archivos que comiencen con `test_` o terminen con `_test.py` en el directorio `tests` por defecto. Puedes personalizar estas convenciones si es necesario.

## Primeros pasos con Pytest

Ahora, vamos a crear algunas pruebas simples para un módulo hipotético llamado `mi_modulo.py`.

### Creación de funciones para probar

Primero, creemos algunas funciones en `mi_modulo.py` que queremos probar. Aquí hay un ejemplo:

```python
# mi_modulo.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
```

### Escribir pruebas básicas

A continuación, crearemos un archivo de prueba llamado `test_mi_modulo.py` en el directorio `tests` para escribir nuestras pruebas. Las funciones de prueba deben comenzar con `test_`.

```python
# test_mi_modulo.py
from mi_modulo import sumar, restar

def test_sumar():
    resultado = sumar(2, 3)
    assert resultado == 5

def test_restar():
    resultado = restar(5, 2)
    assert resultado == 3
```

### Ejecutar las pruebas

Para ejecutar las pruebas, simplemente ejecuta `pytest` desde el directorio raíz del proyecto:

```bash
pytest
```

Pytest buscará automáticamente los archivos de prueba en el directorio `tests` y ejecutará las pruebas. Deberías ver una salida similar a esta:

```
============================== test session starts ===============================
platform linux -- Python 3.x.x, pytest-6.x.x, pluggy-0.x.x
rootdir: /ruta/a/tu/proyecto
collected 2 items                                                              

test_mi_modulo.py ..                                                      [100%]

=============================== 2 passed in 0.12s ===============================
```

Esto indica que ambas pruebas han pasado con éxito.

## Marcadores (Markers)

Los marcadores son etiquetas que puedes aplicar a tus pruebas y que te permiten organizar y ejecutar pruebas de manera selectiva. Pytest incluye varios marcadores incorporados, como `@pytest.mark.skip`, `@pytest.mark.xfail`, y otros, pero también puedes crear tus propios marcadores personalizados.

### Ejemplo de uso de marcadores incorporados

#### `@pytest.mark.skip`

Este marcador permite omitir una prueba específica. Por ejemplo, si tienes una prueba que no es relevante en un sistema operativo en particular, puedes omitirla con `@pytest.mark.skip`.

```python
import pytest

@pytest.mark.skip(reason="No es relevante en Linux")
def test_alguna_prueba():
    # Tu código de prueba aquí
```

#### `@pytest.mark.xfail`

Este marcador indica que se espera que una prueba falle. Puede ser útil cuando se está trabajando en el desarrollo y se sabe que una prueba fallará hasta que se implemente una corrección.

```python
import pytest

@pytest.mark.xfail
def test_prueba_que_fallara():
    # Tu código de prueba aquí
```

### Ejemplo de marcador personalizado

Puedes crear tus propios marcadores personalizados para clasificar tus pruebas de acuerdo a tus necesidades. Por ejemplo, podrías crear un marcador personalizado llamado `@pytest.mark.api` para pruebas relacionadas con una API.

```python
import pytest

@pytest.mark.api
def test_obtener_datos_de_la_api():
    # Tu código de prueba aquí
```

Luego, puedes ejecutar pruebas específicas con marcadores usando el siguiente comando:

```bash
pytest -m marcador
```

Por ejemplo, para ejecutar todas las pruebas con el marcador `@pytest.mark.api`, puedes usar:

```bash
pytest -m api
```

## Parámetros en pruebas parametrizadas

Pytest permite definir parámetros en pruebas parametrizadas. Esto es útil cuando deseas ejecutar la misma prueba con diferentes conjuntos de datos o condiciones. Para usar pruebas parametrizadas, utiliza el decorador `@pytest.mark.parametrize`.

### Ejemplo de prueba parametrizada

Supongamos que queremos probar una función `dividir(a, b)` con varios conjuntos de datos de entrada y resultados esperados. Podemos hacerlo de la siguiente manera:

```python
import pytest

def dividir(a, b):
    return a / b

@pytest.mark.parametrize("entrada, resultado_esperado", [
    (2, 1),
    (6, 2),
    (10, 5),
])
def test_dividir(entrada, resultado_esperado):
    resultado = dividir(entrada, 2)
    assert resultado == resultado_esperado
```

En este ejemplo, hemos parametrizado la prueba con tres conjuntos de datos diferentes, lo que significa que la prueba `test_dividir` se ejecutará tres veces, una vez para cada conjunto de datos. Pytest tomará automáticamente los valores de entrada y resultados esperados y los pasará como argumentos a la función de prueba.

## Uso de fixtures

Las fixtures son funciones que proporcionan datos de configuración o recursos necesarios para las pruebas. Puedes utilizar el decorador `@pytest.fixture` para definir una fixture.

### Ejemplo de fixture

Supongamos que tenemos una base de datos SQLite que queremos usar en nuestras pruebas. Podemos crear una fixture para crear y configurar la base de datos antes de que las pruebas la utilicen.

```python
import

 pytest
import sqlite3

# Fixture para crear y configurar la base de datos
@pytest.fixture
def base_de_datos():
    conexion = sqlite3.connect(':memory:')  # Base de datos en memoria
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT)''')
    conexion.commit()
    yield conexion  # Proporciona la conexión a las pruebas
    conexion.close()  # Cierra la conexión después de las pruebas

# Ejemplo de prueba que utiliza la fixture
def test_insertar_usuario(base_de_datos):
    cursor = base_de_datos.cursor()
    cursor.execute("INSERT INTO usuarios (nombre) VALUES ('Alice')")
    base_de_datos.commit()
    cursor.execute("SELECT nombre FROM usuarios WHERE id=1")
    resultado = cursor.fetchone()
    assert resultado[0] == 'Alice'
```

En este ejemplo, la fixture `base_de_datos` crea una base de datos SQLite en memoria y la configura con una tabla de usuarios. Luego, la conexión a la base de datos se proporciona como un argumento a la función de prueba `test_insertar_usuario`.


## Organización de pruebas en carpetas

Organizar tus pruebas en carpetas es una buena práctica para mantener tu código organizado y fácil de mantener. A continuación, se muestra una estructura de carpetas común para un proyecto de prueba:

```
mi_proyecto/
|-- mi_modulo.py
|-- tests/
|   |-- unit/
|   |   |-- test_mi_modulo.py
|   |-- integration/
|   |   |-- test_integracion.py
|   |-- end_to_end/
|       |-- test_e2e.py
```

En esta estructura:

- `mi_proyecto` es el directorio principal de tu proyecto.
- `mi_modulo.py` es el módulo que deseas probar.
- `tests` es el directorio que contiene todas las pruebas.
- `unit` es una carpeta que contiene pruebas de unidades.
- `integration` es una carpeta que contiene pruebas de integración.
- `end_to_end` es una carpeta que contiene pruebas de extremo a extremo.

Puedes crear tantas carpetas de prueba como necesites para organizar tus pruebas de manera lógica. A continuación, se detallan algunos ejemplos de cómo escribir pruebas en estas carpetas.

## Pruebas de unidad

Las pruebas de unidad se centran en probar unidades individuales de código, como funciones o métodos, de forma aislada. Aquí hay un ejemplo de cómo escribir pruebas de unidad:

```python
# mi_modulo.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
```

```python
# tests/unit/test_mi_modulo.py
from mi_modulo import sumar, restar

def test_sumar():
    resultado = sumar(2, 3)
    assert resultado == 5

def test_restar():
    resultado = restar(5, 2)
    assert resultado == 3
```

Para ejecutar estas pruebas de unidad, utiliza el comando `pytest` desde la carpeta raíz del proyecto:

```bash
pytest tests/unit
```

## Pruebas de integración

Las pruebas de integración verifican cómo varias partes de un sistema interactúan entre sí. Aquí hay un ejemplo de cómo escribir pruebas de integración para el mismo módulo:

```python
# tests/integration/test_integracion.py
from mi_modulo import sumar, restar

def test_sumar_y_restar():
    resultado1 = sumar(2, 3)
    resultado2 = restar(resultado1, 1)
    assert resultado2 == 4
```

Para ejecutar estas pruebas de integración, utiliza el comando `pytest` desde la carpeta raíz del proyecto:

```bash
pytest tests/integration
```

## Pruebas de extremo a extremo (End-to-End)

Las pruebas de extremo a extremo (E2E) verifican todo el flujo de una aplicación, desde la entrada hasta la salida. Estas pruebas son más complejas y pueden involucrar múltiples componentes o sistemas. A continuación, un ejemplo de cómo escribir pruebas E2E:

```python
# tests/end_to_end/test_e2e.py

def test_flujo_completo():
    # Simula el flujo completo de la aplicación
    # (por ejemplo, abrir la aplicación, interactuar con la interfaz de usuario, etc.)
    resultado = funcion_principal_de_la_aplicacion()
    assert resultado == "Éxito"
```

Las pruebas E2E pueden ser más complicadas y requerir herramientas adicionales para simular la interacción del usuario o configurar el entorno adecuadamente. El enfoque de estas pruebas depende de la naturaleza de tu aplicación.

Para ejecutar estas pruebas E2E, utiliza el comando `pytest` desde la carpeta raíz del proyecto:

```bash
pytest tests/end_to_end
```

Con esta estructura de carpetas y ejemplos, puedes organizar tus pruebas de manera efectiva y ejecutar pruebas específicas según tus necesidades. A medida que desarrollas tu proyecto, puedes agregar más pruebas a cada carpeta según sea necesario.