import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.datasets import make_classification
from pymongo import MongoClient
import json

# Implementa el modelo K-means aquí
def run_kmeans(df_final):
    # Asegúrate de que df_final es tu DataFrame principal

    # Excluir columnas no relevantes como id_cliente y fecha_pago
    cols_to_exclude = ['id_cliente', 'fecha_pago']  # Puedes agregar más columnas si es necesario
    df_numeric = df_final.drop(columns=cols_to_exclude, errors='ignore')

    # Filtrar solo las columnas numéricas (float64 o int64) para aplicar KMeans
    df_numeric = df_numeric.select_dtypes(include=['float64', 'int64'])

    # Método del codo para encontrar el número óptimo de clusters
    inertia = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(df_numeric)
        inertia.append(kmeans.inertia_)

    # Seleccionar las variables relevantes
    selected_features = [
        'deudor',
        'PagoBinario',
        'TipoGestion_Administrativa',
        'TipoGestion_Compromiso',
        'TipoGestion_Compromiso-Com',
        'TipoGestion_EMAIL',
        'TipoGestion_Negativa',
        'TipoGestion_Negativa-Com',
        'TipoGestion_Positiva',
        'TipoGestion_Positiva-Adm',
        'TipoGestion_Positiva-Com',
        'TipoGestion_Positiva-Indi',
        'TipoGestion_Positiva-Wsp',
        'TipoGestion_Sistema',
        'TipoGestion_Terreno',
        'Sin acciones',
        'Correo electronico',
        'SMS',
        'Whatsapp',
        'Llamada por bot',
        'Llamada directa',
        'Acciones judiciales',
        'Cantidad_AccionesCobranza',
        'Cantidad_Gestiones',
        'gestion_positiva'
    ]

    # Filtrar el DataFrame con las variables seleccionadas
    df_filtered = df_final[selected_features]

    # Modelo k-means con 7 clusters
    kmeans7 = KMeans(n_clusters=7, random_state=42)
    df_filtered['cluster'] = kmeans7.fit_predict(df_filtered)

    # Se agrega el cluster correspondiente a cada deudor
    df_final['cluster'] = kmeans7.labels_
    print(f"df_final k-means: {df_final}")

    return df_final

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["alloxentric"]
modelo_collection = db["modelo"]

def obtener_ponderaciones():
    # Obtener el documento de ponderaciones desde MongoDB
    modelo = modelo_collection.find_one({})
    n_samples = modelo.get("n_samples", 10000)
    if modelo:
        # Extraer las ponderaciones
        ponderaciones = [
            modelo["pond_sin_acciones"],
            modelo["pond_correo_electronico"],
            modelo["pond_sms"],
            modelo["pond_whatsapp"],
            modelo["pond_llamada_por_bot"],
            modelo["pond_llamada_directa"],
            modelo["pond_acciones_judiciales"],
        ]
        
        # Normalizar las ponderaciones para que sumen 1
        total = sum(ponderaciones)
        ponderaciones_normalizadas = [p / total for p in ponderaciones]
        
        return ponderaciones_normalizadas, n_samples
    else:
        # Valores predeterminados y normalización
        ponderaciones = [0.85, 0.05, 0.05, 0.01, 0.01, 0.01, 0.02]
        total = sum(ponderaciones)
        ponderaciones_normalizadas = [p / total for p in ponderaciones]
        
        return ponderaciones_normalizadas, n_samples

    
