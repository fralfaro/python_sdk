# S.O.L.I.D.

Los Principios SOLID son un conjunto de cinco principios de
diseño de software que fueron introducidos por Robert C. Martin 
(también conocido como Uncle Bob) en la década de 1990. Estos principios se
han convertido en una guía fundamental para escribir código limpio, mantenible y 
flexible en la programación orientada a objetos (POO). A continuación, exploraremos 
en detalle cada uno de los principios SOLID, su origen y cómo se adaptan a diferentes 
lenguajes de programación, incluido Python.

### 1. Principio de Responsabilidad Única (Single Responsibility Principle - SRP)

**Origen**: El SRP fue propuesto por primera vez por Robert C. Martin en su libro "Agile Software Development, Principles, Patterns, and Practices" en 2003. Este principio se basa en la idea de que una clase debe tener una única razón para cambiar, es decir, una sola responsabilidad. La motivación detrás de este principio es reducir la complejidad y aumentar la cohesión en el diseño del software.

**Adaptación en Python**: En Python, el SRP se aplica de manera similar a otros lenguajes. Se busca identificar las responsabilidades de una clase y, si tiene más de una, dividirlas en clases separadas. Python permite lograr esto fácilmente gracias a su flexibilidad en la definición de clases y la capacidad de componer clases pequeñas y específicas.

**Ejemplo SRP en Python**

Supongamos que tenemos una clase `Empleado` que maneja tanto la información del empleado como la generación de informes. Esto violaría el SRP. En su lugar, podríamos dividirlo en dos clases:

```python
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class GeneradorInforme:
    @staticmethod
    def generar_informe(empleado):
        # Lógica para generar el informe
        pass
```

Al dividir las responsabilidades, facilitamos la modificación y el mantenimiento de cada clase por separado.


### 2. Principio Abierto/Cerrado (Open/Closed Principle - OCP)

**Origen**: El OCP fue formulado por Bertrand Meyer en su libro "Object-Oriented Software Construction" en 1988 y posteriormente adoptado en los principios SOLID por Uncle Bob. Este principio establece que las entidades de software (clases, módulos, etc.) deben estar abiertas para la extensión pero cerradas para la modificación. En otras palabras, se debe poder agregar nueva funcionalidad sin cambiar el código existente.

**Adaptación en Python**: Python permite aplicar el OCP mediante técnicas de herencia y polimorfismo. Al diseñar clases y módulos de manera que sean fáciles de extender, los desarrolladores pueden agregar nuevas características sin alterar el código existente. Además, Python fomenta la creación de interfaces y abstracciones, lo que facilita la extensión.

**Ejemplo OCP en Python**

Supongamos que tenemos una clase `Calculadora` que realiza operaciones matemáticas básicas. En lugar de modificar la clase cada vez que necesitemos agregar una nueva operación, podemos extenderla:

```python
class Calculadora:
    def calcular(self, operacion, a, b):
        if operacion == 'suma':
            return a + b
        elif operacion == 'resta':
            return a - b
        # Más operaciones...

# Extender la clase para agregar una nueva operación
class CalculadoraAvanzada(Calculadora):
    def calcular(self, operacion, a, b):
        if operacion == 'multiplicacion':
            return a * b
        # Otras operaciones avanzadas...
```

Al extender la clase en lugar de modificarla, mantenemos la clase original cerrada para modificaciones y abierta para extensiones.

### 3. Principio de Sustitución de Liskov (Liskov Substitution Principle - LSP)

**Origen**: El LSP lleva el nombre de Barbara Liskov, quien formuló este principio en 1987. El LSP establece que los objetos de una subclase deben poder reemplazar sin problemas a los objetos de la clase base sin afectar la integridad del programa. Este principio garantiza la coherencia en la jerarquía de clases.

**Adaptación en Python**: En Python, el LSP se aplica respetando las interfaces y asegurando que las subclases cumplan con las expectativas de las clases base. Aunque Python no tiene tipado estático, sigue siendo importante diseñar clases y métodos de manera que las subclases puedan ser usadas sin problemas donde se esperan objetos de la clase base.

**Ejemplo LSP en Python**

Supongamos que tenemos una clase base `Ave` y una subclase `Avestruz`. Según el LSP, deberíamos poder tratar una avestruz como un ave sin problemas:

```python
class Ave:
    def volar(self):
        pass

class Avestruz(Ave):
    def volar(self):
        raise Exception("Las avestruces no pueden volar")
```

