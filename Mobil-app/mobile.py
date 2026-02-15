import joblib
import numpy as np
import sklearn

# Load the best model and scalers
model = joblib.load('./model/model.pkl')
scaler_X = joblib.load('./model/scaler_X.pkl')
scaler_y = joblib.load('./model/scaler_y.pkl')

class MobilePrice:
    
  def __init__(self):
    self.brand_name = {
        'Samsung': [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Realme': [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Vivo': [0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Oppo': [0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Xiaomi': [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Motorola': [0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Poco ': [0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Oneplus': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Apple': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Iqoo': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Infinix': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Lava': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Tecno': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Google': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Nothing': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Alcatel': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Hmd': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0],
        'Honor': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],
        'Cmf': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],
        'Ai+': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],
        'Acer': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],
        'Itel': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]
    }

    self.processor_name = {
        'Dimensity': [1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Snapdragon': [0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],
        'Exynos': [0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0],
        'Bionic': [0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],
        'Unisoc': [0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],
        'Helio': [0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],
        'Tensor': [0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],
        'Tiger': [0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]
    }

    self.os_name = {
        'Android': [1.0,0.0],
        'iOS': [0.0,1.0]
    }


  def predict_price(self,sistema,procesador,marca,banda,nucleos,memoria_ram,memoria_interna,bateria_tamaño,camera_trasera,camera_frontal,tamano_pantalla):
    # Ensure new_data is a 2D array for scaling
    data_list = self.os_name[sistema] + self.processor_name[procesador] + self.brand_name[marca] + [banda,nucleos,memoria_ram,memoria_interna,bateria_tamaño,camera_trasera,camera_frontal,tamano_pantalla]
    new_mobile_data = np.array(data_list)
    new_data_array = np.array(new_mobile_data).reshape(1, -1)

    # Scale the input data
    new_data_scaled = scaler_X.transform(new_data_array)
    # Make prediction using the model
    prediction_scaled = model.predict(new_data_scaled)
    # Inverse transform the prediction to get original price scale
    prediction = scaler_y.inverse_transform(prediction_scaled.reshape(1, -1))

    return round(prediction[0][0],2) * 10000

# sistema = 'Android'
# procesador = 'Exynos'
# marca = 'Samsung'
# banda = 1
# nucleos = 4
# memoria_ram = 12
# memoria_interna = 128
# bateria_tamaño = 5000
# camera_trasera = 50
# camera_frontal = 20
# tamano_pantalla = 6.80

# new_mobile = MobilePrice()

# predicted_price = new_mobile.predict_price(sistema,procesador,marca,banda,nucleos,memoria_ram,memoria_interna,bateria_tamaño,camera_trasera,camera_frontal,tamano_pantalla)
# print(f"Predicted Price: {predicted_price:.3f} EUROS")
