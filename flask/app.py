from flask import Flask

app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def home():
#    return '¡Hola, mundo! :)'

@app.route('/usuario/<nombre>', methods=['GET'])
def usuario(nombre):
    return f'¡Hola, {nombre}! :)'

@app.route('/suma/<int:num1>/<int:num2>', methods=['GET'])
def suma(num1, num2):
    resultado = num1 + num2
    return f'La suma de {num1} y {num2} es: {resultado}'    

if __name__ == '__main__':
    app.run(debug=True) 


 