# Pydantic

## 1. Introducción a Pydantic

### ¿Qué es Pydantic?

**Pydantic** es una biblioteca Python que proporciona una forma sencilla y declarativa de definir modelos de datos y realizar validación de datos. Su objetivo principal es facilitar la validación de datos y la serialización de objetos en aplicaciones Python.

Pydantic se basa en la **anotación de tipos** introducida en Python 3.5 y utiliza estas anotaciones de tipos para definir la estructura de datos esperada. Luego, realiza automáticamente la validación de datos y la conversión de tipos según las reglas especificadas.

### Instalación de Pydantic

Puede instalar Pydantic fácilmente utilizando pip:

```bash
pip install pydantic
```

Una vez que lo haya instalado, está listo para comenzar a usarlo en sus proyectos.

## 2. Definición de Modelos

### Creación de Modelos

En Pydantic, los modelos se crean mediante clases que heredan de `pydantic.BaseModel`. Dentro de estas clases, se definen los campos que compondrán el modelo utilizando las **anotaciones de tipos**. Veamos un ejemplo simple de un modelo de persona:

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
```

En este ejemplo, hemos definido un modelo `Person` con dos campos: `name` de tipo `str` y `age` de tipo `int`.

### Anotaciones de Tipos

Pydantic utiliza anotaciones de tipos para definir la estructura de datos esperada en sus modelos. Las anotaciones de tipos son claras y legibles, lo que facilita la comprensión de la estructura de datos de un vistazo. Puedes utilizar una variedad de tipos de Python incorporados (como `str`, `int`, `float`, `bool`) o incluso tipos personalizados.

### Valores Predeterminados

Puede proporcionar valores predeterminados para los campos de su modelo utilizando el operador de asignación (`=`). Estos valores se utilizarán si no se proporciona un valor para el campo durante la creación del objeto:

```python
class Person(BaseModel):
    name: str = "John Doe"
    age: int = 30
```

En este ejemplo, si no se proporciona un nombre o una edad al crear un objeto `Person`, se utilizarán los valores predeterminados.

## 3. Validación de Datos

### Validación Automática

Una de las características más poderosas de Pydantic es su capacidad para realizar validación de datos de forma automática. Cuando crea una instancia de un modelo, Pydantic verifica si los datos proporcionados cumplen con las reglas definidas en el modelo. Veamos un ejemplo:

```python
data = {
    "name": "Alice",
    "age": 25
}

person = Person(**data)  # Crear una instancia de Person con los datos
```

Pydantic verifica que `data` contenga los campos `name` y `age`, y que `name` sea de tipo `str` y `age` sea de tipo `int`. Si los datos no cumplen con estas reglas, Pydantic genera una excepción `ValidationError`.

### Excepciones de Validación

Cuando se produce una excepción de validación, Pydantic proporciona información detallada sobre los errores, incluyendo el campo afectado y un mensaje de error. Puede capturar y manejar estas excepciones según sea necesario en su aplicación.

```python
from pydantic import ValidationError

try:
    person = Person(name="Alice", age="25")  # 'age' debe ser int, pero se proporciona str
except ValidationError as e:
    print(e)
```

## 4. Serialización y Deserialización

Pydantic facilita la serialización de objetos a formatos como JSON y la deserialización desde estos formatos.

### Serialización a JSON

Puede convertir fácilmente un objeto Pydantic a formato JSON utilizando el método `json()`:

```python
person = Person(name="Alice", age=25)
json_data = person.json

()
print(json_data)
```

El resultado será:

```json
{"name": "Alice", "age": 25}
```

### Deserialización desde JSON

Para deserializar datos JSON en un objeto Pydantic, simplemente cree una instancia del modelo y pase los datos JSON como argumentos:

```python
json_data = '{"name": "Bob", "age": 30}'
person = Person.parse_raw(json_data)
```

Pydantic se encargará de validar y convertir los datos JSON en un objeto Pydantic.

## 5. Modelos Anidados y Herencia

### Modelos Anidados

Pydantic permite la creación de modelos anidados para representar estructuras de datos más complejas. Puede definir modelos dentro de otros modelos y utilizarlos para representar objetos anidados.

```python
from typing import List

class Address(BaseModel):
    street: str
    city: str

class Person(BaseModel):
    name: str
    age: int
    addresses: List[Address]
