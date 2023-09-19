# Mocking 
En el desarrollo de software, las pruebas unitarias son esenciales para garantizar que su código funcione correctamente. Sin embargo, a menudo es necesario simular o "burlarse" de ciertas partes de su código para probar componentes de manera aislada y controlada. Esto se logra mediante el uso de mocks o "mocker" en el contexto de pruebas. En esta guía, exploraremos qué es el "mocking", cómo se aplica en las pruebas unitarias y cómo utilizarlo en conjunto con Pytest, un popular marco de pruebas para Python.

## ¿Qué es el Mocking en Pruebas Unitarias?

El "mocking" es una técnica que implica simular el comportamiento de ciertas partes de su código para probar componentes de manera aislada. En lugar de usar implementaciones reales, se utilizan objetos simulados o "mocks" que imitan el comportamiento de los objetos reales, pero de manera controlada.

Los "mocks" se utilizan principalmente para:

1. **Aislar Componentes**: Al simular componentes externos, como bases de datos o servicios web, puede aislar la unidad que está probando y evitar que interactúe con componentes reales durante las pruebas.

2. **Controlar Comportamientos**: Puede especificar el comportamiento deseado de un "mock" para que se comporte de una manera particular durante una prueba.

3. **Simular Condiciones de Error**: Puede simular condiciones de error o excepciones lanzadas por un componente para asegurarse de que su código maneje adecuadamente estas situaciones.

## Aplicación de Mocking con Pytest

Pytest es un marco de pruebas popular en Python que ofrece soporte integrado para el "mocking" a través de la biblioteca `unittest.mock`. A continuación, veremos cómo aplicar el "mocking" en pruebas unitarias con Pytest.

### Configuración Inicial

Antes de comenzar a utilizar "mocks" en sus pruebas con Pytest, asegúrese de tener instalado Pytest y la biblioteca `unittest.mock` (también conocida como `mock`) si aún no las ha instalado:

```bash
pip install pytest
pip install pytest-mock
```

### Ejemplo de Mocking con Pytest

Supongamos que tiene una función que realiza una solicitud HTTP a una API externa y procesa la respuesta. Desea probar esta función sin depender de la API real, por lo que utilizará un "mock" para simular la solicitud HTTP.

Primero, definimos la función que realiza la solicitud HTTP en un módulo llamado `api_client.py`:

```python
# api_client.py
import requests

def get_data_from_api(url):
    response = requests.get(url)
    return response.json()
```

Luego, escribiremos una prueba unitaria utilizando Pytest y un "mock" para simular la solicitud HTTP. Creamos un archivo de prueba llamado `test_api_client.py`:

```python
# test_api_client.py
import pytest
from unittest.mock import Mock
from api_client import get_data_from_api

def test_get_data_from_api(mocker):
    # Creamos un mock de requests.get
    mock_get = mocker.patch('requests.get')

    # Configuramos el comportamiento del mock
    mock_get.return_value.json.return_value = {'data': 'mocked_data'}

    # Llamamos a la función bajo prueba
    result = get_data_from_api('http://example.com/api/data')

    # Verificamos que se llamara a requests.get con la URL correcta
    mock_get.assert_called_once_with('http://example.com/api/data')

    # Verificamos que la función devuelva el valor esperado del mock
    assert result == {'data': 'mocked_data'}
```

En esta prueba:

- Importamos `pytest` y `unittest.mock` (alias `mocker`) para usarlos en la prueba.

- Creamos un "mock" de la función `requests.get` utilizando `mocker.patch`. Esto simula la función `get` de la biblioteca `requests`.

- Configuramos el comportamiento del "mock" para que devuelva un valor simulado cuando se llama a `json`. Esto simula la respuesta de la API.

- Llamamos a la función `get_data_from_api` con la URL, que debería utilizar el "mock" en lugar de realizar una solicitud real.

- Verificamos que la función `requests.get` se llamó una vez con la URL correcta utilizando `assert_called_once_with`.

- Finalmente, verificamos que la función bajo prueba devuelva el valor esperado.

### Uso Avanzado de Mocking

El "mocking" con Pytest y `unittest.mock` permite una variedad de configuraciones avanzadas, como especificar valores de retorno dinámicos, contar cuántas veces se llama una función y capturar llamadas y argumentos.

Por ejemplo, para especificar un valor de retorno

 dinámico, puede usar `side_effect`:

```python
# Configurar un mock con un valor de retorno dinámico
mock_get.side_effect = [Exception('Error 1'), {'data': 'mocked_data'}]
```

### Conclusiones

El "mocking" es una técnica poderosa en las pruebas unitarias que le permite controlar el comportamiento de componentes externos y aislar unidades de código para pruebas efectivas. Pytest junto con la biblioteca `unittest.mock` hace que el proceso de "mocking" sea más fácil y efectivo en el contexto de las pruebas en Python.

Al utilizar "mocks", puede asegurarse de que sus pruebas se ejecuten de manera controlada y repetible, lo que aumenta la confianza en la calidad de su código y permite identificar y corregir problemas de manera eficiente.