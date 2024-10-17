from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from sklearn.externals import joblib

app = Flask(__name__)

# Cargar los modelos guardados
lstm_model = load_model('lstm_model.keras')
kmeans_model = joblib.load('kmeans_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Recibir datos en formato JSON
    features = data['features']  # Extraer características

    # Predicción con LSTM
    lstm_pred = lstm_model.predict(features)

    # Predicción con K-Means
    kmeans_pred = kmeans_model.predict(features)

    return jsonify({'lstm_prediction': lstm_pred.tolist(), 'kmeans_prediction': kmeans_pred.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
