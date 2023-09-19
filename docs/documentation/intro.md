# Documentación en Python: Mejores Prácticas y Herramientas

La documentación es una parte fundamental del desarrollo de software. Proporciona información esencial para los desarrolladores, usuarios y colaboradores sobre cómo utilizar y contribuir a un proyecto. En Python, existen buenas prácticas y herramientas que hacen que la creación y mantenimiento de la documentación sea más fácil y efectiva. En este artículo, exploraremos la importancia de la documentación, los diferentes estilos de docstrings y dos de las principales herramientas de documentación en Python: Sphinx y Markdown.

## Importancia de la Documentación

La documentación es una forma de comunicación clave en el desarrollo de software. Proporciona claridad y contexto sobre el propósito, el funcionamiento y el uso de un proyecto. Algunas de las razones por las que la documentación es importante incluyen:

- **Facilita el Uso**: Permite a los usuarios comprender cómo usar una biblioteca o aplicación sin necesidad de leer el código fuente.
- **Colaboración Eficiente**: Ayuda a los colaboradores a comprender cómo contribuir al proyecto y a mantener un estándar común.
- **Resolución de Problemas**: Facilita la solución de problemas al proporcionar información sobre errores comunes y ejemplos de uso.
- **Mantenimiento Sostenible**: Permite que un proyecto sea mantenible a lo largo del tiempo, incluso si los desarrolladores originales ya no están disponibles.

## Docstrings 

Los docstrings en Python son
cadenas de documentación que se
utilizan para describir el propósito y el funcionamiento de módulos, clases, funciones y métodos en el código. Estas cadenas de documentación proporcionan una forma de comunicar de manera efectiva cómo se debe utilizar y entender una pieza de software. En este artículo, exploraremos en detalle los docstrings en Python, incluyendo los diferentes estilos de docstrings y su importancia.

### ¿Qué Son los Docstrings?

Los docstrings son simplemente cadenas de texto que se colocan en la parte superior de un módulo, clase, función o método en Python. Estas cadenas de texto se utilizan para documentar el código y proporcionar información sobre lo que hace ese código, cómo debe usarse y qué argumentos se esperan.

En Python, los docstrings son tratados como literales de cadena y se asignan automáticamente al atributo `__doc__` de un objeto. Esto significa que puedes acceder a la cadena de documentación de cualquier objeto en Python utilizando la notación de punto, por ejemplo, `objeto.__doc__`.

### Estilos de Docstrings

Existen varios estilos y convenciones para escribir docstrings en Python. Los dos estilos de docstrings más comunes son:

#### 1. Estilo de una Línea

Este estilo es adecuado para documentar módulos, clases, funciones o métodos muy simples en una sola línea. Generalmente, se coloca entre comillas triples (simples o dobles) y se coloca inmediatamente debajo de la definición del objeto.

```python
def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b
```

#### 2. Estilo de Múltiples Líneas

Este estilo se utiliza para proporcionar una documentación más detallada y estructurada. Sigue las convenciones de las PEP 257. Aquí hay un ejemplo:

```python
def divide(dividendo, divisor):
    """
    Divide el dividendo entre el divisor y devuelve el resultado.

    Args:
        dividendo (int): El número que se divide.
        divisor (int): El número por el cual se divide.

    Returns:
        float: El resultado de la división.

    Raises:
        ValueError: Si el divisor es igual a cero.
    """
    if divisor == 0:
        raise ValueError("No se puede dividir por cero.")
    return dividendo / divisor
```

En el ejemplo anterior:

- La sección **Args** describe los argumentos que la función espera y sus tipos.
- La sección **Returns** describe el valor de retorno de la función y su tipo.
- La sección **Raises** enumera las excepciones que puede generar la función.

###  Formatos principales de docstrings

#### NumPy/SciPy Docstrings
   
   Los docstrings de estilo NumPy/SciPy siguen las convenciones utilizadas en las bibliotecas NumPy y SciPy, que son ampliamente utilizadas en la comunidad científica de Python. Estos docstrings están diseñados para proporcionar una documentación clara y concisa para funciones y clases que trabajan con matrices multidimensionales y operaciones matemáticas.

   - **Ejemplo:**

     ```python
     def matrix_multiply(matrix1, matrix2):
         """
         Multiply two matrices element-wise.

         Parameters:
             matrix1 (numpy.ndarray): The first input matrix.
             matrix2 (numpy.ndarray): The second input matrix.

         Returns:
             numpy.ndarray: The result of element-wise multiplication.
         """
     ```

#### Google Docstrings

   Los docstrings de estilo Google siguen las convenciones de documentación utilizadas por Google para documentar su código en Python. Este formato se centra en proporcionar una documentación clara y legible utilizando un estilo de lenguaje natural. Incluye secciones específicas para describir parámetros, valores de retorno y ejemplos.

   - **Ejemplo:**

     ```python
     def calculate_area(length, width):
         """
         Calculate the area of a rectangle.

         Args:
             length (float): The length of the rectangle.
             width (float): The width of the rectangle.

         Returns:
             float: The area of the rectangle.
         """
     ```

#### reStructuredText

   reStructuredText (reST) es un formato de marcado utilizado para escribir documentación estructurada en Python. Se utiliza en combinación con herramientas como Sphinx para generar documentación de alta calidad a partir de docstrings y archivos de texto en formato reST. Este formato es particularmente popular en proyectos de código abierto y bibliotecas bien documentadas.

   - **Ejemplo:**

     ```python
     def calculate_volume(length, width, height):
         """
         Calculate the volume of a rectangular prism.

         :param float length: The length of the prism.
         :param float width: The width of the prism.
         :param float height: The height of the prism.
         :return: The volume of the prism.
         :rtype: float
         """
     ```

#### Epytext

   Epytext es un formato de marcado diseñado específicamente para documentar código Python. Aunque no es tan ampliamente utilizado como los otros formatos, es una opción válida para documentar funciones y clases en Python. Epytext utiliza etiquetas especiales para describir parámetros, valores de retorno y otros elementos de la documentación.

   - **Ejemplo:**

     ```python
     def calculate_perimeter(side1, side2):
         """
         Calculate the perimeter of a rectangle.

         @param side1: The length of one side of the rectangle.
         @type side1: float
         @param side2: The length of the adjacent side of the rectangle.
         @type side2: float
         @return: The perimeter of the rectangle.
         @rtype: float
         """
     ```

