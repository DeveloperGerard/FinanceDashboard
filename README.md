# Finance Dashboard

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **XAMPP:** Para contar con un servidor web local y gestionar MySQL.  
  [Descargar XAMPP](https://www.apachefriends.org/es/download.html)
- **Visual Studio Code:** Editor de código.  
  [Descargar Visual Studio Code](https://code.visualstudio.com/)

## Instalación y Configuración

1. **Clonar el Repositorio:**
   - Abre Visual Studio Code.
   - Ve al menú central y selecciona la opción "Clone Git Repository".
   - Elige una carpeta vacía donde clonar el repositorio.

2. **Configurar el Entorno Virtual:**
   - Abre la terminal integrada (menú superior → *New Terminal*).
   - Crea el entorno virtual ejecutando:
     ```bash
     python -m venv venv
     ```
   - Activa el entorno virtual:
     - En **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - En **Unix/Linux/MacOS**:
       ```bash
       source venv/bin/activate
       ```

3. **Instalar Dependencias:**
   - Ejecuta en la terminal:
     ```bash
     pip install -r requirements.txt
     ```

4. **Configurar XAMPP:**
   - Abre XAMPP y enciende los módulos **Apache** (para el servidor web) y **MySQL** (para la base de datos).
   - Haz clic en el botón **Admin** de MySQL para acceder al panel de administración.
   - Crea una nueva base de datos llamada **finance**.

5. **Configurar la Base de Datos con Flask-Migrate:**
   - En la terminal de Visual Studio Code, con el entorno virtual activo, ejecuta los siguientes comandos en el orden indicado:
     ```bash
     flask db init
     flask db migrate
     flask db upgrade
     ```

6. **Iniciar el Servidor:**
   - Ejecuta el siguiente comando en la terminal para iniciar el servidor:
     ```bash
     python server.py
     ```