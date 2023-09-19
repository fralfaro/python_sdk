# Logging

Python, como lenguaje de programación, 
ofrece un módulo de registro extremadamente versátil conocido como [logging](https://docs.python.org/3/howto/logging.html). Ya sea para depurar una simple aplicación o gestionar registros desde múltiples servidores, el módulo `logging` de Python puede ser una herramienta esencial para desarrolladores y operadores. En este artículo, exploraremos en profundidad el concepto de registro, la importancia de su uso y cómo aprovechar al máximo el módulo `logging` de Python.

## Introducción 

**Logging**, que proviene del término inglés "log," se refiere a un protocolo que registra eventos y acciones importantes en la historia de un proceso o aplicación. En el contexto de la programación, esto significa la captura y el registro de eventos y datos relevantes durante la ejecución de un programa. Dependiendo de los requisitos de seguimiento, puedes configurar el registro para registrar solo eventos específicos o para registrar todo lo que ocurra en tu aplicación.

Cuando trabajas en aplicaciones complejas, el registro de Python puede generar una gran cantidad de datos. El módulo `logging` de Python permite escribir estos datos en archivos de registro, pero es importante que esta escritura sea asincrónica para evitar bloqueos en la ejecución del código.

### Análisis de Errores con Niveles de Gravedad

El módulo `logging` de Python proporciona cinco niveles de gravedad distintos, también conocidos como "levels of severity." Aunque puedes crear tus propios filtros de registro, los niveles de gravedad predefinidos en el módulo `logging` de Python, desarrollado por **Vinay Sajip**, son bastante adecuados y comunes en la industria:

| Nombre del Nivel de Registro | Uso                                                                                                                  | Ejemplo de Mensaje de Registro                                                  |
|------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Debug                        | Diagnóstico de problemas, información detallada                                                                          | Sangría inesperada en la línea X                                           |
| Info                         | Indica que la aplicación funciona correctamente                                                                         | La función 1*1 se está ejecutando.                                          |
| Warning                      | La aplicación funciona correctamente, pero se ha producido una situación inesperada o se predice un problema futuro. | Poco espacio de almacenamiento                                             |
| Error                        | No se pudo realizar una función debido a un problema.                                                                | Ha ocurrido un error y se ha interrumpido la acción.                       |
| Critical                     | Ha ocurrido un problema grave. Es posible que la aplicación deba interrumpirse por completo.                         | Error grave: el programa no puede acceder a este servicio y debe cerrarse. |

* **Debug** es el nivel más bajo y se utiliza para la información de baja prioridad. Esto no significa que los errores registrados con este nivel sean menos graves que los registrados con nivel **Critical**.

* **Debug** incluye todos los niveles superiores, lo que significa que si configuras el registro en **Debug**, se registrarán todos los mensajes, desde **Debug** hasta **Critical**.

### Componentes Principales del Módulo `logging`

#### Logger

Los loggers registran acciones durante la ejecución de un programa. No se pueden utilizar directamente como instancias, sino que se obtienen mediante la función `logging.getLogger(nombre del logger)`. Asignar un nombre concreto a un logger puede ayudar a estructurar las jerarquías de registros. Por ejemplo, si tienes un paquete llamado `log`, los loggers pueden tener nombres como `log.bam` o `log.bar.loco`. Los loggers funcionan de manera similar a la estructura de directorios en Python, donde los puntos separan los paquetes. Esto significa que el objeto `log` recibirá los registros de los directorios `log.bam` y `log.bar.loco`.

#### Handler

Los handlers recopilan información del logger y la envían a un destino específico. Los handlers son clases básicas que determinan cómo se comportan las instancias del handler. Para configurar el destino, debes usar el tipo de handler correspondiente. Por ejemplo, **StreamHandler** envía los datos de registro a flujos, mientras que **FileHandler** los envía a archivos. Puedes usar varios handlers en un programa para enviar mensajes del mismo logger a diferentes destinos. Esto es útil si deseas mostrar mensajes de depuración en la consola y mensajes de error en un archivo independiente.

Mediante el método `setLevel()`, puedes establecer el nivel mínimo de gravedad que un mensaje de registro debe tener para ser enviado al handler correspondiente. Para establecer el nivel de registro de un handler en lugar del logger, utiliza `[nombre del handler].setLevel`.

#### Formatter

Los formateadores (o formatters) se utilizan para definir el formato en el que se presentarán los mensajes en el archivo de registro. Si no se utiliza un formato personalizado, solo se mostrará el mensaje especificado en el registro.

#### Filter

Los filtros permiten definir condiciones precisas para los mensajes de salida. Debes configurar los filtros primero y luego agregarlos al handler o logger correspondiente utilizando el método `addFilter()`. Si el valor de un filtro es falso debido a las propiedades del mensaje, el mensaje no se enviará. Puedes utilizar filtros para permitir que solo los datos de registro de un logger específico se envíen y bloquear todos los demás loggers.

## Uso del Módulo `logging` de Python

Ahora que hemos explorado los fundamentos del módulo `

logging` de Python, es hora de aprender cómo utilizarlo en la práctica. A continuación, se muestra un ejemplo simple de cómo configurar un logger y registrar mensajes:

```python
import logging

# Configurar el logger
logging.basicConfig(level=logging.DEBUG, filename='app.log', format='%(asctime)s - %(levelname)s: %(message)s')

# Crear un logger con un nombre específico
logger = logging.getLogger('mi_aplicacion')

# Registrar eventos
logger.debug('Este es un mensaje de depuración.')
logger.info('Información: La aplicación funciona correctamente.')
logger.warning('¡Advertencia! Espacio de almacenamiento bajo.')
logger.error('Error: La operación ha fallado.')
logger.critical('Error crítico: La aplicación debe cerrarse.')

# Finalizar el registro
logging.shutdown()
```

En este ejemplo:

- Configuramos el nivel de registro en **DEBUG**, lo que significa que se registrarán todos los mensajes, desde **DEBUG** hasta **CRITICAL**.
- Especificamos un archivo de registro llamado `app.log` y un formato personalizado para los mensajes de registro.
- Creamos un logger con el nombre 'mi_aplicacion' para estructurar los registros.
- Registramos eventos con diferentes niveles de gravedad.
- Finalizamos el registro con `logging.shutdown()`.

Recuerda que el módulo `logging` de Python ofrece muchas más opciones de configuración y personalización. Puedes ajustar los handlers, formatters y filtros según tus necesidades específicas.

## Loguru

[Loguru](https://github.com/Delgan/loguru) es una biblioteca de registro en Python que tiene como objetivo hacer que el proceso de registro sea más sencillo y agradable. Desarrollada por **Delgan**, Loguru está diseñada para mejorar la experiencia de registro en Python, proporcionando una amplia gama de funcionalidades útiles y resolviendo muchas de las dificultades asociadas con los loggers estándar.

### Facilidad de Uso

La principal filosofía detrás de Loguru es que "hay uno y solo uno" *logger*. Este logger se configura automáticamente y envía los mensajes a la salida estándar (`stderr`) por defecto. Esto significa que puedes comenzar a registrar eventos sin necesidad de configuraciones complejas. Veamos un ejemplo simple de cómo funciona:

```python
from loguru import logger

logger.debug("¡Así de sencillo es utilizar Loguru para el registro de eventos!")
```

### Sin Necesidad de Handlers, Formatters o Filtros: Todo en Uno

En el mundo de los loggers estándar, configurar handlers, definir el formato de los registros, aplicar filtros y establecer niveles de registro puede ser una tarea tediosa. Loguru simplifica todo esto con una función llamada `add()`:

```python
from loguru import logger

logger.add("archivo.log", format="{time} {level} {message}", filter="mi_modulo", level="INFO")
```

La función `add()` se utiliza para agregar "sinks", que son responsables de manejar los mensajes de registro contextualizados en forma de diccionarios. Un "sink" puede tomar varias formas, desde una función simple hasta una ruta de archivo, y se encarga de la administración de los mensajes de registro.

### Registro de Archivos Simplificado con Rotación, Retención y Compresión

Si deseas registrar mensajes en un archivo, Loguru lo hace extremadamente sencillo. Puedes especificar una ruta de archivo como destino de registro:

```python
from loguru import logger

logger.add("archivo_{time}.log")
```

Loguru también facilita la configuración de la rotación de archivos (por tamaño, tiempo o cualquier criterio personalizado), la retención de registros antiguos y la compresión de archivos de registro al cerrar la aplicación:

```python
from loguru import logger

logger.add("archivo_1.log", rotation="500 MB")  # Rotación cuando el archivo supera los 500 MB
logger.add("archivo_2.log", rotation="12:00")   # Nuevo archivo cada día al mediodía
logger.add("archivo_3.log", rotation="1 week")  # Rotación semanal
logger.add("archivo_X.log", retention="10 days")  # Retención durante 10 días
logger.add("archivo_Y.log", compression="zip")   # Compresión de archivos en formato ZIP
```

### Captura de Excepciones en Hilos y el Flujo Principal

Loguru resuelve un problema común al capturar excepciones en hilos o en el flujo principal del programa. ¿Alguna vez has visto que tu aplicación falla sin ningún mensaje de registro? ¿O has notado que las excepciones en los hilos no se registran? Loguru soluciona esto utilizando el decorador/administrador de contexto `catch`, que garantiza que las excepciones se propaguen correctamente al logger:

```python
from loguru import logger

@logger.catch
def mi_funcion(x, y, z):
    # ¡Las excepciones se registran automáticamente!
    return 1 / (x + y + z)
```

### Registro Atractivo con Colores

Loguru agrega automáticamente colores a tus registros si tu terminal es compatible. Puedes definir tu propio estilo utilizando etiquetas de marcado en el formato del "sink":

```python
from loguru import logger

logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
```

Las funciones asíncronas utilizadas como "sink" también son compatibles y se pueden esperar con `complete()`.

### Excepciones Totalmente Descriptivas

Registrar excepciones es fundamental para depurar problemas, pero puede ser inútil si no tienes información suficiente para solucionarlos. Loguru te ayuda a identificar problemas mostrando todo el seguimiento de la pila, incluyendo los valores de las variables:

```python
from loguru import logger

logger.add("salida.log", backtrace=True, diagnose=True)  # Cuidado, esto puede exponer datos sensibles en producción

def mi_funcion(a, b):
    return a / b

def anidada(c):
    try:
        mi_funcion(5, c)
    except ZeroDivisionError:
        logger.exception("¡Ups!")
```

### Mejor Gestión de Fecha y Hora

Lograr que los registros tengan una fecha y hora legibles puede ser complicado con los loggers estándar. Loguru lo resuelve de manera sencilla:

```python
from loguru import logger

logger.add("archivo.log", format="{time:YYYY-MM-DD a las HH:mm:ss} | {level} | {message}")
```

En resumen, Loguru simplifica significativamente el proceso de registro de eventos en Python y ofrece una amplia gama de características útiles. Ya sea para una pequeña aplicación o un proyecto más grande, Loguru puede mejorar tu experiencia de registro y ayudarte a mantener un mejor control sobre los eventos de tu aplicación.