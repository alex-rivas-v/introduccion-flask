# Introduccion a Flask

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

En una terminal, ya sea en PowerShell o la terminal de Visual Studio Code, cambie al directorio donde se encuentra el archivo `main.py` y ejecute el siguiente comando:

```bash
python3 main.py
```

Luego de ejecutar el comando, se mostrará algo similar a lo siguiente en la terminal:

```bash
 * Serving Flask app 'App'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with watchdog (fsevents)
 * Debugger is active!
 * Debugger PIN: 249-588-001
```

Para acceder a la aplicacion, abra un navegador y ve a la dirección que se muestra en la salida. En este caso, `http://127.0.0.1:5000`.

## Cerrar la aplicacion

Para cerrar la aplicacion, presione `CTRL+C` en la terminal donde se esta ejecutando la aplicacion.