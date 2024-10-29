#!/usr/bin/env python3.13

import os

def create_file_if_not_exists(file_path, content=""):
    """
    Crea un archivo si no existe y escribe el contenido proporcionado.
    """
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Archivo creado: {file_path}")
    else:
        print(f"Archivo ya existe: {file_path}")

def create_global_static_files(static_dir):
    """
    Crea los archivos globales CSS y JS en el directorio de static.
    """
    os.makedirs(os.path.join(static_dir, 'css'), exist_ok=True)
    os.makedirs(os.path.join(static_dir, 'js'), exist_ok=True)
    
    create_file_if_not_exists(os.path.join(static_dir, 'css', 'global.css'), "/* Estilos globales */")
    create_file_if_not_exists(os.path.join(static_dir, 'js', 'global.js'), "// Javascript global")

def create_global_template_files(template_dir):
    """
    Crea la plantilla base.html en el directorio global de templates.
    """
    os.makedirs(template_dir, exist_ok=True)
    
    base_html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{% static 'css/global.css' %}">
    <title>{% block title %}PISU-Community{% endblock %}</title>
</head>
<body>
    <header>
        <h1>PISU-Community</h1>
    </header>

    <nav>
        <!-- Links de navegación -->
    </nav>

    <main>
        {% block content %}
        <!-- Contenido específico de cada página -->
        {% endblock %}
    </main>

    <footer>
        <p>© 2024 PISU-Community</p>
    </footer>
</body>
</html>
"""
    create_file_if_not_exists(os.path.join(template_dir, 'base.html'), base_html_content)

def create_app_static_and_templates(app_name, app_path):
    """
    Crea las carpetas y archivos de static y templates para una aplicación específica.
    """
    static_dir = os.path.join(app_path, 'static', app_name, 'css')
    templates_dir = os.path.join(app_path, 'templates', app_name)
    
    os.makedirs(static_dir, exist_ok=True)
    os.makedirs(templates_dir, exist_ok=True)
    
    create_file_if_not_exists(os.path.join(static_dir, f'{app_name}.css'), f"/* Estilos para {app_name} */")
    
    index_html_content = f"""{{% extends "base.html" %}}

{{% block content %}}
<h2>Página de {app_name}</h2>
<p>Bienvenido a la página de {app_name}.</p>
{{% endblock %}}
"""
    create_file_if_not_exists(os.path.join(templates_dir, 'index.html'), index_html_content)

def create_structure_for_project(project_path):
    """
    Lee la estructura de un proyecto Django y crea las carpetas correspondientes.
    """
    apps = []
    
    for item in os.listdir(project_path):
        item_path = os.path.join(project_path, item)
        
        # Verificar si es una aplicación de Django (carpeta con views.py, models.py, etc.)
        if os.path.isdir(item_path) and 'views.py' in os.listdir(item_path):
            apps.append(item)

    # Crear las carpetas y archivos globales en la carpeta principal del proyecto
    static_dir = os.path.join(project_path, 'static')
    template_dir = os.path.join(project_path, 'templates')

    create_global_static_files(static_dir)
    create_global_template_files(template_dir)

    # Crear carpetas y archivos para cada aplicación
    for app in apps:
        app_path = os.path.join(project_path, app)
        create_app_static_and_templates(app, app_path)

    print("Estructura creada correctamente.")

if __name__ == '__main__':
    project_path = input("Ingresa la ruta del proyecto Django: ")
    if os.path.exists(project_path):
        create_structure_for_project(project_path)
    else:
        print("La ruta proporcionada no existe.")