Aunque las avestruces no pueden volar, la subclase `Avestruz` aún cumple con la interfaz
definida por la clase base `Ave`, evitando problemas inesperados en el código que usa objetos de tipo `Ave`.


### 4. Principio de Segregación de Interfaces (Interface Segregation Principle - ISP)

**Origen**: El ISP también fue introducido por Uncle Bob como parte de los principios SOLID. Este principio se basa en la idea de que las interfaces deben ser pequeñas y específicas. En lugar de tener interfaces grandes y complejas, se deben crear múltiples interfaces específicas para cada cliente.

**Adaptación en Python**: Aunque Python no tiene interfaces formales como algunos lenguajes estáticos, se puede aplicar el ISP dividiendo las responsabilidades en clases o mixins específicos. Python permite componer objetos de manera flexible, lo que facilita la implementación de interfaces segregadas.
**Ejemplo ISP en Python**

Supongamos que tenemos una interfaz `Trabajador` que define métodos para trabajar en diferentes tareas. En lugar de tener una

 sola interfaz grande, podemos dividirla en interfaces más pequeñas y específicas:

```python
class Trabajador:
    def trabajar(self):
        pass

class TrabajadorManual(Trabajador):
    def trabajar(self):
        # Realizar trabajo manual
        pass

class TrabajadorOficina(Trabajador):
    def trabajar(self):
        # Realizar trabajo de oficina
        pass
```

De esta manera, las clases que implementan `TrabajadorManual` no están obligadas a implementar métodos relacionados con el trabajo de oficina.

### 5. Principio de Inversión de Dependencia (Dependency Inversion Principle - DIP)

**Origen**: El DIP es otro principio propuesto por Uncle Bob. Este principio establece que los módulos de alto nivel no deben depender de módulos de bajo nivel, sino que ambos deben depender de abstracciones. Además, las abstracciones no deben depender de detalles, sino que los detalles deben depender de abstracciones.

**Adaptación en Python**: Python facilita la inversión de dependencias mediante la inyección de dependencias y la programación orientada a objetos. Los desarrolladores pueden diseñar sus clases de manera que dependan de abstracciones en lugar de implementaciones concretas, lo que facilita la sustitución y la prueba de componentes.

**Ejemplo DIP en Python**

Supongamos que tenemos una clase `Luz` que depende de una clase `Interruptor`. Siguiendo el DIP, podemos invertir la dependencia mediante el uso de abstracciones:

```python
from abc import ABC, abstractmethod

class Interruptor(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class Luz:
    def __init__(self, interruptor: Interruptor):
        self.interruptor = interruptor

    def encender(self):
        self.interruptor.encender()

    def apagar(self):
        self.interruptor.apagar()

class InterruptorPared(Interruptor):
    def encender(self):
        # Lógica para encender el interruptor de pared
        pass

    def apagar(self):
        # Lógica para apagar el interruptor de pared
        pass
```

Ahora, la clase `Luz` depende de la abstracción `Interruptor`, y diferentes tipos de interruptores pueden implementar esa abstracción sin afectar la clase `Luz`.


Supongamos que tenemos una clase `Luz` que depende de una clase `Interruptor`. Siguiendo el DIP, podemos invertir la dependencia mediante el uso de abstracciones:

```python
from abc import ABC, abstractmethod

class Interruptor(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class Luz:
    def __init__(self, interruptor: Interruptor):
        self.interruptor = interruptor

    def encender(self):
        self.interruptor.encender()

    def apagar(self):
        self.interruptor.apagar()

class InterruptorPared(Interruptor):
    def encender(self):
        # Lógica para encender el interruptor de pared
        pass

    def apagar(self):
        # Lógica para apagar el interruptor de pared
        pass
```

Ahora, la clase `Luz` depende de la abstracción `Interruptor`, y diferentes tipos de interruptores pueden implementar esa abstracción sin afectar la clase `Luz`.

## Conclusiones

En resumen, los principios SOLID son fundamentales para el diseño de software robusto y se pueden aplicar de manera efectiva en Python y otros lenguajes de programación. Estos principios promueven la modularidad, la flexibilidad y la mantenibilidad del código, lo que es esencial para desarrollar aplicaciones de alta calidad en cualquier lenguaje. Al comprender y aplicar estos principios, los desarrolladores pueden escribir software más limpio y menos propenso a errores.