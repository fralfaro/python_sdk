# Makefile

El Makefile es una herramienta poderosa y versátil utilizada 
en el desarrollo de software para automatizar procesos de compilación y construcción de proyectos.

## Orígenes del Makefile

El concepto de Makefile se originó en la década de 1970 en los laboratorios Bell,
donde se desarrolló el lenguaje de programación C y el sistema operativo Unix.

Stuart Feldman creó la primera versión de la utilidad "make" para automatizar el proceso de 
compilación de programas C. Desde entonces, "make" se ha convertido en una herramienta estándar 
en sistemas Unix y se ha extendido a otros sistemas operativos.

## Por Qué Debería Utilizarse un Makefile

### 1. **Automatización de Tareas:**
   Un Makefile permite automatizar tareas repetitivas de compilación y construcción. Esto ahorra tiempo y reduce la posibilidad de errores humanos al realizar estas tareas manualmente.

### 2. **Gestión de Dependencias:**
   Define las dependencias entre archivos fuente y archivos objeto, garantizando que los archivos se compilen en el orden correcto y solo cuando sea necesario.

### 3. **Portabilidad:**
   Los Makefiles son compatibles con una variedad de plataformas y entornos de desarrollo, lo que facilita la portabilidad de proyectos entre sistemas.

### 4. **Mantenimiento Sencillo:**
   Los Makefiles son fáciles de mantener y actualizar a medida que cambian los requisitos del proyecto.

## Ejemplos en Python

Supongamos que tenemos un proyecto Python simple con dos archivos: `main.py` y `util.py`. Queremos crear un Makefile para compilar y ejecutar el proyecto.

### 1. Creación del Makefile

Primero, creamos un archivo llamado `Makefile` en la raíz de nuestro proyecto. Este es el contenido inicial:

```make
# Makefile para proyecto Python

.PHONY: all run clean

all: main

main: main.py util.py
    python3 main.py

clean:
    rm -f main
```

- `.PHONY` es una directiva especial que indica a Make que los objetivos `all`, `run` y `clean` no representan archivos reales.
- `all` es el objetivo predeterminado que se construirá cuando ejecutemos `make` sin argumentos.
- `main` es el objetivo para compilar y ejecutar nuestro programa.
- `clean` es un objetivo para eliminar el archivo ejecutable generado.

### 2. Compilación y Ejecución

Ejecutamos los siguientes comandos en la terminal:

- `make` o `make all`: Compila y ejecuta el programa.
- `make clean`: Elimina el archivo ejecutable.

### 3. Personalización del Makefile

Si deseamos agregar más archivos fuente o cambiar las opciones de compilación, podemos modificar fácilmente el Makefile para reflejar estos cambios.

```make
# Makefile para proyecto Python

.PHONY: all run clean

all: main

main: main.py util.py helper.py
    python3 main.py

clean:
    rm -f main
```

En este ejemplo, hemos agregado un archivo `helper.py` y lo hemos incluido como una dependencia en la regla `main`. Esto asegura que se recompile si se modifican los archivos fuente relacionados.

### 4. Ejemplo avanzado 

Tenemos el siguiente Makefile:

```make
# Makefile para proyecto Python con precommit hooks, pytest y documentación

.PHONY: all clean lint test docs

all: clean lint test docs

clean:
    @echo "Limpiando archivos temporales..."
    rm -rf build dist *.egg-info
    find . -type d -name '__pycache__' -exec rm -rf {} +
    find . -type f -name '*.pyc' -exec rm -f {} +
    @echo "Limpieza completa."

lint:
    @echo "Ejecutando linters (flake8 y black)..."
    flake8 . --exclude=__init__.py
    black . --check --exclude=__init__.py
    @echo "Linters completados."

test:
    @echo "Ejecutando pruebas con pytest..."
    pytest
    @echo "Pruebas completadas."

docs:
    @echo "Generando documentación con mkdocs..."
    mkdocs build
    @echo "Documentación generada."
```

Explicaremos detalladamente cada parte del código del Makefile:

1. **Objetivos y Reglas:**
   
   ```make
   .PHONY: all clean lint test docs precommit
   ```
   
   - `.PHONY` es una directiva especial que le dice a Make que estos objetivos no representan archivos reales, sino tareas a realizar.

2. **Objetivo `all`:**

   ```make
   all: clean lint test docs
   ```

   - `all` es el objetivo predeterminado que se construirá cuando ejecutes `make` sin argumentos.
   - Este objetivo depende de otros objetivos: `clean`, `lint`, `test`, y `docs`. Cuando se ejecuta `make all`, se ejecutarán estos objetivos en ese orden.

