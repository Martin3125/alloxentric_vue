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
            <!-- <div class="settings-header">
                <div class="pag-settings">
                    <h5 style="margin-top: 3%;">Settings</h5>
                </div>
                <div class="user">
                    <h5 style="margin-top: 3%;">Usuario</h5>
                </div>
            </div> -->

            <div class="settings-body">
                <h2>Modelos</h2>
                <br>
                <form @submit.prevent="submitForm">
                    <!-- Ajuste de ponderaciones en porcentajes -->
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

                <div v-if="message" class="message">{{ message }}</div>
            </div>
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
            isCollapsed: true
        };
    },
    methods: {
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
            this.weights.forEach((weight, index) => {
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
    }
}
</script>

<style scoped>
body {
    display: flex;
    justify-content: center; /* Centra el contenido horizontalmente en la página */
    align-items: center; /* Centra el contenido verticalmente */
    height: 100vh; /* Utiliza toda la altura de la ventana */
    margin: 0; /* Elimina el margen por defecto */
    background-color: #f0f0f0; /* Color de fondo para la página */
}

.settings-body {
    display: flex;
    flex-direction: column;
    align-items: center; /* Centra horizontalmente */
    justify-content: center; /* Centra verticalmente */
    padding: 12px;
    max-width: 800px; /* Ancho máximo para el formulario */
    width: 100%; /* Ancho relativo para que sea responsivo */
    height: auto; /* Ajuste automático de la altura */
    max-height: 95vh; /* Máxima altura para el formulario */
    overflow-y: auto; /* Agrega desplazamiento si es necesario */
    margin: auto; /* Centrando el contenedor en la página */
    border: 1px solid #ccc; /* Agrega un borde */
    border-radius: 8px; /* Bordes redondeados */
    background-color: #ffffff; /* Fondo blanco para el formulario */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra para dar profundidad */
    position: relative; /* Posición relativa para contener elementos internos */
    top: 5px; /* Separa del menú superior (ajusta según el espacio del menú) */
}

form {
    width: 100%; /* Tomar todo el ancho del contenedor */
}

label {
    margin: 8px 0; /* Espacio vertical entre etiquetas y campos */
}

input[type="number"] {
    width: 100%; /* Campos de entrada ocupan el ancho completo */
    padding: 10px; /* Relleno interno para los campos */
    margin-bottom: 10px; /* Espacio entre campos */
    border: 1px solid #ccc; /* Borde para los campos */
    border-radius: 4px; /* Bordes redondeados para los campos */
    box-sizing: border-box; /* Asegura que el padding y el border se incluyan en el ancho total */
}

button {
    width: 48%; /* Botones ocupan la mitad del ancho */
    padding: 10px; /* Relleno interno para botones */
    margin: 5px 1%; /* Espacio entre botones */
    border: none; /* Sin borde */
    border-radius: 4px; /* Bordes redondeados */
    cursor: pointer; /* Cambia el cursor al pasar sobre los botones */
}

.btn-secondary {
    background-color: #6c757d; /* Color de fondo del botón secundario */
    color: white; /* Color de texto del botón secundario */
}

.btn-primary {
    background-color: #007bff; /* Color de fondo del botón primario */
    color: white; /* Color de texto del botón primario */
}

.message {
    margin-top: 20px; /* Espacio superior para el mensaje */
    color: green; /* Color del mensaje de éxito */
    text-align: center; /* Centrar el texto del mensaje */
}

/* Responsividad para pantallas pequeñas */
@media (max-width: 600px) {
    .settings-body {
        padding: 10px; /* Relleno más pequeño en pantallas pequeñas */
    }

    button {
        width: 100%; /* Botones ocupan todo el ancho en pantallas pequeñas */
        margin: 5px 0; /* Espacio vertical entre botones */
    }
}

</style>