import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.datasets import make_classification


# Implementa el modelo K-means aquí

def run_kmeans(df_final):

# Asegúrate de que df_final es tu DataFrame principal

    # Excluir columnas no relevantes como id_cliente y fecha_pago
    cols_to_exclude = ['id_cliente', 'fecha_pago']  # Puedes agregar más columnas si es necesario
    df_numeric = df_final.drop(columns=cols_to_exclude, errors='ignore')

    # Filtrar solo las columnas numéricas (float64 o int64) para aplicar KMeans
    df_numeric = df_numeric.select_dtypes(include=['float64', 'int64'])

    # Escalar los datos numéricos
    # scaler = StandardScaler()
    # data_scaled = scaler.fit_transform(df_numeric)

    # Método del codo para encontrar el número óptimo de clusters
    inertia = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, random_state=42)
        kmeans.fit(df_numeric)
        inertia.append(kmeans.inertia_)
    

# Codigo para determinar el Clustering
    # Seleccionar los datos de df_copy
    df_selected = df_final

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
        'Correo electrÃ³nico',
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
    df_filtered = df_selected[selected_features]

    #Modelo k-means con 7 clusters

    # Normalización de los datos antes de aplicar K-means
    # scaler = StandardScaler()
    # df_filtered = scaler.fit_transform(df_filtered)

    # Aplicación del modelo K-means (con 3 clusters por ejemplo)
    kmeans7 = KMeans(n_clusters=7, random_state=42)
    df_filtered['cluster'] = kmeans7.fit_predict(df_filtered)

    # Obtener los centroides del modelo K-means
    centroids = kmeans7.cluster_centers_

    # Reducción de dimensionalidad con PCA a 2 componentes para visualización
    pca7 = PCA(n_components=3)
    pca_components = pca7.fit_transform(df_filtered)

    # Agregar las componentes principales al DataFrame para visualización
    df_filtered['pca_1'] = pca_components[:, 0]
    df_filtered['pca_2'] = pca_components[:, 1]

    #Se agrega el cluster correspondiente a cada deudor
    df_final['cluster'] = kmeans7.labels_

    return df_final


# Implementa el modelo LSTM aquí
def run_lstm(df_final):

    # Suponiendo que df_final ya contiene las columnas de acciones
    acciones_columnas = [
        'Sin acciones',
        'Correo electr贸nico',
        'SMS',
        'Whatsapp',
        'Llamada por bot',
        'Llamada directa',
        'Acciones judiciales'
    ]

    # Crear un diccionario de acciones
    acciones_dict = {
        'Sin acciones': 0,
        'Correo electr贸nico': 1,
        'SMS': 2,
        'Whatsapp': 3,
        'Llamada por bot': 4,
        'Llamada directa': 5,
        'Acciones judiciales': 6
    }

    # Crear una nueva columna 'etiqueta_accion' que combine las columnas
    # Primero, obtenemos la acci贸n correspondiente
    df_final['etiqueta_accion'] = df_final[acciones_columnas].idxmax(axis=1)

    # Convertir la acci贸n a su correspondiente etiqueta usando el diccionario
    df_final['etiqueta_accion'] = df_final['etiqueta_accion'].map(acciones_dict)


    # Supongamos que ya has creado la columna 'etiqueta_accion' como se describió anteriormente

    # Separar características y etiquetas
    X = df_final.drop(columns=['etiqueta_accion', 'fecha', 'Descripcion', 'fecha_pago', 'id_cliente'])
    y = df_final['etiqueta_accion']

    # Normalizar las características
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Crear datos sintéticos para clases minoritarias
    # Especificar el número de muestras sintéticas que deseas crear
    n_samples = 10000  # Ajusta este valor según sea necesario
    X_synthetic, y_synthetic = make_classification(n_samples=n_samples,
                                                n_features=X.shape[1],
                                                n_classes=len(np.unique(y)),
                                                n_informative=X.shape[1]//2,
                                                n_redundant=0,
                                                n_clusters_per_class=1,
                                                weights=[0.85, 0.05, 0.05, 0.05, 0.01, 0.01, 0.1],  # Ajusta según la distribución deseada
                                                random_state=42)

    # Combinar datos originales con datos sintéticos
    X_combined = np.vstack((X_scaled, X_synthetic))
    y_combined = np.hstack((y, y_synthetic))

    # Verificar la distribución de clases
    print("Distribución de clases combinadas:")
    print(pd.Series(y_combined).value_counts())

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_combined, y_combined, test_size=0.2, random_state=42)

    # Reshape de los datos para la entrada LSTM (n_samples, timesteps, features)
    X_train_reshaped = X_train.reshape((-1, 1, X_train.shape[1]))
    X_test_reshaped = X_test.reshape((-1, 1, X_test.shape[1]))

    # Definir el modelo LSTM
    model = models.Sequential()
    model.add(layers.LSTM(128, input_shape=(X_train_reshaped.shape[1], X_train_reshaped.shape[2]), return_sequences=False))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(len(np.unique(y)), activation='softmax'))  # Usamos softmax para clasificación multiclase

    # Compilar el modelo
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Entrenar el modelo
    history = model.fit(X_train_reshaped, y_train, epochs=10, batch_size=64, validation_split=0.2)

    # Predecir las etiquetas en el conjunto de prueba
    y_pred_test = np.argmax(model.predict(X_test_reshaped), axis=1)
    # Predecir las etiquetas en el conjunto de entrenamiento
    y_pred_train = np.argmax(model.predict(X_train_reshaped), axis=1)

    #  Mostrar métricas de rendimiento para el conjunto de prueba
    print("\nAccuracy Score (Test):", accuracy_score(y_test, y_pred_test))
    print("\nClassification Report (Test):\n", classification_report(y_test, y_pred_test))

    # Mostrar métricas de rendimiento para el conjunto de entrenamiento
    print("\nAccuracy Score (Train):", accuracy_score(y_train, y_pred_train))
    print("\nClassification Report (Train):\n", classification_report(y_train, y_pred_train))
    
    return df_final