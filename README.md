# PISU Community: Plataforma de Integración Social Universitaria

## Integrantes del Equipo

1. Fernando Gael Hernández Magaña
2. Héctor Daniel Martínez Téllez
3. Fernando Estrada

## Descripción del Proyecto

**PISU Community** es una plataforma digital destinada a la comunidad universitaria de la Universidad de Guadalajara, creada con el objetivo de unificar tanto la gestión académica como la interacción social y la conservación de momentos importantes de la vida estudiantil. Con funcionalidades clave como un foro universitario y un anuario digital, PISU Community busca fomentar la identidad universitaria, facilitando la comunicación y el intercambio de recursos entre estudiantes, profesores y personal administrativo.

## Metodologías de Desarrollo

Para el desarrollo de PISU Community, hemos decidido implementar una combinación del ciclo de vida en cascada y la metodología Agile Kanban, con el apoyo de la herramienta **Todoist** para la gestión de tareas y el seguimiento de cada etapa.

### Ciclo de Vida en Cascada

El ciclo de vida en cascada permite estructurar el proyecto en etapas claras, asegurando la calidad en cada fase. En este proyecto, el ciclo de vida en cascada guía los pasos iniciales, desde el análisis de requisitos y el diseño hasta la implementación de las funcionalidades fundamentales del sistema (foro universitario y anuario digital).

### Metodología Agile Kanban

Una vez implementadas las bases del proyecto, utilizaremos Kanban para mantener un flujo continuo de trabajo, adaptarnos rápidamente a nuevas necesidades y optimizar el desarrollo basado en la retroalimentación de los usuarios. Todoist se empleará para gestionar las tareas de Kanban, categorizando las tareas en columnas de “Por Hacer”, “En Proceso” y “Completadas” para facilitar la organización y asegurar un avance incremental y flexible.

## Interfaces de Usuario

A continuación, se presentarán imágenes de las posibles interfaces de la aplicación, mostrando diseños preliminares del foro universitario, el anuario digital y el sistema de navegación principal:

### Barra de Navegación - Anuario Vista

Esta es la vista contara con el nombre de la aplicación y su logo en la parte Izquierda sin ninguna función asignada solamente por motivos de estítica, en seguida de esto se localizan dos botones que tendrían una transición dependiendo de la vista a la que apunte, en la imagen mostrada la vista que se esta renderizando sera la del Anuario, y con la opción del foro justo abajo para poder hacer el cambio de vista. Después, se encuentra el buscador que sera un auxiliar para localizar publicaciones, generaciones, carreras o centros. Por ultimo tendremos el nombre del estudiante y su carrera alado de un icono con su foto de perfil que el podra definir.

![Anuario.png](PISU%20Community%20Plataforma%20de%20Integracio%CC%81n%20Social%20U%2012ecacad32d780da861ce0aece6c3040/196921e2-ac84-491f-beaa-a7f4a95662d7.png)

### Barra de Navegación - Foro Vista

En esta vista se encontrara la misma información que en la vista anterior solo que lo que cambiara sera el label (botón) que pasara de Anuario a Foro. Después, al igual que la barra de la vista del Anuario se encontrara un buscador auxiliar que ayudara para agilizar la localización de Foros o Discusiones especificas.

![Foro.png](PISU%20Community%20Plataforma%20de%20Integracio%CC%81n%20Social%20U%2012ecacad32d780da861ce0aece6c3040/bdbe9598-11c8-4cb5-a03a-adc94fa18244.png)

### Auth - Home Vista

Sera una vista general al dar con la ruta por default de la pagina en donde se explica brevemente como acceder y agrandes rasgos que es. El único botón disponible es el de iniciar sesion que mandara a otra vista.

![Auth.png](PISU%20Community%20Plataforma%20de%20Integracio%CC%81n%20Social%20U%2012ecacad32d780da861ce0aece6c3040/4896e17e-1f90-4731-9ce5-fddcec10bad6.png)

### Auth - Login Vista

En esta vista optamos con un enfoque minimista, en donde podrías iniciar sesión con tu cuenta Institucional de Google, esto antes registrándote con tu cuenta institucional, el campo del registro del correo se encargara de verificar si es una cuenta con el dominio de la udg, `@alumnos.udg.mx` en dado caso de ser a si permitiría el registro y mandara antes un correo de confirmación a su correo institucional.

![Auth.png](PISU%20Community%20Plataforma%20de%20Integracio%CC%81n%20Social%20U%2012ecacad32d780da861ce0aece6c3040/6fe14e87-9506-451a-8a4b-a6304de72478.png)

---
