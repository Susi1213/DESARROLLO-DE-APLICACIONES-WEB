from flask import Flask , request

app = Flask ( __name__ )


@app.route ( '/' )
def hello_world():
    return 'Hello World clase encuentro!!'


# Nueva ruta para mostrar un mensaje personalizado
@app.route ( '/usuario/<nombre>' )
def usuario(nombre):
    return f'Bienvenido, {nombre}!'


# Ruta para mostrar el formulario
@app.route ( '/usuario/' , methods = [ 'GET' , 'POST' ] )
def usuario_form():
    if request.method == 'POST':
        nombre = request.form [ 'nombre' ]
        return f'Bienvenido, {nombre}!!!'

    return '''
    <form method="post">
        <label for="nombre">Ingresa tu nombre:</label>
        <input type="text" id="nombre" name="nombre" required>
        <button type="submit">Enviar</button>
    </form>
    '''


if __name__ == '__main__':
    app.run ( debug = True )
