# Poetry: Gestión de Dependencias 

[Poetry](https://python-poetry.org/) es una herramienta revolucionaria para la gestión de dependencias y el empaquetado en Python. Con Poetry, declarar las bibliotecas en las que tu proyecto depende es sencillo, y Poetry se encargará de administrar la instalación y actualización de esas dependencias por ti.

## Instalación de Poetry

Para instalar Poetry de forma aislada y segura en tu sistema, sigue estos pasos:

### macOS / Linux / bash en Windows
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

### Windows PowerShell
```bash
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

## Creación de un Proyecto con Poetry

Poetry no solo facilita la gestión de dependencias, sino que también agiliza la estructuración de proyectos Python. Puedes crear un nuevo proyecto desde cero de la siguiente manera:

```bash
poetry new poetry-tutorial-project
```

Esta simple línea de comandos generará una estructura de carpetas estándar para tu proyecto, incluyendo un archivo `pyproject.toml`, que es fundamental en la configuración de tu proyecto.

### Configuración Centralizada

El archivo `pyproject.toml` es el núcleo de la configuración de tu proyecto con Poetry. Puedes definir metadatos, dependencias, scripts y más en este archivo. A continuación, mostramos un ejemplo completo:

```toml
[tool.poetry]
name = "poetry_tutorial_project"
version = "0.1.0"
description = "Simple Python project built with Poetry."
authors = ["Todd Birchard <toddbirchard@gmail.com>"]
maintainers = ["Todd Birchard <toddbirchard@gmail.com>"]
license = "MIT"
readme = "README.md"
homepage = ""
repository = "https://github.com/hackersandslackers/python-poetry-tutorial/"
documentation = "https://hackersandslackers.com/python-poetry/"
keywords = ["Poetry", "Virtual Environments", "Tutorial", "Packages", "Packaging"]

[tool.poetry.dependencies]
python = "^3.7"
loguru = "*"
psutil = "*"

[tool.poetry.dev-dependencies]
pytest = "*"

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"

[tool.poetry.scripts]
run = "wsgi:main"

[tool.poetry.urls]
issues = "https://github.com/hackersandslackers/python-poetry-tutorial/issues"
```

Esta configuración incluye metadatos, dependencias, scripts y enlaces útiles para tu proyecto.

**Referencia:** [Documentación oficial de Poetry - pyproject.toml](https://python-poetry.org/docs/pyproject/)

## Uso de la CLI de Poetry

La interfaz de línea de comandos (CLI) de Poetry simplifica la gestión de dependencias y la administración de proyectos. Aquí tienes algunas tareas comunes:

- **`poetry shell`**: Crea y activa un entorno virtual para tu proyecto. Esto aísla las dependencias de tu proyecto del sistema y otros proyectos.

- **`poetry install`**: Instala las dependencias especificadas en el archivo `pyproject.toml`. Las versiones reales se registran en el archivo `poetry.lock`.

- **`poetry update`**: Actualiza las dependencias de acuerdo con las versiones especificadas en `pyproject.toml`. El archivo `poetry.lock` se actualiza.

- **`poetry add [nombre-del-paquete]`**: Agrega una nueva dependencia a tu proyecto y la instala automáticamente.

- **`poetry remove [nombre-del-paquete]`**: Elimina una dependencia de tu proyecto.

- **`poetry export -f requirements.txt > requirements.txt`**: Exporta las dependencias y versiones de tu proyecto en formato `requirements.txt` para casos de uso específicos.

Poetry simplifica significativamente la gestión de dependencias y la administración de proyectos Python, lo que permite una experiencia de desarrollo más eficiente y organizada.

**Referencia:** [Documentación oficial de Poetry - Comandos](https://python-poetry.org/docs/cli/)

En resumen, Poetry es una herramienta imprescindible para el desarrollo de proyectos Python. Facilita la gestión de dependencias, la organización de proyectos y el empaquetado, simplificando muchas tareas comunes. ¡Explora más sobre Poetry y úsalo para mejorar tu flujo de trabajo de desarrollo en Python!