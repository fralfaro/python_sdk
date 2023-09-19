# Styling & Formatting Code


El código limpio y bien formateado es esencial para escribir programas mantenibles y colaborativos en Python. La estilización y el formateo adecuados ayudan a que el código sea más legible y fácil de entender para los desarrolladores, lo que a su vez facilita la detección y corrección de errores. En este artículo, exploraremos las mejores prácticas y herramientas para estilizar y formatear código en Python.

## Por qué es Importante el Formateo de Código

El formateo de código es importante por varias razones:

1. **Legibilidad**: Un código bien formateado es más fácil de leer y comprender, lo que facilita su mantenimiento y depuración.

2. **Consistencia**: El formateo consistente hace que el código se vea uniforme y coherente, incluso cuando es escrito por múltiples desarrolladores.

3. **Cumplimiento de Estándares**: Algunos proyectos y equipos de desarrollo tienen estándares de estilo de código que deben seguirse para garantizar la coherencia en todo el proyecto.

4. **Facilita la Colaboración**: Cuando varios desarrolladores trabajan en un proyecto, un estilo de código coherente reduce las posibilidades de conflictos y errores.

## PEP 8: La Guía de Estilo de Python

El estándar de estilo de código más ampliamente aceptado y utilizado en Python es el [PEP 8](https://www.python.org/dev/peps/pep-0008/), que es la "Propuesta de Mejora de Python" número 8. PEP 8 establece las pautas y recomendaciones para la estilización del código Python. Aquí hay algunos aspectos destacados de PEP 8:

- **Indentación**: Usar 4 espacios para la indentación. No usar tabulaciones.

- **Longitud de línea**: Las líneas no deben tener más de 79 caracteres. Para las cadenas de documentación o comentarios, el límite es de 72 caracteres.

- **Espacios en blanco**: Evitar espacios en blanco inútiles alrededor de paréntesis, corchetes y llaves. Separar las funciones y clases con dos líneas en blanco.

- **Nombres de Variables y Funciones**: Usar minúsculas con guiones bajos para los nombres de variables y funciones (snake_case). Para las clases, usar CamelCase.

- **Comentarios y Docstrings**: Usar comentarios para explicar el código cuando sea necesario. Usar docstrings para documentar funciones, clases y módulos.


## Configuración en Editores de Texto

La mayoría de los editores de texto y entornos de desarrollo populares ofrecen extensiones o plugins que pueden ayudarte a mantener el estilo de código de acuerdo con PEP 8. Algunos ejemplos incluyen:

- **Visual Studio Code**: La extensión [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) incluye opciones de formateo basadas en PEP 8. También puedes integrar Black con Visual Studio Code usando la extensión [Python Black](https://marketplace.visualstudio.com/items?itemName=ryanolsonx.python-black).

- **PyCharm**: PyCharm tiene integración nativa con PEP 8 y puede aplicar automáticamente el formateo cuando guardas un archivo.

- **Sublime Text**: Puedes instalar el plugin [SublimeLinter](http://www.sublimelinter.com/en/latest/) con [autopep8](https://pypi.org/project/autopep8/) para formatear tu código en tiempo real.


## Herramientas

### Black

**Black** es una herramienta de formateo de código que se describe a sí misma como "el formateador de código sin discusión de Python". Su objetivo principal es garantizar que el código Python sea consistente y siga un estilo de codificación predefinido. Black se enfoca en automatizar el proceso de formateo, eliminando así las discusiones sobre el estilo de código en el equipo de desarrollo.

**Características Principales**

- **Opinión Fuerte**: Black tiene una opinión fuerte sobre cómo debe formatearse el código y aplica ese estilo de manera consistente.

- **Sin Configuración**: A diferencia de algunas otras herramientas, Black no requiere configuración. Simplemente se ejecuta y formatea tu código de acuerdo con sus reglas predefinidas.

- **Reformatting**: Black puede reformatear todo tu código automáticamente, lo que lo hace ideal para proyectos existentes.

- **Integración con Editores**: Black se integra fácilmente con editores de código populares como VSCode, PyCharm y otros, lo que facilita el formateo del código en tiempo real.

**Ejemplo de Uso de Black**

Supongamos que tenemos el siguiente código desordenado en un archivo llamado `mi_script.py`:

```python
def suma(a,b):
return a+b
```

Ejecutar Black en este archivo reformateará el código automáticamente:

```python
def suma(a, b):
    return a + b
```

Para usar Black, primero debes instalarlo mediante pip:

```bash
pip install black
```

Luego, puedes ejecutar Black en un archivo o directorio de la siguiente manera:

```bash
black mi_script.py
```

### isort

**isort** es una herramienta de ordenación de importaciones en Python. Su función principal es organizar las declaraciones de importación en tu código de manera consistente y siguiendo ciertas reglas predefinidas. Mantener un orden en las importaciones facilita la lectura del código y evita problemas de importación circular.

**Características Principales**

- **Clasificación Inteligente**: isort organiza las importaciones de forma inteligente, agrupándolas en categorías como estándar, terceros y propios.

- **Configuración Personalizada**: Aunque isort viene con una configuración predefinida que funciona bien en la mayoría de los casos, también puedes personalizar las reglas de ordenación según las necesidades de tu proyecto.

- **Integración con Editores**: Al igual que Black, isort se integra fácilmente con editores populares, lo que facilita la ordenación de importaciones en tiempo real.

**Ejemplo de Uso de isort**

Supongamos que tenemos un archivo llamado `mi_script.py` con importaciones desordenadas:

```python
import os
import sys
import math
import requests
```

Ejecutar isort en este archivo organizará las importaciones:

```python
import math
import os
import sys

import requests
```

Para usar isort, primero debes instalarlo mediante pip:

```bash
pip install isort
```

Luego, puedes ejecutar isort en un archivo o directorio de la siguiente manera:

```bash
isort mi_script.py
```

### Flake8

**Flake8** es una herramienta de verificación de código estático que se encarga de buscar problemas de estilo y errores en el código Python. A diferencia de Black e isort, Flake8 no formatea el código, pero te ayuda a identificar problemas potenciales.

**Características Principales**

- **Verificación de Estilo**: Flake8 verifica que tu código siga las convenciones de estilo de Python, como la PEP 8.

- **Detección de Errores**: Flake8 detecta errores en el código, como variables no utilizadas, importaciones no utilizadas y más.

- **Personalización**: Puedes personalizar las reglas y configuraciones de Flake8 según las necesidades de tu proyecto.

**Ejemplo de Uso de Flake8**

Supongamos que tenemos un archivo llamado `mi_script.py` con algunas violaciones de estilo y errores:

```python
def suma(a,b):
return a+b

result = suma(3, 4)
print(result)

unused_variable = 42
```

Ejecutar Flake8 en este archivo mostrará mensajes de error y advertencias:

```
mi_script.py:1:1: E302 expected 2 blank lines, found 1
mi_script.py:1:9: E231 missing whitespace after ','
mi_script.py:2:1: E305 expected 2 blank lines after function or class definition, found 1
mi_script.py:3:5: E701 multiple statements on one line (colon)
mi_script.py:6:1: F841 local variable 'unused_variable' is assigned to but never used
```

Para usar Flake8, primero debes instalarlo mediante pip:

```bash
pip install flake8
```



Luego, puedes ejecutar Flake8 en un archivo o directorio de la siguiente manera:

```bash
flake8 mi_script.py
```

### pyupgrade

**pyupgrade** es una herramienta
poderosa que te permite actualizar automáticamente el código Python a una versión más reciente del lenguaje. Esto es útil para aprovechar las características más recientes de Python, hacer que tu código sea más limpio y legible, y asegurarte de que estés utilizando las mejores prácticas.

**Motivos para Usar pyupgrade**

Existen varias razones para utilizar pyupgrade en tus proyectos de Python:

1. **Mantener el Código Actualizado**: Python está en constante evolución, y cada nueva versión trae consigo mejoras y características nuevas. Al mantener tu código actualizado, puedes aprovechar estas mejoras y mantenerlo en línea con las últimas prácticas recomendadas.

2. **Mejorar la Legibilidad**: pyupgrade puede realizar cambios que mejoran la legibilidad del código. Por ejemplo, puede convertir el uso de `str.format()` en f-strings, lo que hace que las cadenas de formato sean más claras y concisas.

3. **Eliminar Obsolescencias**: Python introduce obsolescencias (deprecations) en versiones posteriores para indicar que ciertas características o bibliotecas ya no se recomiendan. pyupgrade puede ayudarte a eliminar esas obsolescencias de manera automática.

4. **Estándares de Código**: pyupgrade puede ayudarte a cumplir con los estándares de código de Python y seguir las pautas de estilo recomendadas.

**Ejemplos de Actualizaciones Realizadas por pyupgrade**

A continuación, se presentan algunos ejemplos de actualizaciones que pyupgrade puede realizar en tu código:

**1.- Set Literals**

En versiones recientes de Python, se introdujo una sintaxis más concisa para definir conjuntos (sets) llamada "set literals". pyupgrade puede convertir las definiciones de conjuntos obsoletas en set literals más legibles.

**Antes**:

```python
my_set = set([1, 2, 3])
```

**Después**:

```python
my_set = {1, 2, 3}
```

**2.- Dictionary Comprehensions**

Python admite "dictionary comprehensions" que permiten crear diccionarios de manera más eficiente y legible que utilizando bucles. pyupgrade puede actualizar las construcciones de diccionarios obsoletas a "dictionary comprehensions".

**Antes**:

```python
my_dict = {}
for i in range(5):
    my_dict[i] = i * i
```

**Después**:

```python
my_dict = {i: i * i for i in range(5)}
```

**3.- Format Specifiers**

Las "f-strings" introducidas en Python 3.6 ofrecen una forma más concisa y legible de formatear cadenas. pyupgrade puede convertir las llamadas a `str.format()` en f-strings.

**Antes**:

```python
name = "Alice"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
```

**Después**:

```python
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
```

Estos son solo algunos ejemplos de las actualizaciones que pyupgrade puede realizar. La herramienta es altamente configurable y puede adaptarse a las necesidades de tu proyecto específico.

**Uso de pyupgrade**

Para utilizar pyupgrade, primero debes instalarlo mediante pip:

```bash
pip install pyupgrade
```

Luego, puedes ejecutar pyupgrade en un archivo o directorio de la siguiente manera:

```bash
pyupgrade your_file.py
```

pyupgrade analizará el código en busca de oportunidades de actualización y realizará las modificaciones necesarias. Asegúrate de revisar los cambios realizados por pyupgrade para garantizar que el código siga funcionando como se esperaba.

En resumen, pyupgrade es una herramienta valiosa para mantener tu código Python actualizado y en línea con las últimas mejores prácticas del lenguaje. Puede ahorrarte tiempo y esfuerzo al automatizar las actualizaciones y mejoras de código, lo que te permite concentrarte en el desarrollo de nuevas características y funcionalidades.

