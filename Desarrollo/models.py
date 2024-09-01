from fastapi import FastAPI, HTTPException
from sklearn.cluster import KMeans
import tensorflow as tf
import numpy as np

app = FastAPI()

# Ejemplo de un modelo K-Means preentrenado
kmeans_model = KMeans(n_clusters=5)
# Carga o entrena tu modelo aquí

# Ejemplo de un modelo LSTM preentrenado
lstm_model = tf.keras.models.load_model('path_to_lstm_model.h5')

@app.post("/segment/")
def segment_customer(data: dict):
    # Preprocesa los datos de entrada según sea necesario
    features = np.array([data['feature1'], data['feature2'], data['feature3']])
    cluster = kmeans_model.predict([features])
    return {"cluster": int(cluster[0])}

@app.post("/predict/")
def predict_action(data: dict):
    # Preprocesa los datos secuenciales
    sequence = np.array([data['sequence']])  # Debe ser una secuencia compatible con LSTM
    prediction = lstm_model.predict(sequence)
    return {"predicted_action": prediction.tolist()}

# <template>
#   <div>
#     <button @click="getCluster">Segmentar Cliente</button>
#     <button @click="predictAction">Predecir Acción</button>
#   </div>
# </template>

# <script>
# import axios from 'axios';

# export default {
#   data() {
#     return {
#       customerData: {
#         feature1: 0,
#         feature2: 0,
#         feature3: 0,
#         sequence: [0.1, 0.2, 0.3, 0.4]
#       },
#       cluster: null,
#       predictedAction: null
#     };
#   },
#   methods: {
#     async getCluster() {
#       try {
#         const response = await axios.post('http://localhost:8000/segment/', this.customerData);
#         this.cluster = response.data.cluster;
#         console.log('Cluster:', this.cluster);
#       } catch (error) {
#         console.error(error);
#       }
#     },
#     async predictAction() {
#       try {
#         const response = await axios.post('http://localhost:8000/predict/', this.customerData);
#         this.predictedAction = response.data.predicted_action;
#         console.log('Predicted Action:', this.predictedAction);
#       } catch (error) {
#         console.error(error);
#       }
#     }
#   }
# };
# </script>

# <div v-if="cluster !== null">
#   <p>El cliente pertenece al clúster: {{ cluster }}</p>
# </div>
# <div v-if="predictedAction !== null">
#   <p>La acción de cobranza recomendada es: {{ predictedAction }}</p>
# </div>
