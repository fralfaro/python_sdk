# Pre-commit

La calidad del código es esencial en cualquier proyecto de desarrollo de software. Es importante mantener un código limpio, formateado correctamente y libre de errores para facilitar la colaboración y mantener la sostenibilidad del proyecto a largo plazo. Una herramienta valiosa que puede ayudarte a automatizar y mejorar la calidad de tu código en proyectos Python es **Pre-commit**.

## ¿Qué es Pre-commit?

**Pre-commit** es una herramienta que automatiza las verificaciones de calidad en tu repositorio de código antes de cada commit. Se integra con sistemas de control de versiones como Git y te permite configurar una serie de ganchos (hooks) que se ejecutan automáticamente antes de que se realice un commit. Estos ganchos pueden realizar diversas tareas, como formatear el código, verificar errores sintácticos, buscar problemas de estilo y más.

## Configuración Básica de Pre-commit

Para comenzar a utilizar Pre-commit en tu proyecto de Python, sigue estos pasos:

### 1. Instala Pre-commit

Puedes instalar Pre-commit utilizando pip:

```bash
pip install pre-commit
```

### 2. Crea un Archivo de Configuración

En la raíz de tu proyecto, crea un archivo llamado `.pre-commit-config.yaml`. Este archivo contendrá la configuración de Pre-commit. Aquí hay un ejemplo básico de configuración:

```yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-black
    rev: v20.8b1
    hooks:
      - id: black
```

En este ejemplo, hemos configurado un gancho para formatear el código utilizando la herramienta Black. El repositorio `https://github.com/pre-commit/mirrors-black` es un espejo de Black que Pre-commit utiliza para instalar la herramienta.

### 3. Instala los Ganchos

Ejecuta el siguiente comando para instalar los ganchos configurados en tu repositorio:

```bash
pre-commit install
```

Esto configurará Pre-commit para que se ejecute antes de cada commit.

### 4. Realiza un Commit

Ahora, cuando realices un commit en tu repositorio, Pre-commit ejecutará automáticamente el gancho que hemos configurado para formatear el código con Black. Si el código necesita cambios, Pre-commit te los mostrará y podrás realizar los cambios necesarios antes de completar el commit.

## Casos de Uso Comunes

Pre-commit es una herramienta versátil que se puede utilizar para automatizar una amplia variedad de verificaciones de calidad en proyectos Python. Aquí hay algunos casos de uso comunes:

### 1. Formateo de Código

Puedes configurar Pre-commit para que formatee automáticamente tu código antes de cada commit. Esto garantiza que el código en tu repositorio siga un estilo de codificación consistente.

### 2. Verificación de Estilo

Utiliza herramientas como Flake8 o pylint para verificar el estilo de tu código y garantizar que cumple con las convenciones de estilo de Python, como la PEP 8.

```yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-flake8
    rev: v3.9.2
    hooks:
      - id: flake8
```

### 3. Detección de Errores

Puedes configurar ganchos que ejecuten pruebas estáticas en tu código para detectar errores y problemas potenciales antes de que se realice un commit.

```yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-pylint
    rev: v2.9.6
    hooks:
      - id: pylint
```

### 4. Pruebas Unitarias

Aunque Pre-commit se enfoca en verificaciones antes del commit, también puedes configurarlo para ejecutar pruebas unitarias antes de confirmar tus cambios. Esto garantiza que no se introduzcan regresiones en tu código.

```yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-tox
    rev: v3.24.0
    hooks:
      - id: tox
```

## Ejemplo de Uso Avanzado

Supongamos que tienes un proyecto de Python con las siguientes características:

- Utilizas Black para formatear el código.
- Utilizas Flake8 para verificar el estilo.
- Tienes pruebas unitarias escritas con pytest.

Puedes configurar Pre-commit para que realice todas estas verificaciones antes de cada commit. Aquí está un ejemplo de configuración avanzada:

```yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-black
    rev: v20.8b1
    hooks:
      - id: black

  - repo: https://github.com/pre-commit/mirrors-flake8
    rev: v3.9.2
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-pytest
    rev: v6.2.4
    hooks:
      - id: pytest
```

Con esta configuración, Pre-commit ejecutará Black, Flake8 y pytest antes de cada commit, asegurándose de que tu código esté formateado correctamente, cumpla con las convenciones de estilo y pase todas las pruebas unitarias.

## Conclusión

Pre-commit es una herramienta poderosa que puede mejorar significativamente la calidad y la consistencia de tu código en proyectos Python. Al automatizar las verificaciones de calidad antes de cada commit, te aseguras de que tu código esté limpio, formateado correctamente y libre de errores. Esto facilita la colaboración en equipos de desarrollo y contribuye a la sostenibilidad a largo plazo de tus proyectos.

Si deseas obtener más información sobre cómo configurar Pre-commit o explorar otras opciones de ganchos disponibles, consulta la [documentación oficial de Pre-commit](https://pre-commit.com/).

Integrar Pre-commit en tu flujo de trabajo de desarrollo de software es una decisión inteligente que te ayudará a mantener la calidad de tu código sin esfuerzo adicional. ¡Pruébalo en tu próximo proyecto y experimenta los beneficios por ti mismo!