```

En este ejemplo, el modelo `Person` tiene una lista de direcciones, donde cada dirección es un objeto `Address`. Esto permite representar datos anidados de manera clara y estructurada.

### Herencia de Modelos

Pydantic admite la herencia de modelos, lo que facilita la creación de modelos especializados basados en modelos existentes. Puede heredar campos y comportamientos de un modelo base y personalizarlos según sus necesidades.

```python
class Employee(Person):
    employee_id: int
```

En este ejemplo, `Employee` hereda los campos `name` y `age` del modelo `Person` y agrega un campo adicional `employee_id`. Esto permite reutilizar código y definir modelos de manera eficiente.

## 6. Configuración de Modelos

### Configuraciones de Modelo

Pydantic permite configurar modelos utilizando la clase `Config`. Puede personalizar varios aspectos del comportamiento de un modelo, como el control de alias, la validación de campos adicionales y más.

```python
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(..., alias="fullName")

    class Config:
        allow_population_by_field_name = True
        validate_all = True
```

En este ejemplo, hemos configurado el modelo `Person` para que permita la asignación de valores utilizando el nombre del campo (`allow_population_by_field_name`) y para que realice validación en todos los campos, incluso aquellos sin anotaciones de tipo (`validate_all`).

### Ignorar Campos Desconocidos

Puede configurar un modelo para que ignore campos desconocidos utilizando `Config`:

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str

    class Config:
        ignore_extra = True
```

Esto significa que al crear una instancia de `Person`, cualquier campo no definido en el modelo será ignorado en lugar de generar un error de validación.

## 7. Uso en Aplicaciones Web

### Integración con Frameworks Web

Pydantic se integra perfectamente con marcos web populares como FastAPI y Flask. Aquí, veremos cómo usar Pydantic con FastAPI para validar solicitudes HTTP y respuestas.

#### Ejemplo de Validación de Solicitud HTTP en FastAPI

Supongamos que estamos construyendo una API RESTful en FastAPI y deseamos validar una solicitud POST que contiene datos de usuario en formato JSON. Utilizaremos un modelo Pydantic para definir la estructura esperada de la solicitud y realizar la validación:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str

@app.post("/create_user/")
async def create_user(user: User):
    # 'user' ya está validado por Pydantic
    # Procesamos la solicitud y creamos el usuario en la base de datos
    return {"message": "Usuario creado exitosamente"}
```

En este ejemplo, definimos un modelo Pydantic llamado `User`, que especifica la estructura de datos esperada en la solicitud. FastAPI se encarga automáticamente de validar la solicitud y, si los datos no cumplen con el modelo, devuelve una respuesta de error.

#### Ejemplo de Validación de Respuesta HTTP en FastAPI

También podemos utilizar Pydantic para validar las respuestas de nuestras rutas en FastAPI. Supongamos que queremos validar la respuesta de un usuario:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    email: str

@app.get("/user/{user_id}", response_model=User)
async def read_user(user_id: int):
    # Recuperar datos del usuario de la base de datos
    user_data = {"username": "alice", "email": "alice@example.com"}
    return user_data
```

En este ejemplo, hemos especificado `response_model=User` en la ruta, lo que indica que la respuesta debe cumplir con el modelo `User`. Si la respuesta no coincide con el modelo, FastAPI generará una respuesta de error automáticamente.

## 8. Personalización Avanzada

### Validadores Personalizados

Pydantic permite crear validadores personalizados para aplicar lógica de validación adicional a los campos de un modelo. Esto es útil cuando necesita reglas de validación específicas para sus datos.

#### Ejemplo de Validador Personalizado

Supongamos que estamos creando un modelo para representar fechas de nacimiento y queremos asegurarnos de que las fechas sean válidas y no futuras. Podemos crear un validador personalizado para lograr esto:

```python
from pydantic import BaseModel, validator
from datetime import date

class Person(BaseModel):
    birthdate: date

    @validator("birthdate")
    def validate_birthdate(cls, value):
        if value >= date.today():
            raise ValueError("La fecha de nacimiento no puede ser en el futuro")
        return value
```

En este ejemplo, hemos definido un validador personalizado llamado `validate_birthdate` que verifica si la fecha de nacimiento es válida. Si la fecha es futura, se genera un error.

### Conversiones Personalizadas

Pydantic permite definir métodos de clase personalizados para realizar conversiones personalizadas al analizar datos de entrada.

