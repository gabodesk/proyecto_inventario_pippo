# Sistema de Gestión de Inventario - Jardín Infantil Pippo

Prototipo de aplicación de escritorio para la gestión básica de inventario de productos utilizados en el Jardín Infantil Pippo.

El sistema permite registrar productos, guardar información en una base de datos local SQLite y visualizar alertas según el stock mínimo definido para cada producto.

## Objetivo del prototipo

Desarrollar una aplicación funcional mínima para apoyar el control de inventario de productos de limpieza, educativos y de oficina, permitiendo visualizar de forma clara qué productos requieren reposición.

## Tecnologías utilizadas

- Python 3.10+
- CustomTkinter
- SQLite3
- Git
- Entorno virtual `venv`

## Funcionalidades implementadas

- Registro de productos.
- Selección de categoría mediante lista desplegable.
- Selección de unidad de medida mediante lista desplegable.
- Registro de stock actual.
- Registro de stock mínimo.
- Persistencia de datos mediante SQLite.
- Visualización de productos registrados.
- Ordenamiento de productos según urgencia.
- Alerta visual por color:
  - Rojo: producto bajo stock mínimo.
  - Verde: producto con stock suficiente.

## Categorías disponibles

- Limpieza
- Educativo
- Oficina

## Unidades de medida disponibles

- Unidades enteras
- Litros
- Kilogramos
- Metros

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

> Nota: el archivo `inventario.db` se genera automáticamente al ejecutar la aplicación y no se sube al repositorio porque está incluido en `.gitignore`.

## Instalación y ejecución

1. Clonar o abrir la carpeta del proyecto.

2. Crear un entorno virtual:

```bash
python3 -m venv venv
```

3. Activar el entorno virtual:

```bash
source venv/bin/activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecutar la aplicación:

```bash
python main.py
```

## Base de datos

El sistema utiliza SQLite3 como motor de base de datos local.

La tabla principal es `productos`, con los siguientes campos:

```text
id
nombre
categoria
unidad_medida
stock_actual
stock_minimo
```

## Estado actual del proyecto

El prototipo se encuentra en una etapa funcional inicial. Actualmente permite registrar y visualizar productos con alerta de stock mínimo.

## Próximas mejoras

- Editar productos existentes.
- Eliminar productos.
- Buscar productos por nombre.
- Filtrar productos por categoría.
- Registrar movimientos de compra y consumo.
- Mejorar la presentación visual del listado.
- Agregar validaciones adicionales.

## Autor

Gabriel Sebastián Alarcón Pereira

Proyecto desarrollado como parte de la práctica profesional para el instituto profesional IACC.

## Agradecimientos
A mi familia que me apoyó y comprendió durante todas estas horas de trabajo.
