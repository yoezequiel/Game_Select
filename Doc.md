### Documentación Técnica del Proyecto: Game_Select

### 1. Introducción

#### Propósito

El propósito de este documento es proporcionar una guía técnica detallada sobre el desarrollo y funcionamiento del proyecto "Selector de Juegos". Este proyecto se encarga de proporcionar una interfaz gráfica para que los usuarios seleccionen y ejecuten diferentes minijuegos.

#### Alcance

El alcance de este documento incluye la descripción del código, su estructura, instalación, configuración, y cómo mantener y extender el proyecto. No se incluyen los detalles específicos de los minijuegos en sí, solo el selector.

### 2. Estructura del Proyecto

#### Descripción de la Estructura de Directorios

```
Game_Select/
├── main.py
├── database/
|   |--db.py
├── screens/
│   ├── game_screen.py
├── utils
|   |--config.py
|   |--buttons.py
|   |--execute_game.py
├── assets/
|   |--fonts/
|   |   |--font_game.TTF
│   └── img/
|   |   |--flecha.png
|   |   |--fondo.jpg
|   |   |--marco.jpg
|   |   |--minigame.jpg
|   |   |--minigame1.jpg
└── games/
    ├── game1/
    ├── game2/
    ├── game3/
    └── game4/
```

#### Descripción de Archivos

-   **main.py**: Punto de entrada del proyecto que inicializa la base de datos y maneja el flujo entre pantallas.
-   **database/**: Contiene funciones relacionadas con la base de datos SQLite.
-   **utils/**: Contiene funciones auxiliares como la ejecución de juegos.
-   **screens/**: Contiene funciones para manejar y dibujar la pantalla de juegos.
-   **assets/**: Carpeta que contiene todas las imágenes y fuentes necesarias para el proyecto.
-   **games/**: Carpeta que contiene los minijuegos.

### 3. Requisitos del Sistema

#### Hardware

-   Procesador: 1 GHz o superior
-   Memoria RAM: 2 GB o superior
-   Espacio en Disco: 50 MB

#### Software

-   Python 3.x
-   Pygame 2.0 o superior
-   Sistema Operativo: Windows, macOS, Linux

### 4. Instalación y Configuración

#### Instalación

Explicada en el [README](README)

#### Configuración

1. Asegúrate de que las imágenes necesarias están en la carpeta `assets/`.
2. Coloca los minijuegos en la carpeta `games/`.
3. Actualiza el archivo `config.py` con la dirección del `main.py` de los juegos

### 5. Descripción de los Módulos

#### `db.py`

Módulo para manejar la base de datos SQLite.

-   **create_db()**: Crea la base de datos y la tabla de usuarios.

#### `utils/`

Módulo auxiliar con funciones adicionales.

-   **execute_game(filepath)**: Ejecuta un archivo de Python para iniciar un minijuego.
-   **config()**: Configuración general del programa
-   **buttons()**: Botones necesarios en el programa

#### `screens/game_screen.py`

Módulo para la pantalla de selección de juegos.

-   **draw_back_button(screen)**: Dibuja el botón de "Volver".
-   **game_screen(screen)**: Maneja la lógica de la pantalla de juegos.

#### `main.py`

Punto de entrada principal del proyecto.

-   **main()**: Inicializa la base de datos y controla el flujo entre pantallas.

### 6. Flujo del Programa

#### Descripción del Flujo Principal

1. El programa inicia en `main.py`, que llama a `create_db()` para inicializar la base de datos.
2. Luego, se entra en un bucle principal que llama a `main_screen(screen)` para mostrar la pantalla principal.
3. Desde la pantalla principal, el usuario puede ingresar su nombre y seleccionar su grado.
4. Si el usuario existe, o después de registrarse, se pasa a `game_screen(screen)`.
5. En la pantalla de juegos, el usuario puede seleccionar y ejecutar un minijuego o volver a la pantalla principal.

#### Diagramas de Flujo

![Diagrama de Flujo](<diagrama de flujo.png>)
