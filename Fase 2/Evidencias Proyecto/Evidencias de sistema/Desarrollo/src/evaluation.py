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


def evaluate_models(modeling):
    # Realiza la evaluación de los resultados de K-Means y LSTM
    # Resumen del modelo K-means
    # Aplicar PCA a los centroides para visualización en 2D
    centroids_pca7 = pca7.transform(centroids)

    # # Visualización de los clusters con PCA y los centroides
    # plt.figure(figsize=(10, 6))
    # sns.scatterplot(x='pca_1', y='pca_2', hue='cluster', data=df_filtered, palette='Set1', legend='full')

    # # Graficar los centroides en el mismo gráfico
    # plt.scatter(centroids_pca7[:, 0], centroids_pca7[:, 1], s=300, c='black', marker='X', label='Centroides')
    # plt.title('Visualización de Clústeres con PCA y Centroides')
    # plt.legend()
    # plt.show()

    print("Shape de los centroids:",centroids.shape)
    print("Centroides pca:",centroids_pca7)

    # Calcular la inercia (within-cluster sum of squares)
    inertia = kmeans7.inertia_
    print(f"Inercia: {inertia}")

    # Calcular el índice de silueta
    silhouette_avg = silhouette_score(df_filtered, df_filtered['cluster'])
    print(f"Índice de Silueta: {silhouette_avg}")

    # Calcular el índice de Calinski-Harabasz
    calinski_harabasz = calinski_harabasz_score(df_filtered, df_filtered['cluster'])
    print(f"Índice de Calinski-Harabasz: {calinski_harabasz}")

    # Calcular el índice de Davies-Bouldin
    davies_bouldin_index = davies_bouldin_score(df_filtered, df_filtered['cluster'])
    print(f"Davies-Bouldin Index: {davies_bouldin_index}")

    # Resumen del modelo LSTM
    print(model.summary())

    # Entrenar el modelo
    history = model.fit(X_train_reshaped, y_train, epochs=10, batch_size=64, validation_split=0.2)

    # Predecir las etiquetas en el conjunto de prueba
    y_pred_test = np.argmax(model.predict(X_test_reshaped), axis=1)

    # Predecir las etiquetas en el conjunto de entrenamiento
    y_pred_train = np.argmax(model.predict(X_train_reshaped), axis=1)

    # Mostrar métricas de rendimiento para el conjunto de prueba
    print("\nAccuracy Score (Test):", accuracy_score(y_test, y_pred_test))
    print("\nClassification Report (Test):\n", classification_report(y_test, y_pred_test))

    # Mostrar métricas de rendimiento para el conjunto de entrenamiento
    print("\nAccuracy Score (Train):", accuracy_score(y_train, y_pred_train))
    print("\nClassification Report (Train):\n", classification_report(y_train, y_pred_train))

    # # Graficar pérdida y precisión
    # plt.figure(figsize=(12, 6))

    # # Pérdida
    # plt.subplot(1, 2, 1)
    # plt.plot(history.history['loss'], label='Pérdida de entrenamiento')
    # plt.plot(history.history['val_loss'], label='Pérdida de validación')
    # plt.title('Pérdida durante el entrenamiento')
    # plt.xlabel('Épocas')
    # plt.ylabel('Pérdida')
    # plt.legend()

    # # Precisión
    # plt.subplot(1, 2, 2)
    # plt.plot(history.history['accuracy'], label='Precisión de entrenamiento')
    # plt.plot(history.history['val_accuracy'], label='Precisión de validación')
    # plt.title('Precisión durante el entrenamiento')
    # plt.xlabel('Épocas')
    # plt.ylabel('Precisión')
    # plt.legend()

    # plt.tight_layout()
    # plt.show()
    return modeling
