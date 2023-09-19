# Typing

Python es conocido por su simplicidad y flexibilidad, pero a medida que los proyectos crecen en complejidad, puede ser beneficioso agregar una capa de tipado estático para mejorar la legibilidad del código y reducir errores. La biblioteca `typing` es una parte esencial de la caja de herramientas de Python para el tipado estático. En este artículo, exploraremos a fondo la biblioteca `typing`, sus características, ejemplos y cómo se relaciona con los Protocolos PEP (Python Enhancement Proposals).

## Introducción a `typing`

La biblioteca `typing` se introdujo en Python 3.5 y se utiliza para agregar anotaciones de tipos estáticos a las variables, argumentos de función y valores de retorno en el código Python. Aunque Python es un lenguaje de tipado dinámico, estas anotaciones proporcionan información adicional sobre los tipos de datos esperados, lo que puede hacer que el código sea más claro y permitir a las herramientas de análisis de código encontrar errores más fácilmente.

## Anotaciones de Tipos Simples

Empecemos por lo básico: cómo usar `typing` para anotar tipos de variables simples.

### Enteros, Flotantes y Cadenas

```python
from typing import List, Dict

# Anotación de tipos simples
x: int = 5
y: float = 3.14
name: str = "Python"
```

En el código anterior, hemos anotado tres variables con tipos simples: `int`, `float` y `str`.

### Listas y Diccionarios

`typing` también permite anotar estructuras de datos más complejas como listas y diccionarios.

```python
# Anotación de tipos para listas y diccionarios
numbers: List[int] = [1, 2, 3]
student_grades: Dict[str, float] = {'Alice': 95.5, 'Bob': 89.0, 'Charlie': 78.5}
```

Aquí, hemos anotado `numbers` como una lista de enteros y `student_grades` como un diccionario que asigna nombres de estudiantes a calificaciones en punto flotante.

## Tipado de Funciones

Además de anotar variables, `typing` nos permite especificar los tipos de argumentos y valores de retorno en las funciones.

### Funciones sin Tipo de Retorno

```python
def greet(name: str) -> None:
    print(f"Hello, {name}!")

greet("Alice")
```

En este ejemplo, hemos definido una función `greet` que toma un argumento `name` de tipo `str` y no devuelve nada (`None`).

### Funciones con Valores de Retorno

```python
def add(a: int, b: int) -> int:
    return a + b

result: int = add(3, 4)
```

La función `add` toma dos argumentos enteros y devuelve un entero. Hemos anotado tanto los argumentos como el valor de retorno.

## Tipado de Estructuras de Datos

`typing` también es útil para definir estructuras de datos personalizadas, como tuplas y clases.

### Tuplas

```python
from typing import Tuple

point: Tuple[int, int] = (3, 4)
```

En este ejemplo, hemos anotado la variable `point` como una tupla de dos enteros.

### Clases y Atributos

```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, I'm {self.name} and I'm {self.age} years old."

person: Person = Person("Alice", 30)
```

Hemos definido una clase `Person` con anotaciones de tipos para el constructor `__init__` y el método `greet`. Luego, hemos creado una instancia de `Person` llamada `person`.

## Tipado de Contenedores Genéricos

Python permite crear estructuras de datos genéricas utilizando la notación de tipo `typing`, lo que facilita la creación de contenedores altamente flexibles.

### Listas Genéricas

```python
from typing import List, TypeVar

# Definir un tipo genérico
T = TypeVar('T')

def first_element(items: List[T]) -> T:
    return items[0]

numbers: List[int] = [1, 2, 3]
result: int = first_element(numbers)
```

En este ejemplo, hemos definido una función `first_element` que toma una lista genérica de elementos de tipo `T` y devuelve un elemento de tipo `T`. Luego, hemos utilizado esta función con una lista de enteros.

### Diccionarios Genéricos

```python
from typing import Dict, TypeVar

K = TypeVar('K')
V = TypeVar('V')

def get_value(d: Dict[K, V], key: K) -> V:
    return d[key]

grades: Dict[str, float] = {'Alice': 95.5, 'Bob': 89.0, 'Charlie': 78.5}
result: float = get_value(grades, 'Alice')
```

Aquí, hemos definido una función `get_value` que toma un diccionario genérico con claves de tipo `K` y valores de tipo `V`. La función devuelve un valor de tipo `V` dado una clave de tipo `K`.

## Anotaciones de Tipo para Variables Nulas

`typing` también admite anotaciones de tipo para variables que pueden ser nulas (None).

```python


from typing import Optional

def divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b

result: Optional[float] = divide(10, 2)
```

En este ejemplo, hemos anotado la función `divide` para que devuelva un valor opcional (`Optional[float]`). Esto indica que la función puede devolver un número en punto flotante o `None` si la división no es válida.

## Protocolos PEP (PEP 544)

Los Protocolos PEP son una parte importante de `typing`. Estos protocolos proporcionan una forma de definir las características esperadas de un tipo de manera más abstracta. El PEP 544 introduce la idea de Protocolos de Tipo, que se utilizan para describir interfaces en lugar de clases concretas.

### Definición de un Protocolo

Veamos cómo definir un protocolo usando `typing.Protocol`:

```python
from typing import Protocol

class Printable(Protocol):
    def __str__(self) -> str:
        ...
```

En este ejemplo, hemos definido un protocolo llamado `Printable` que describe un objeto que puede convertirse en una cadena.

### Implementación de un Protocolo

Luego, podemos hacer que una clase implemente este protocolo:

```python
class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

book: Printable = Book("The Python Guide", "Python Enthusiast")
```

Hemos definido una clase `Book` que implementa el protocolo `Printable` proporcionando una implementación del método `__str__`. Ahora podemos anotar una variable `book` como un objeto `Printable`.

### Usando el Protocolo

```python
def print_info(item: Printable) -> None:
    print(str(item))

print_info(book)
```

La función `print_info` toma un argumento `item` de tipo `Printable` y lo imprime. Hemos pasado nuestra instancia de `Book`, que cumple con el protocolo `Printable`, a esta función.

## Conclusiones

La biblioteca `typing` de Python es una herramienta poderosa para agregar anotaciones de tipo estático a su código, lo que lo hace más claro y ayuda a detectar errores más temprano en el ciclo de desarrollo. Con `typing`, puede anotar variables, argumentos de función, valores de retorno y estructuras de datos complejas. Además, los Protocolos PEP le permiten definir interfaces abstractas y crear código más flexible.

Al aprovechar al máximo `typing`, puede mejorar la calidad y la mantenibilidad de su código Python. A medida que explore más a fondo estas características y las incorpore en su desarrollo, estará mejor equipado para abordar proyectos más grandes y complejos.

Es importante recordar que las anotaciones de tipo son opcionales en Python, pero pueden ser muy beneficiosas en términos de claridad y detección temprana de errores. La elección de utilizar `typing` en su proyecto depende de sus necesidades y preferencias personales.

A medida que continúa su viaje en Python, siga explorando y experimentando con `typing` y los Protocolos PEP para aprovechar al máximo esta poderosa herramienta de tipado estático.