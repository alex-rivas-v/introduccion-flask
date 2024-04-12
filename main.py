from flask import Flask, render_template, request

# Creamos la aplicacion, se le puede pasar un nombre a la aplicacion
app = Flask('App')

@app.route('/', methods=['GET', 'POST'])
def index():

    # Creamos un diccionario con los datos que se quieren enviar a la vista
    data = {
        'titulo': 'Hola, Mundo',
        'nombre': 'Alex',
        'edad': 20,
        'hobbies': ['Leer', 'Correr', 'Programar']
    }

    # Verificamos si el metodo de la peticion es POST, no es necesario implementar esto
    if request.method == 'POST':
        # Agregamos a data el valor de la vista, cambiando 'nombre' por el nombre del campo
        # data['nombre'] = request.form['nombre']
        pass # Quitamos el pass y descomentamos la linea anterior para que funcione

    # Verificamos si el metodo de la peticion es GET, no es necesario implementar esto
    if request.method == 'GET':
        # Agregamos a data el valor de la vista, cambiando 'nombre' por el nombre del campo
        # data['nombre'] = request.args.get('nombre')
        pass # Quitamos el pass y descomentamos la linea anterior para que funcione

    # Otros calculos o procesos que se quieran hacer
    
    # Retornamos la vista con los datos 
    return render_template('index.html', data=data)

# Iniciamos la aplicacion
if __name__ == '__main__':
    app.run(debug=True)
