# Programación Orientada a Objetos

La programación orientada a objetos (POO) 
en Python es un enfoque de programación que se basa en la creación y manipulación de objetos.

Para comprender la POO en Python, es fundamental conocer los conceptos básicos relacionados con las clases, los objetos, los constructores y los métodos. En este artículo, exploraremos en detalle estos conceptos fundamentales con ejemplos prácticos.

## Clases y Objetos en Python

### Clases

Una clase es una plantilla o un plano para crear objetos. Define las propiedades (atributos) y los comportamientos (métodos) que los objetos creados a partir de ella tendrán. En Python, se define una clase utilizando la palabra clave `class`.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
```

En este ejemplo, hemos definido una clase `Persona` con un constructor `__init__` y un método `saludar`.

### Objetos

Un objeto es una instancia específica de una clase. 
Se crea un objeto llamando al constructor de la clase. Los objetos tienen sus propios valores para los atributos y pueden llamar a los métodos de la clase.

```python
juan = Persona("Juan", 30)
maria = Persona("Maria", 25)

print(juan.saludar())  # Output: Hola, soy Juan y tengo 30 años.
print(maria.saludar()) # Output: Hola, soy Maria y tengo 25 años.
```

En este ejemplo, `juan` y `maria` son objetos de la clase `Persona`, cada uno con sus propios valores para `nombre` y `edad`.

## Constructores en Python

### Constructor `__init__`

El constructor es un método especial en Python que se llama automáticamente cuando se crea un objeto de una clase. En la mayoría de los casos, se llama `__init__`. Recibe `self` como primer parámetro, que se refiere al objeto en sí. El constructor se utiliza para inicializar los atributos de un objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

En este ejemplo, el constructor `__init__` toma dos parámetros (`nombre` y `edad`) y los utiliza para inicializar los atributos `self.nombre` y `self.edad`.

### Otros Constructores

Aunque `__init__` es el constructor más común, Python permite definir otros constructores utilizando el método especial `__new__`. Sin embargo, esto es menos común y no se utiliza con frecuencia en la programación cotidiana.

## Atributos de Clase y de Instancias

### Atributos de Clase

Los atributos de clase son compartidos entre todas las instancias de una clase. Se definen directamente en la clase y no en un método del objeto. Un ejemplo de un atributo de clase podría ser un contador que rastrea el número de instancias creadas de una clase. Aquí hay un ejemplo:

```python
class Coche:
    contador = 0  # Atributo de clase

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Coche.contador += 1  # Incrementar el contador en cada creación de objeto

    def obtener_informacion(self):
        return f"{self.marca} {self.modelo}"

# Uso de la clase Coche
coche1 = Coche("Toyota", "Camry")
coche2 = Coche("Honda", "Accord")
print(f"Total de coches creados: {Coche.contador}")
```

- `contador` es un atributo de clase que se incrementa cada vez que se crea un objeto de la clase `Coche`.

### Atributos de Instancia

Los atributos de instancia son específicos de cada objeto y se definen en el constructor de la clase. Cada objeto tiene su propio conjunto de valores para estos atributos. En el ejemplo anterior, `marca` y `modelo` son atributos de instancia.

```python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo de instancia
        self.modelo = modelo  # Atributo de instancia
```


## Métodos en Python

### Métodos de Instancia

Los métodos de instancia son funciones definidas dentro de una clase que operan en los atributos de un objeto específico. Los métodos de instancia toman `self` como su primer parámetro, que se refiere al objeto en sí.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."
```

En este ejemplo, `saludar()` es un método de instancia que opera en los atributos `nombre` y `edad` del objeto.

### Métodos Estáticos

Los métodos estáticos son funciones definidas en una clase que no toman `self` como parámetro y no operan en atributos de objeto específicos. Se utilizan para funcionalidades relacionadas con la clase en su conjunto.

```python
class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b
```

En este ejemplo, `sumar()` es un método estático de la clase `Calculadora` que no requiere la creación de un objeto para ser utilizado.

### Métodos de Clase

Los métodos de clase son funciones definidas en una clase que operan en atributos de clase en lugar de atributos de objeto específicos. Se utilizan con el decorador `@classmethod` y toman `cls` como su primer parámetro, que se refiere a la clase en sí.

```python
class Coche:
    total_coches = 0

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        Coche.total_coches += 1

    @classmethod
    def total(cls):
        return cls.total_coches
```

En este ejemplo, `total()` es un método de clase que accede al atributo de clase `total_coches`.


## Principios Fundamentales 

### 1. Encapsulación

La encapsulación es el principio de POO que se refiere a la ocultación de los detalles internos de un objeto y la exposición de una interfaz pública para interactuar con él. En Python, la encapsulación se implementa utilizando modificadores de acceso como `_`, `__`, y `@property`.

**Ejemplo de Encapsulación**

```python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido
        self.__edad = edad  # Atributo privado

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad

# Crear una instancia de Persona
persona = Persona("Alice", 30)

# Acceder a atributos protegidos y privados
print(persona.get_nombre())  # Salida: Alice
print(persona.edad)  # Salida: 30

# Modificar atributos protegidos y privados
persona.set_nombre("Bob")
persona.edad = 25

# No se recomienda acceder a atributos privados desde fuera de la clase, pero es posible
print(persona._nombre)  # Salida: Bob
print(persona._Persona__edad)  # Salida: 25
```

### 2. Abstracción

La abstracción es el proceso de simplificar la realidad enfocándonos en los detalles esenciales y ocultando los detalles no esenciales. En POO, las clases y objetos son abstracciones del mundo real.

**Ejemplo de Abstracción**

```python
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        pass

class Coche(Vehiculo):
    def conducir(self):
        return f"Conduciendo {self.marca} {self.modelo} a 100 km/h"

class Motocicleta(Vehiculo):
    def conducir(self):
        return f"Conduciendo {self.marca} {self.modelo} a 80 km/h"

# Crear instancias de Coche y Motocicleta
mi_coche = Coche("Toyota", "Corolla")
mi_moto = Motocicleta("Honda", "CBR")

# Utilizar el método conducir
print(mi_coche.conducir())  # Salida: Conduciendo Toyota Corolla a 100 km/h
print(mi_moto.conducir())   # Salida: Conduciendo Honda CBR a 80 km/h
```

### 3. Herencia

La herencia es un principio que permite que una clase herede atributos y métodos de otra clase, lo que promueve la reutilización de código y la creación de jerarquías de clases.

**Ejemplo de Herencia**

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

# Crear instancias de Perro y Gato
mi_perro = Perro("Fido")
mi_gato = Gato("Garfield")

# Llamar al método hacer_sonido
print(mi_perro.hacer_sonido())  # Salida: Guau
print(mi_gato.hacer_sonido())   # Salida: Miau
```

### 4. Polimorfismo

El polimorfismo permite que objetos de diferentes clases respondan de manera diferente a los mismos métodos, lo que facilita la flexibilidad en el diseño de programas.

**Ejemplo de Polimorfismo**

```python
def hacer_sonar_animal(animal):
    return animal.hacer_sonido()

# Crear instancias de Perro y Gato
mi_perro = Perro("Fido")
mi_gato = Gato("Garfield")

# Utilizar la función hacer_sonar_animal con diferentes objetos
print(hacer_sonar_animal(mi_perro))  # Salida: Guau
print(hacer_sonar_animal(mi_gato))   # Salida: Miau
```


