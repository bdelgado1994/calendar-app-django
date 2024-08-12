# Django FullCalendar Event Management

Este es un proyecto de gestión de eventos utilizando Django y FullCalendar. Permite a los usuarios ver, crear, editar y eliminar eventos en un calendario interactivo.

## Funcionalidades

- **Ver Eventos**: Muestra un calendario con eventos ya existentes.
- **Crear Eventos**: Permite a los usuarios añadir nuevos eventos.
- **Editar Eventos**: Permite a los usuarios modificar eventos existentes.
- **Eliminar Eventos**: Permite a los usuarios eliminar eventos.

## Tecnologías Utilizadas

- **Django**: Framework web para Python.
- **FullCalendar**: Biblioteca JavaScript para la visualización de calendarios.
- **Bootstrap 5**: Framework CSS para el diseño responsive.
- **Crispy Forms**: Extensión de Django para mejorar la apariencia de los formularios.

## Instalación

Sigue estos pasos para configurar el proyecto en tu máquina local:

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
2. **Configura el entorno virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
4. **Realiza las migraciones:**
   ```bash
   python manage.py migrate