3. **Objetivo `clean`:**

   ```make
   clean:
       @echo "Limpiando archivos temporales..."
       rm -rf build dist *.egg-info
       find . -type d -name '__pycache__' -exec rm -rf {} +
       find . -type f -name '*.pyc' -exec rm -f {} +
       @echo "Limpieza completa."
   ```

   - Este objetivo se utiliza para eliminar archivos temporales y limpiar el directorio del proyecto.
   - Usa el comando `rm` para eliminar los directorios `build`, `dist`, y los archivos `.egg-info`.
   - Luego, utiliza el comando `find` para buscar y eliminar todos los directorios `__pycache__` y archivos `.pyc`, que son generados por Python.

4. **Objetivo `lint`:**

   ```make
   lint:
       @echo "Ejecutando linters (flake8 y black)..."
       flake8 . --exclude=__init__.py
       black . --check --exclude=__init__.py
       @echo "Linters completados."
   ```

   - Este objetivo se utiliza para ejecutar linters, en este caso, `flake8` y `black`, que verifican el estilo y formato del código Python.
   - `flake8` se utiliza para verificar el estilo del código en el proyecto, y se excluye el archivo `__init__.py` del análisis.
   - `black` se utiliza en modo de comprobación (`--check`) para verificar si el código cumple con las reglas de formato definidas por `black`. `black` no realiza cambios en el código, solo informa sobre las discrepancias.

5. **Objetivo `test`:**

   ```make
   test:
       @echo "Ejecutando pruebas con pytest..."
       pytest
       @echo "Pruebas completadas."
   ```

   - Este objetivo se utiliza para ejecutar pruebas automatizadas en el proyecto utilizando `pytest`.
   - `pytest` busca y ejecuta todas las pruebas en el proyecto y muestra los resultados en la terminal.

6. **Objetivo `docs`:**

   ```make
   docs:
       @echo "Generando documentación con mkdocs..."
       mkdocs build
       @echo "Documentación generada."
   ```

   - Este objetivo se utiliza para generar la documentación del proyecto utilizando `mkdocs`.
   - `mkdocs build` compila la documentación y genera los archivos HTML y otros recursos necesarios para la documentación.


## Uso del Repositorio "makefiletutorial" 

El repositorio [theicfire/makefiletutorial](https://github.com/theicfire/makefiletutorial)
es una valiosa fuente de información y recursos para aquellos que desean aprender más sobre
Makefiles y cómo utilizarlos de manera efectiva en proyectos de desarrollo de software. 

### Contenido del Repositorio

El repositorio "makefiletutorial" contiene una serie de recursos, tutoriales y ejemplos relacionados con el uso de Makefiles en proyectos de desarrollo de software. Algunos de los elementos clave incluyen:

1. **Documentación Detallada:** El repositorio proporciona documentación detallada sobre cómo crear y utilizar Makefiles. Esto incluye explicaciones sobre la estructura de un Makefile, reglas, objetivos, dependencias y comandos comunes utilizados en Makefiles.

2. **Ejemplos Prácticos:** Se incluyen ejemplos prácticos de Makefiles que cubren una variedad de casos de uso. Estos ejemplos muestran cómo utilizar Makefiles para compilar, construir, ejecutar pruebas y realizar otras tareas comunes en el desarrollo de software.

3. **Recursos Complementarios:** El repositorio también puede proporcionar enlaces a recursos adicionales relacionados con Makefiles, como libros, artículos y otras fuentes de información útiles.

### Importancia de Utilizar el Repositorio

El repositorio "makefiletutorial" es importante por varias razones:

1. **Aprendizaje Accesible:** Proporciona una forma accesible para que desarrolladores de todos los niveles de experiencia aprendan sobre el uso de Makefiles. Los tutoriales y ejemplos se presentan de manera clara y estructurada.

2. **Eficiencia en el Desarrollo:** Al dominar el uso de Makefiles, los desarrolladores pueden automatizar tareas repetitivas de construcción, compilación y pruebas, lo que aumenta la eficiencia y reduce la posibilidad de errores humanos en el proceso de desarrollo de software.

3. **Portabilidad y Estandarización:** Utilizar Makefiles en proyectos facilita la portabilidad del código entre diferentes sistemas operativos y entornos de desarrollo. Además, promueve la estandarización de prácticas de construcción y compilación en equipos de desarrollo.

4. **Alineación con Buenas Prácticas:** Aprender a utilizar Makefiles a través de este repositorio puede ayudar a los desarrolladores a alinearse con las mejores prácticas de desarrollo de software y mejorar la calidad de sus proyectos.

5. **Flexibilidad y Personalización:** Los Makefiles pueden adaptarse a las necesidades específicas de un proyecto, lo que brinda a los desarrolladores la flexibilidad para crear flujos de trabajo de desarrollo personalizados.

