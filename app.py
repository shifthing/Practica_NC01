from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
        return '¡Hola, mundo! Esta es mi primera app en la nube. Versión 2.0.'

if __name__ == '__main__':
    # La aplicación debe escuchar en el puerto 8080 para Heroku
    app.run(host='0.0.0.0', port=8080)