#### Ejemplo de Conversión Personalizada

Supongamos que queremos representar un campo `score` en nuestro modelo como un valor flotante, pero las solicitudes pueden enviarlo como una cadena. Podemos realizar una conversión personalizada para manejar esto:

```python
from pydantic import BaseModel

class Player(BaseModel):
    name: str
    score: float

    @classmethod
    def parse_obj(cls, obj):
        if isinstance(obj.get("score"), str):
            obj["score"] = float(obj["score"])
        return super().parse_obj(obj)
```

En este ejemplo, hemos definido el método `parse_obj` para convertir el campo `score` de una cadena a un flotante antes de crear una instancia del modelo `Player`.

## 9. Manejo de Errores y Excepciones

Pydantic proporciona excepciones específicas para ayudar en el manejo de errores de validación. Esto permite que su código sea más robusto y proporciona información detallada sobre los problemas de validación.

### Manejo de Excepciones de Validación

Supongamos que estamos creando una aplicación que procesa datos de encuestas y deseamos manejar excepciones de validación de manera adecuada:

```python
from pydantic import BaseModel, ValidationError

class SurveyResult(BaseModel):
    question: str
    answer: int

data = {
    "question": "¿Cuál es tu edad?",
    "answer": "veinticinco"  # Esto debería ser un número entero
}

try:
    result = SurveyResult(**data)
except ValidationError as e:
    print(f"Error de validación: {e}")
```

En este ejemplo, cuando `answer` es una cadena en lugar de un entero, se genera una excepción `ValidationError`. Esto le permite manejar el error de manera adecuada en su aplicación.

## 10. Documentación Automática

Puede generar documentación automáticamente para sus modelos Pydantic utilizando herramientas como Sphinx y `sphinx-pydantic`. Esto facilita la creación de documentación precisa y legible para sus API y aplicaciones.

## 11. Casos de Uso del Mundo Real

### Ejemplos Prácticos

#### Validación en Aplicaciones Web

Pydantic es especialmente útil en aplicaciones web, donde se deben validar las solicitudes entrantes y las respuestas salientes.

#### Procesamiento de Datos

Puede utilizar Pydantic para validar y convertir datos en scripts de procesamiento de datos, lo que garantiza la integridad de los datos en todo momento.

#### Configuración de Aplicaciones

Pydantic se puede usar para cargar y validar archivos de configuración, lo que facilita la configuración de aplicaciones de manera segura y estructurada.

### Aplicaciones Comunes

#### APIs RESTful

Pydantic es una elección sólida para validar datos en solicitudes y respuestas de APIs RESTful, lo que mejora la calidad y la seguridad de sus servicios web.

#### Scripts de Procesamiento

Al utilizar Pydantic en scripts de procesamiento de datos, puede garantizar que los datos se ajusten a las especificaciones deseadas antes de ser procesados.

#### Configuración

 de Aplicaciones

La validación de archivos de configuración con Pydantic ayuda a evitar errores de configuración y simplifica la gestión de la configuración de la aplicación.

## 12. Rendimiento y Consideraciones

Es fundamental tener en cuenta el rendimiento al utilizar Pydantic en aplicaciones que requieren una alta velocidad de procesamiento. Si bien Pydantic es rápido, la validación de datos y la conversión de tipos tienen un costo computacional. Es importante evaluar el impacto en el rendimiento en aplicaciones críticas.

## 13. Conclusiones

Pydantic es una biblioteca Python poderosa y versátil que simplifica la validación y el modelado de datos. Desde la integración con marcos web hasta la creación de validadores y conversiones personalizadas, Pydantic ofrece una amplia gama de características para mejorar la calidad y la robustez de su código. Al aplicar Pydantic en sus proyectos, puede garantizar la integridad de sus datos y simplificar la validación, lo que conduce a aplicaciones más sólidas y seguras.

Esta guía profunda ha explorado en detalle cómo utilizar Pydantic en escenarios del mundo real. Sin embargo, recuerde que Pydantic es una herramienta versátil con aún más características por descubrir. Consulte la documentación oficial de Pydantic para obtener información adicional y ejemplos detallados, y no dude en explorar y aplicar Pydantic en sus propios proyectos para aprovechar al máximo esta valiosa biblioteca de validación de datos en Python. ¡La calidad y la confiabilidad de su código mejorarán significativamente con su uso!