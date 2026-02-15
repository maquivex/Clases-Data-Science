from flask import Flask,request,render_template
from mobile import MobilePrice

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    mobile = MobilePrice()
    brand_name = list(mobile.brand_name.keys())
    processor_name = list(mobile.processor_name.keys())
    os_name = list(mobile.os_name.keys())   
    
    precio = 0
    
    if request.method == 'POST':
        sistema = request.form['os_name']
        procesador = request.form['processor_name']
        marca = request.form['brand_name']
        banda = int(request.form['banda'])
        nucleos = int(request.form['nucleos'])
        memoria_ram = int(request.form['memoria_ram'])
        memoria_interna = int(request.form['memoria_interna'])
        bateria_tamaño = int(request.form['bateria_tamaño'])
        camera_trasera = int(request.form['camera_trasera'])
        camera_frontal = int(request.form['camera_frontal'])
        tamano_pantalla = float(request.form['tamano_pantalla'])

        precio = mobile.predict_price(sistema,procesador,marca,banda,nucleos,memoria_ram,memoria_interna,bateria_tamaño,camera_trasera,camera_frontal,tamano_pantalla)
    
    context = {
        'brand_name':brand_name,
        'processor_name':processor_name,
        'os_name':os_name,
        'precio':precio
    }
    return render_template('index.html',**context)

if __name__ == '__main__':
    app.run(debug=True)