# Finance Dashboard 

## PREVIO A INSTALACION
1. Debes tener instalado xampp para el servido web local.
2. Instalar visual studio code(editor de codigo).

## Instalación 
1. Dirigirse a visual studio code 
2. Clonar el repositorio desde el menu central `clone git repository`
3. Selecionar una carpeta vacia  donde guardar el repositorio 
4. Abrir la terminal desde el menu superior apretar `new terminal` 
5. Crear entorno virtual: `python -m venv venv` 
6. Activar entorno virtual: 
   - Windows: `venv\Scripts\activate` 
   - Unix: `source venv/bin/activate` 
7. Instalar dependencias: `pip install -r requirements.txt`
8. Dirigete a xampp y prende apache para el servidor y mysql para base de datos
9. Despues has click en `admin de mysql`
10. Crea una nueva base de datos llamada finance
11. Dirigete a la terminal de visual studio code y ejecuta estos comandos en este orden con el entorno vitual prendido `flask db init,flask db migrate ,flask db upgrade`
12. Ejecutar `server.py`
