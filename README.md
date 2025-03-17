# Finance Dashboard

## Descripción
Finance Dashboard es una aplicación web que te permite gestionar tus finanzas personales. Con ella podrás llevar el control de ingresos, gastos, servicios, préstamos y generar informes financieros.

## Características
- Gestión de cuentas bancarias
- Registro de ingresos y gastos
- Control de servicios y pagos
- Administración de préstamos
- Informes financieros

## Requisitos
- **Python 3.8+**: Lenguaje de programación.
- **MySQL**: Sistema de gestión de bases de datos.
- **[XAMPP](https://www.apachefriends.org/es/download.html)** (opcional): Permite ejecutar un servidor web y MySQL de forma local.

## Instalación

### 1. Clonar el Repositorio
Este paso consiste en copiar el código del proyecto desde GitHub a tu computadora.

1. Abre una terminal o símbolo del sistema.
2. Ejecuta el siguiente comando para clonar el repositorio:
   ```bash
   git clone https://github.com/DeveloperGerard/FinanceDashboard.git
   ```
3. Entra en la carpeta del proyecto:
   ```bash
   cd FinanceDashboard
   ```

### 2. Crear y Activar el Entorno Virtual
El entorno virtual es un espacio aislado para instalar las dependencias del proyecto sin interferir con otras instalaciones de Python.

1. Para crear el entorno virtual, ejecuta:
   ```bash
   python -m venv venv
   ```
   Esto creará una carpeta llamada `venv` donde se almacenarán las librerías del proyecto.

2. Activa el entorno virtual:
   - **En sistemas Unix/Linux/MacOS**:
     ```bash
     source venv/bin/activate
     ```
   - **En Windows**:
     ```bash
     venv\Scripts\activate
     ```
   Una vez activado, verás que el prompt de tu terminal cambia (aparecerá algo como `(venv)` al inicio).

### 3. Instalar Dependencias
Las dependencias son las librerías y paquetes que el proyecto necesita para funcionar.

1. Con el entorno virtual activado, ejecuta:
   ```bash
   pip install -r requirements.txt
   ```
   Este comando leerá el archivo `requirements.txt` e instalará todas las librerías necesarias.

### 4. Configuración Automática de la Base de Datos y Migraciones
El siguiente paso automatiza la creación de la base de datos y la estructura de las tablas, sin necesidad de hacerlo manualmente.

#### a) Crear la Base de Datos Automáticamente
El proyecto utiliza **SQLAlchemy** para conectarse a MySQL y crear la base de datos "finance" si aún no existe. Abre el archivo de configuración (por ejemplo, `__init__.py`) y añade lo siguiente:

```python
from sqlalchemy import create_engine,text
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Cadena de conexión sin especificar la base de datos.
# Cambia 'usuario' y 'contraseña' por tus credenciales de MySQL.
db_uri_base = 'mysql+pymysql://usuario:contraseña@localhost/'

# Conectarse a MySQL y crear la base de datos si no existe.
engine = create_engine(db_uri_base)
with engine.connect() as connection:
    connection.execute(text("CREATE DATABASE IF NOT EXISTS finance"))


# Configurar la aplicación para usar la base de datos "finance".
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri_base + 'finance'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

**Explicación:**  
- Se conecta a MySQL sin seleccionar una base de datos específica.
- Se ejecuta una instrucción SQL que crea la base de datos **finance** si no existe.
- Luego, se configura la aplicación Flask para usar esa base de datos.

#### b) Automatizar las Migraciones
Las migraciones permiten crear y actualizar la estructura (tablas) de la base de datos de forma organizada. Para automatizarlas, puedes usar un script de shell llamado `setup.sh`.

1. Crea un archivo llamado `setup.sh` en la raíz del proyecto y pega el siguiente contenido:

   ```bash
   #!/bin/bash
   # Verificar que estamos en la carpeta correcta
   if [ ! -f "requirements.txt" ]; then
     echo "Por favor, ejecuta este script desde la raíz del repositorio."
     exit 1
   fi

   echo "Activando el entorno virtual..."
   # Activa el entorno virtual (modifica la línea según tu sistema operativo)
   source venv/bin/activate

   echo "Inicializando migraciones..."
   flask db init

   echo "Creando la migración inicial..."
   flask db migrate -m "Migración inicial"

   echo "Aplicando migraciones..."
   flask db upgrade

   echo "Iniciando la aplicación..."
   python server.py
   ```

2. Dale permisos de ejecución al script:
   ```bash
   chmod +x setup.sh
   ```

3. Ejecuta el script:
   ```bash
   ./setup.sh
   ```

**Explicación del Script:**  
- **Activación del entorno virtual:** Asegura que se usen las librerías correctas.
- **Migraciones:**  
  - `flask db init`: Inicializa la carpeta de migraciones.
  - `flask db migrate`: Genera una migración basada en los cambios del modelo.
  - `flask db upgrade`: Aplica la migración a la base de datos, creando las tablas necesarias.
- **Inicio de la aplicación:** Finalmente, inicia el servidor Flask.

### 5. Iniciar la Aplicación Manualmente (Opcional)
Si prefieres ejecutar cada comando de forma individual o ya configuraste la base de datos y migraciones, simplemente inicia el servidor con:
```bash
flask run
```

## Recomendaciones Adicionales: Uso de Visual Studio Code
Aunque es posible realizar todos estos pasos de manera nativa con cualquier editor y terminal, **recomendamos el uso de Visual Studio Code (VS Code)** por las siguientes razones:

- **Terminal Integrada:**  
  VS Code permite abrir una terminal integrada (usualmente con el atajo ``Ctrl+` ``) en la misma ventana, lo que facilita la ejecución de comandos sin cambiar de aplicación.

- **Control de Versiones:**  
  Cuenta con integración nativa con Git, lo que permite clonar, gestionar ramas y hacer commits de manera visual y sencilla.

- **Extensiones y Complementos:**  
  Existen extensiones para Python y Flask que proporcionan resaltado de sintaxis, autocompletado, depuración y otros útiles recursos.

- **Navegación y Edición de Código:**  
  La interfaz de VS Code facilita la búsqueda y navegación por el código, permitiendo encontrar rápidamente funciones, variables y archivos.

- **Configuraciones y Tareas Automatizadas:**  
  Puedes configurar tareas automatizadas (por ejemplo, para ejecutar scripts de configuración o pruebas) que se integran directamente en el entorno de desarrollo.

Si deseas aprovechar estas funcionalidades, descarga e instala [Visual Studio Code](https://code.visualstudio.com/), abre la carpeta del proyecto y explora las opciones en el menú lateral para Git, Terminal y Extensiones.

## Personalización
- **Favicon:**  
  El ícono de la pestaña del navegador se encuentra en el archivo `favicon.ico`. Puedes reemplazarlo con tu propio ícono para personalizar la aplicación.