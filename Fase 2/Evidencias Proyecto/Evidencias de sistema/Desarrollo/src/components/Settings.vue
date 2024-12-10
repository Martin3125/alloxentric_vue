<template>
    <!--Link fuentes de letras-->
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
    <!--Link settings.css-->
    <link rel="stylesheet" href="src/assets/settings.css">

    <!--Header-->
    <header>
        <div id="logo_header">
            <button class="toggle-btn" @click="toggleSidebar">
                <span class="icon" v-if="isCollapsed">☰</span>
                <span class="icon" v-else>✖</span>
            </button>
            <img src="@/assets/2.png" alt="logo">
            <h2>Alloxentric</h2>
        </div>
        <div class="input_search" >
        <input v-model="busqueda" type="search" placeholder="Buscar" />
        <i class="bi bi-search" id="search"></i>
        </div>
        <div class="card-body">
        <h5 class="card-title2">Usuario{{ usuarioLogueado }}</h5>
        </div>
    </header>

    <!--Menú-->
    <div class="main-settings">
        <Menu_P v-if="!isCollapsed"/>

        <div class="settings-content">

            <div class="container">
                <br>
                <!-- <form @submit.prevent="submitForm">
                     Ajuste de ponderaciones en porcentajes 
                    <h4>Pesos de las acciones (en porcentaje)</h4>
                    
                    <label for="sin_acciones">Sin acciones:</label>
                    <input type="number" id="sin_acciones" v-model.number="percentages[0]" step="1" min="0" max="100" @input="adjustPercentages(0)" @keydown.prevent>
                    <span>F1 Score: {{ f1Scores[0] }}</span>
                    <br>

                    <label for="correo_electronico">Correo electrónico:</label>
                    <input type="number" id="correo_electronico" v-model.number="percentages[1]" step="1" min="0" max="100" @input="adjustPercentages(1)" @keydown.prevent>
                    <span>F1 Score: {{ f1Scores[1] }}</span>
                    <br>

                    <label for="sms">SMS:</label>
                    <input type="number" id="sms" v-model.number="percentages[2]" step="1" min="0" max="100" @input="adjustPercentages(2)" @keydown.prevent>
                    <span>F1 Score: {{ f1Scores[2] }}</span>
                    <br>

                    <label for="whatsapp">Whatsapp:</label>
                    <input type="number" id="whatsapp" v-model.number="percentages[3]" step="1" min="0" max="100" @input="adjustPercentages(3)" @keydown.prevent>
                    <span>F1 Score: {{ f1Scores[3] }}</span>
                    <br>

                    <label for="llamada_bot">Llamada por bot:</label>
                    <input type="number" id="llamada_bot" v-model.number="percentages[4]" step="1" min="0" max="100" @input="adjustPercentages(4)" @keydown.prevent>
                    <span>F1 Score: {{ f1Scores[4] }}</span>
                    <br>

                    <label for="llamada_directa">Llamada directa:</label>
                    <input type="number" id="llamada_directa" v-model.number="percentages[5]" step="1" min="0" max="100" @input="adjustPercentages(5)" @keydown.prevent>
                    <span>F1 Score: {{ f1Scores[5] }}</span>
                    <br>

                    <label for="acciones_judiciales">Acciones judiciales:</label>
                    <input type="number" id="acciones_judiciales" v-model.number="percentages[6]" step="1" min="0" max="100" @input="adjustPercentages(6)" @keydown.prevent>
                    <span>F1 Score: {{ f1Scores[6] }}</span>
                    <br><br>

                    <button class="btn btn-secondary" type="button" @click="resetForm">Restablecer todo</button>
                    <button class="btn btn-primary" type="submit">Guardar cambios</button>
                </form>

                <div v-if="message" class="message">{{ message }}</div> -->
                
            <div style="display: flex; justify-content: center; gap: 20px;">
                <div >
                    <h3>Clases de acciones</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>Acción</th>
                                <th>Clase (Número)</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Sin acciones</td>
                                <td>0</td>
                            </tr>
                            <tr>
                                <td>Correo electrónico</td>
                                <td>1</td>
                            </tr>
                            <tr>
                                <td>SMS</td>
                                <td>2</td>
                            </tr>
                            <tr>
                                <td>Whatsapp</td>
                                <td>3</td>
                            </tr>
                            <tr>
                                <td>Llamada por bot</td>
                                <td>4</td>
                            </tr>
                            <tr>
                                <td>Llamada directa</td>
                                <td>5</td>
                            </tr>
                            <tr>
                                <td>Acciones judiciales</td>
                                <td>6</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                 <!-- Tabla de métricas Test Metrics Report-->
                 <div v-if="metrics">
                    <h2>Test Metrics Report</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Label</th>
                                <th>Precision</th>
                                <th>Recall</th>
                                <th>F1-Score</th>
                                <th>Support</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(value, key) in metrics" :key="key">
                                <td v-if="key !== 'accuracy' && key !== 'macro avg' && key !== 'weighted avg'">{{ key }}</td>
                                <td v-if="key !== 'accuracy' && key !== 'macro avg' && key !== 'weighted avg'">{{ value['precision'].toFixed(2) }}</td>
                                <td v-if="key !== 'accuracy' && key !== 'macro avg' && key !== 'weighted avg'">{{ value['recall'].toFixed(2) }}</td>
                                <td v-if="key !== 'accuracy' && key !== 'macro avg' && key !== 'weighted avg'">{{ value['f1-score'].toFixed(2) }}</td>
                                <td v-if="key !== 'accuracy' && key !== 'macro avg' && key !== 'weighted avg'">{{ value['support'] }}</td>
                            </tr>
                            <!-- Fila para la precisión general -->
                            <tr v-if="metrics.accuracy">
                                <td colspan="3">Accuracy</td>
                                <td>{{ metrics.accuracy.toFixed(2) }}</td>
                                <td>{{ metrics['weighted avg'] ? metrics['weighted avg']['support'] : metrics['macro avg']['support'] }}</td>
                            </tr>
                            <!-- Filas para promedios -->
                            <tr v-if="metrics['macro avg']">
                                <td>Macro Avg</td>
                                <td>{{ metrics['macro avg']['precision'].toFixed(2) }}</td>
                                <td>{{ metrics['macro avg']['recall'].toFixed(2) }}</td>
                                <td>{{ metrics['macro avg']['f1-score'].toFixed(2) }}</td>
                                <td>{{ metrics['macro avg']['support'] }}</td>
                            </tr>
                            <tr v-if="metrics['weighted avg']">
                                <td>Weighted Avg</td>
                                <td>{{ metrics['weighted avg']['precision'].toFixed(2) }}</td>
                                <td>{{ metrics['weighted avg']['recall'].toFixed(2) }}</td>
                                <td>{{ metrics['weighted avg']['f1-score'].toFixed(2) }}</td>
                                <td>{{ metrics['weighted avg']['support'] }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div v-else>
                    <p>Cargando métricas...</p>
                </div>



                 <!-- Tabla de métricas Train Metrics Report-->
                 <div v-if="metrics2">
                    <h2>Train Metrics Report</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Label</th>
                                <th>Precision</th>
                                <th>Recall</th>
                                <th>F1-Score</th>
                                <th>Support</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(value, key) in metrics2" :key="key">
                                <td v-if="key !== 'accuracy' && key !== 'macro avg' && key !== 'weighted avg'">{{ key }}</td>
                                <td v-if="key !== 'accuracy' && key !== 'macro avg' && key !== 'weighted avg'">{{ value['precision'].toFixed(2) }}</td>
                                <td v-if="key !== 'accuracy' && key !== 'macro avg' && key !== 'weighted avg'">{{ value['recall'].toFixed(2) }}</td>
                                <td v-if="key !== 'accuracy' && key !== 'macro avg' && key !== 'weighted avg'">{{ value['f1-score'].toFixed(2) }}</td>
                                <td v-if="key !== 'accuracy' && key !== 'macro avg' && key !== 'weighted avg'">{{ value['support'] }}</td>
                            </tr>
                            <!-- Fila para la precisión general -->
                            <tr v-if="metrics2.accuracy">
                                <td colspan="3">Accuracy</td>
                                <td>{{ metrics2.accuracy.toFixed(2) }}</td>
                                <td>{{ metrics2['weighted avg'] ? metrics2['weighted avg']['support'] : metrics2['macro avg']['support'] }}</td>
                            </tr>
                            <!-- Filas para promedios -->
                            <tr v-if="metrics2['macro avg']">
                                <td>Macro Avg</td>
                                <td>{{ metrics2['macro avg']['precision'].toFixed(2) }}</td>
                                <td>{{ metrics2['macro avg']['recall'].toFixed(2) }}</td>
                                <td>{{ metrics2['macro avg']['f1-score'].toFixed(2) }}</td>
                                <td>{{ metrics2['macro avg']['support'] }}</td>
                            </tr>
                            <tr v-if="metrics2['weighted avg']">
                                <td>Weighted Avg</td>
                                <td>{{ metrics2['weighted avg']['precision'].toFixed(2) }}</td>
                                <td>{{ metrics2['weighted avg']['recall'].toFixed(2) }}</td>
                                <td>{{ metrics2['weighted avg']['f1-score'].toFixed(2) }}</td>
                                <td>{{ metrics2['weighted avg']['support'] }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div v-else>
                    <p>Cargando métricas...</p>
                </div>
            </div>
                
            </div>
            </div>
            <div>
                
            </div>
            
        </div>
</template>

<script>
import Menu_P from './Menu-.vue';
import axios from 'axios';

export default {
    name: 'Settings',
    components: {
        Menu_P
    },
    data() {
        return {
            percentages: [85, 5, 5, 1, 1, 1, 2], // Valores iniciales en porcentaje
            weights: [], // Se calculará a partir de percentages
            f1Scores: [], // Aquí se almacenan los F1-scores correspondientes
            n_samples: 10000,
            message: '',
            loadedData: null,
            busqueda: "",
            isCollapsed: true,
            metrics: null, // Almacenará los datos de las métricas
            metrics2: null, // Almacenará los datos de las métricas
        };
    },
    methods: {
        async loadMetrics() {
            try {
                const response = await axios.get('http://localhost:8000/api/metrics');
                this.metrics = response.data;
            } catch (error) {
                console.error("Error al cargar las métricas:", error);
            }
        },
        async loadtrain_metrics_report() {
            try {
                const response = await axios.get('http://localhost:8000/api/train_metrics_report');
                this.metrics2 = response.data;
            } catch (error) {
                console.error("Error al cargar las métricas:", error);
            }
        },
        adjustPercentages(changedIndex) {
            let total = this.percentages.reduce((sum, val) => sum + val, 0);
            
            if (total !== 100) {
                const adjustment = 100 - total;
                const otherIndices = this.percentages
                    .map((_, i) => i)
                    .filter(i => i !== changedIndex);

                const currentTotalWithoutChanged = this.percentages
                    .filter((_, i) => i !== changedIndex)
                    .reduce((sum, val) => sum + val, 0);

                otherIndices.forEach(index => {
                    const proportion = this.percentages[index] / currentTotalWithoutChanged;
                    this.percentages[index] += Math.round(adjustment * proportion);
                });

                // Asegurarse de que el total vuelva a ser exactamente 100
                const finalTotal = this.percentages.reduce((sum, val) => sum + val, 0);
                if (finalTotal !== 100) {
                    this.percentages[changedIndex] += 100 - finalTotal;
                }
            }
        },
        async submitForm() {
        // Validar que la suma de porcentajes sea 100
        const totalPercentage = this.percentages.reduce((acc, p) => acc + p, 0);
        if (totalPercentage !== 100) {
            this.message = "La suma de los porcentajes debe ser igual a 100%";
            return;
        }

        // Convertir los porcentajes a pesos
        this.weights = this.percentages.map(p => p / 100);

        try {
            const formData = new FormData();
            this.weights.forEach((weight) => {
                formData.append(`weights`, weight);
            });
            formData.append('n_samples', this.n_samples);

            const response = await axios.post('http://localhost:8000/api/manipular-modelo', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            this.message = response.data.message;
            this.saveWeightsToLocal();
            this.loadWeights();
        } catch (error) {
            console.error(error);
            this.message = error.response ? error.response.data.detail : 'Error al guardar los cambios';
        }
    },
        
    async loadWeights() {
            try {
                const response = await axios.get('http://localhost:8000/api/modelo');
                this.loadedData = response.data;
                this.weights = [
                    this.loadedData.pond_sin_acciones,
                    this.loadedData.pond_correo_electronico,
                    this.loadedData.pond_sms,
                    this.loadedData.pond_whatsapp,
                    this.loadedData.pond_llamada_por_bot,
                    this.loadedData.pond_llamada_directa,
                    this.loadedData.pond_acciones_judiciales
                ];

                this.f1Scores = [
                    this.loadedData.f1_sin_acciones,
                    this.loadedData.f1_correo_electronico,
                    this.loadedData.f1_sms,
                    this.loadedData.f1_whatsapp,
                    this.loadedData.f1_llamada_por_bot,
                    this.loadedData.f1_llamada_directa,
                    this.loadedData.f1_acciones_judiciales
                ];

                this.n_samples = this.loadedData.n_samples || 10000;
                this.saveWeightsToLocal();
            } catch (error) {
                console.error(error);
                this.loadedData = null;
            }
        },

        saveWeightsToLocal() {
            localStorage.setItem('weights', JSON.stringify(this.weights));
            localStorage.setItem('n_samples', this.n_samples); // Guardar n_samples en localStorage
        },

        loadWeightsFromLocal() {
            const savedWeights = localStorage.getItem('weights');
            if (savedWeights) {
                this.weights = JSON.parse(savedWeights);
                this.percentages = this.weights.map(w => w * 100); // Convertir pesos a porcentajes
            }
            const savedSamples = localStorage.getItem('n_samples');
            if (savedSamples) {
                this.n_samples = parseInt(savedSamples);
            }
        },

        resetForm() {
            this.percentages = [85, 5, 5, 1, 1, 1, 2]; // Restablecer a valores iniciales
            this.n_samples = 10000;
        },

        toggleSidebar() {
        this.isCollapsed = !this.isCollapsed;
      },
    },
    mounted() {
        this.loadWeightsFromLocal();
        this.loadWeights();
        this.loadMetrics();//test
        this.loadtrain_metrics_report();//train
    }
}
</script>

<style scoped>
body {
    font-family: 'Nunito', sans-serif;
}
.actions-info-box {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        padding: 20px;
        border-radius: 8px;
        max-width: 500px;
        margin: auto;
    }
    
.actions-info-box h3 {
    text-align: center;
    font-size: 1.5em;
    margin-bottom: 20px;
}

/* Estilos del contenedor de tarjetas */

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
}

th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid #ddd;
}

th {
    background-color: #f2f2f2;
    font-weight: bold;
}

.settings-body {
    margin-top: 2%;
    padding: 10px; /* Espaciado reducido */
}

.form-group {
    display: flex;
    flex-direction: column; /* Verticaliza el contenido */
    margin-bottom: 5px; /* Espacio entre grupos de formulario */
}

label {
    font-size: 14px; /* Tamaño de fuente reducido */
    margin-bottom: 2px; /* Espaciado mínimo entre label y input */
}

input[type="number"] {
    padding: 5px; /* Espaciado interno reducido */
    font-size: 14px; /* Tamaño de fuente reducido para inputs */
    width: 100%; /* Ocupa el 100% del ancho */
}

.form-buttons {
    display: flex;
    justify-content: space-between; /* Espacio entre botones */
    margin-top: 10px; /* Espacio entre el formulario y los botones */
}

.btn {
    padding: 5px 10px; /* Tamaño de botón más pequeño */
    font-size: 14px; /* Tamaño de fuente reducido para botones */
}

.message {
    margin-top: 10px;
    color: green; /* Color para mensajes de éxito */
    font-size: 14px; /* Tamaño de fuente reducido para mensajes */
}

/* Ajustes específicos para pantallas pequeñas */
@media (max-width: 600px) {
    .settings-body {
        padding: 5px; /* Espaciado mínimo */
    }

    .form-group {
        margin-bottom: 3px; /* Espacio reducido */
    }

    input[type="number"] {
        font-size: 12px; /* Tamaño de fuente más pequeño */
    }

    .btn {
        padding: 4px 8px; /* Tamaño de botón aún más pequeño */
    }

    .message {
        font-size: 12px; /* Tamaño de fuente más pequeño para mensajes */
    }
}

.container {
    display: flex;
    flex-direction: column;
    box-shadow: 8px 8px 8px 8px #bdbdbdbf;
    width: 150%;
    max-width: 1200px; /* Limitar el ancho máximo */
    height: auto; /* Asegurarse de que la altura sea automática */
    min-height: 600px; /* Establece una altura mínima para evitar que el contenedor se vea pequeño */
    background-color: #ffffff;
    border-radius: 20px;
    margin: auto; /* Centrar horizontalmente */
    margin-top: 2%;
    padding: 20px; /* Espaciado interno */
    overflow: hidden; /* Evitar que se desborde el contenido */
    transition: all 0.3s ease; /* Transición suave */
}

/* Media Queries para Responsividad */
@media (max-width: 768px) {
  .list-group-item {
    flex: 1 1 100%; /* Ocupa el 100% en pantallas pequeñas */
  }

  #logo_header img {
    height: 40px; /* Reducción del tamaño del logo */
  }
}

@media (max-width: 480px) {
  header {
    flex-direction: column; /* Cambia a disposición vertical en pantallas muy pequeñas */
    align-items: flex-start; /* Alinear al inicio */
  }

  .input_search {
    margin: 10px 0; /* Espaciado vertical */
  }
}
</style>