# Implementa el modelo LSTM aquí
def run_lstm(df_final):
    # Suponiendo que df_final ya contiene las columnas de acciones
    acciones_columnas = [
        'Sin acciones',
        'Correo electronico',
        'SMS',
        'Whatsapp',
        'Llamada por bot',
        'Llamada directa',
        'Acciones judiciales'
    ]

    # Crear un diccionario de acciones
    acciones_dict = {
        'Sin acciones': 0,
        'Correo electronico': 1,
        'SMS': 2,
        'Whatsapp': 3,
        'Llamada por bot': 4,
        'Llamada directa': 5,
        'Acciones judiciales': 6,
    }

    # Diccionario inverso para convertir los números de vuelta a nombres de acciones
    acciones_dict_inverso = {v: k for k, v in acciones_dict.items()}

    # Determinar la etiqueta de acción
    df_final['etiqueta_accion'] = df_final[acciones_columnas].idxmax(axis=1)
    df_final['etiqueta_accion'] = df_final['etiqueta_accion'].map(acciones_dict)

    # Separar características y etiquetas
    X = df_final.drop(columns=['etiqueta_accion', 'fecha', 'Descripcion', 'fecha_pago', 'id_cliente'])
    y = df_final['etiqueta_accion']

    # Normalizar las características
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

     # Obtener ponderaciones y n_samples actualizados desde MongoDB
    ponderaciones_normalizadas, n_samples = obtener_ponderaciones()

    # Crear datos sintéticos para clases minoritarias
    n_samples = 10000  # Ajusta este valor según sea necesario
    X_synthetic, y_synthetic = make_classification(
        n_samples=n_samples,
        n_features=X.shape[1],
        n_classes=len(np.unique(y)),
        n_informative=X.shape[1] // 2,
        n_redundant=0,
        n_clusters_per_class=1,
        weights=ponderaciones_normalizadas,
        random_state=42
    )

    print(f"Ponderaciones: {ponderaciones_normalizadas}")
    print(f"N° Samples: {n_samples}")

    # Combinar datos originales con datos sintéticos
    X_combined = np.vstack((X_scaled, X_synthetic))
    y_combined = np.hstack((y, y_synthetic))

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_combined, y_combined, test_size=0.2, random_state=42)

    # Reshape de los datos para la entrada LSTM (n_samples, timesteps, features)
    X_train_reshaped = X_train.reshape((-1, 1, X_train.shape[1]))
    X_test_reshaped = X_test.reshape((-1, 1, X_test.shape[1]))

    # Definir el modelo LSTM
    model = models.Sequential()
    model.add(layers.LSTM(128, input_shape=(X_train_reshaped.shape[1], X_train_reshaped.shape[2]), return_sequences=False))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(len(np.unique(y)), activation='softmax'))

    # Compilar el modelo
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Resumen del modelo
    print(model.summary())

    # Entrenar el modelo
    model.fit(X_train_reshaped, y_train, epochs=10, batch_size=64, validation_split=0.2)

    # Evaluar el modelo
    y_pred = np.argmax(model.predict(X_test_reshaped), axis=1)
    report = classification_report(y_test, y_pred, output_dict=True)
    print("Test Metrics Report")
    print(classification_report(y_test, y_pred))

    with open('metrics_report.json', 'w') as f:
        json.dump(report, f)

    # Evaluar en datos de entrenamiento
    y_train_pred = np.argmax(model.predict(X_train_reshaped), axis=1)
    train_report = classification_report(y_train, y_train_pred, output_dict=True)
    print("Train Metrics Report")
    print(classification_report(y_train, y_train_pred))

    # Guardar el informe de entrenamiento en un archivo JSON
    with open('train_metrics_report.json', 'w') as f:
        json.dump(train_report, f)

        # Predecir usando el conjunto original
    # Asegúrate de que df_deudores contiene solo las columnas necesarias para la predicción
    df_deudores = df_final.copy()  # Crear una copia del DataFrame original
    X_deudores = df_deudores.drop(columns=['etiqueta_accion', 'fecha', 'Descripcion', 'fecha_pago', 'id_cliente'])

    # Normalizar las características de deudores usando el mismo scaler
    X_deudores_scaled = scaler.transform(X_deudores)

    # Reshape para predicciones
    X_deudores_reshaped = X_deudores_scaled.reshape((-1, 1, X_deudores_scaled.shape[1]))

    # Realizar predicciones con el modelo LSTM entrenado
    y_deudores_pred = np.argmax(model.predict(X_deudores_reshaped), axis=1)

    # Agregar las predicciones al DataFrame original
    df_deudores['accion_predicha'] = y_deudores_pred

    # Mapear los valores numéricos a los nombres de acciones

    df_deudores['accion_predicha'] = df_deudores['accion_predicha'].map(acciones_dict_inverso)

    # Agrupar deudores por acción predicha, separando los IDs por comas y contando el número de deudores
    df_group = df_deudores.groupby('accion_predicha').agg(
        deudores=('deudor', lambda x: ','.join(x.astype(str))),  # Concatenar IDs de deudores
        total_deudores=('deudor', 'count')  # Contar el total de deudores por acción
    ).reset_index()

    # Crear el DataFrame df_group
    df_group2 = pd.DataFrame(df_group)

    # Guardar df_group en un archivo CSV
    df_group2.to_csv('uploads/df_group.csv', index=False)

    return df_group


