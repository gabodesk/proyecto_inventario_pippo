# Sistema de Gestión de Inventario - Jardín Infantil Pippo

Aplicación de escritorio desarrollada en Python para apoyar el control de inventario de insumos del Jardín Infantil Pippo, especialmente productos de limpieza, materiales educativos y artículos de oficina.

El sistema permite registrar, consultar, editar, eliminar y buscar productos almacenados en una base de datos local SQLite. Además, incorpora alertas visuales para identificar productos con stock bajo o suficiente, facilitando la toma de decisiones sobre reposición de insumos.

## Objetivo del proyecto

Desarrollar una aplicación de escritorio funcional para gestionar el inventario de productos utilizados por el Jardín Infantil Pippo, permitiendo mantener un registro ordenado de existencias, categorías, unidades de medida y niveles mínimos de stock.

El proyecto busca reducir los errores asociados al control manual de inventario y mejorar la visualización de los productos que requieren reposición.

## Tecnologías utilizadas

* Python 3.10+
* CustomTkinter
* SQLite3
* Git
* Entorno virtual `venv`

## Funcionalidades principales

* Registro de productos.
* Consulta de productos registrados.
* Edición de productos existentes.
* Eliminación de productos.
* Búsqueda de productos por nombre.
* Búsqueda aproximada por caracteres.
* Filtro de productos por categoría.
* Búsqueda cruzada por nombre y categoría.
* Registro de categoría del producto.
* Registro de unidad de medida.
* Registro de stock actual.
* Registro de stock mínimo.
* Detección de productos bajo stock mínimo.
* Ordenamiento visual según urgencia de reposición.
* Alerta visual por color según estado de stock.
* Persistencia de datos mediante base de datos local SQLite.
* Interfaz gráfica de escritorio simple y orientada al usuario final.

## Alertas visuales de stock

La aplicación utiliza una simbología visual para facilitar la interpretación rápida del estado del inventario:

* Rojo: producto bajo el stock mínimo definido.
* Verde: producto con stock suficiente.

Esta funcionalidad permite identificar de forma inmediata qué productos requieren reposición prioritaria.

## Categorías disponibles

El sistema permite clasificar los productos en categorías mediante listas desplegables, evitando errores de escritura y manteniendo mayor consistencia en los registros.

Categorías consideradas:

* Limpieza
* Educativo
* Oficina

## Unidades de medida disponibles

El sistema permite asociar cada producto a una unidad de medida, también mediante listas desplegables.

Unidades consideradas:

* Unidades enteras
* Litros
* Kilogramos
* Metros

## Estructura del proyecto

```text
proyecto_inventario_pippo/
├── main.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
└── inventario.db
```

> Nota: el archivo `inventario.db` se genera automáticamente al ejecutar la aplicación. No se sube al repositorio porque está incluido en `.gitignore`.

## Descripción de archivos principales

### `main.py`

Contiene la interfaz gráfica de la aplicación, desarrollada con CustomTkinter. Desde este archivo se gestionan las ventanas, botones, formularios, menús desplegables, búsquedas y visualización de productos.

### `database.py`

Contiene la lógica de conexión y operaciones con la base de datos SQLite. Incluye funciones para crear la tabla de productos y realizar operaciones CRUD sobre los registros.

### `requirements.txt`

Contiene las dependencias necesarias para ejecutar el proyecto.

## Base de datos

El sistema utiliza SQLite3 como motor de base de datos local.

La tabla principal es `productos`, compuesta por los siguientes campos:

```text
id
nombre
categoria
unidad_medida
stock_actual
stock_minimo
```

La base de datos se crea automáticamente al ejecutar la aplicación por primera vez.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/gabodesk/proyecto_inventario_pippo.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd proyecto_inventario_pippo
```

### 3. Crear un entorno virtual

En Linux o macOS:

```bash
python3 -m venv venv
```

En Windows:

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

En Linux o macOS:

```bash
source venv/bin/activate
```

En Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Ejecutar la aplicación

```bash
python main.py
```

En algunos sistemas Linux puede utilizarse:

```bash
python3 main.py
```

## Flujo general de uso

1. Ejecutar la aplicación.
2. Registrar productos indicando nombre, categoría, unidad de medida, stock actual y stock mínimo.
3. Visualizar los productos cargados en el listado principal.
4. Usar la búsqueda por nombre o filtro por categoría para encontrar productos específicos.
5. Editar productos existentes cuando sea necesario.
6. Eliminar productos que ya no correspondan al inventario.
7. Revisar visualmente los productos con stock bajo para priorizar reposiciones.

## Estado actual del proyecto

El proyecto se encuentra en etapa funcional como prototipo de aplicación de escritorio. Actualmente permite gestionar productos mediante operaciones básicas de inventario, almacenar información localmente y visualizar alertas de stock mínimo.

La aplicación cumple con las funciones principales definidas para un producto mínimo viable orientado al control de inventario del Jardín Infantil Pippo.

## Alcance actual

El sistema está enfocado en la gestión local de productos e insumos mediante una aplicación de escritorio. Su alcance actual incluye:

* Gestión básica de productos.
* Control de stock actual y stock mínimo.
* Clasificación por categoría.
* Persistencia local mediante SQLite.
* Visualización clara del estado del inventario.
* Apoyo a la detección de productos que requieren reposición.

## Limitaciones actuales

* No incluye autenticación de usuarios.
* No genera reportes en PDF.
* No posee sincronización en la nube.
* No registra historial detallado de compras o consumos.
* No incluye instalador ni versión portable.
* La base de datos se mantiene de forma local en el equipo donde se ejecuta la aplicación.

## Posibles mejoras futuras

* Generación de reportes en PDF.
* Registro de movimientos de entrada y salida de stock.
* Historial de compras y consumos.
* Planificador de compras.
* Estimación de costos de reposición.
* Exportación de datos.
* Mejoras visuales en la interfaz.
* Creación de una versión portable o ejecutable.
* Respaldo automático de la base de datos.

## Autor

Gabriel Sebastián Alarcón Pereira

Proyecto desarrollado como parte de la práctica profesional para el Instituto Profesional IACC.

## Agradecimientos

A mi familia, por su apoyo y comprensión durante el desarrollo de este proyecto.

