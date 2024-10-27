<template>
    <!--Link fuentes de letras-->
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
    <!--Link settings.css-->
    <link rel="stylesheet" href="src/assets/settings.css">

    <!--Header-->
    <header>
        <div id="logo_header">
            <img src="@/assets/2.png" alt="logo">
            <h2>Alloxentric</h2>
        </div>
    </header>

    <!--Menú-->
    <div class="main-settings">
        <Menu_P />

        <div class="settings-content">
            <div class="settings-header">
                <div class="pag-settings">
                    <h5 style="margin-top: 3%;">Settings</h5>
                </div>
                <div class="user">
                    <h5 style="margin-top: 3%;">Usuario</h5>
                </div>
            </div>

            <div class="settings-body">
                <h2>Modelos</h2>
                <br>
                <form @submit.prevent="submitForm">

                    <!--Ajuste de ponderaciones o weights para el balanceo de clases-->
                    <h4>Ponderaciones de clases</h4>
                    <label for="sin_acciones">Sin acciones:</label>
                    <input type="number" id="sin_acciones" v-model="weights[0]" step="0.01">
                    <br>

                    <label for="correo_electronico">Correo electrónico:</label>
                    <input type="number" id="correo_electronico" v-model="weights[1]" step="0.01">
                    <br>

                    <label for="sms">SMS:</label>
                    <input type="number" id="sms" v-model="weights[2]" step="0.01">
                    <br>

                    <label for="whatsapp">Whatsapp:</label>
                    <input type="number" id="whatsapp" v-model="weights[3]" step="0.01">
                    <br>

                    <label for="llamada_bot">Llamada por bot:</label>
                    <input type="number" id="llamada_bot" v-model="weights[4]" step="0.01">
                    <br>

                    <label for="llamada_directa">Llamada directa:</label>
                    <input type="number" id="llamada_directa" v-model="weights[5]" step="0.01">
                    <br>

                    <label for="acciones_judiciales">Acciones judiciales:</label>
                    <input type="number" id="acciones_judiciales" v-model="weights[6]" step="0.01">
                    <br><br>


                    <!--Ajustes de n° samples para balancear clases-->
                    <h4>Ajuste de datos sintéticos</h4>
                    <label for="n_samples">Número de muestras sintéticas:</label>
                    <input type="number" id="n_samples" v-model="n_samples" step="1" min="1" value="10000">
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
            weights: [0.85, 0.05, 0.05, 0.05, 0.01, 0.01, 0.1], // Inicializa los pesos
            n_samples: 10000, // Inicializa n_samples
            message: '',
            loadedData: null // Para cargar los datos guardados
        };
    },
    methods: {
        async submitForm() {
            try {
                const formData = new FormData();
                this.weights.forEach((weight, index) => {
                    formData.append(`weights`, weight);
                });
                formData.append('n_samples', this.n_samples); // Añadir n_samples a formData

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
                this.n_samples = this.loadedData.n_samples || 10000; // Cargar n_samples si existe
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
            }
            const savedSamples = localStorage.getItem('n_samples');
            if (savedSamples) {
                this.n_samples = parseInt(savedSamples); // Cargar n_samples de localStorage
            }
        },

        resetForm() {
            // Restablecer los valores predeterminados
            this.weights = [0.85, 0.05, 0.05, 0.05, 0.01, 0.01, 0.1];
            this.n_samples = 10000; // Restablecer n_samples
        }
    },
    mounted() {
        this.loadWeightsFromLocal();
        this.loadWeights();
    }
}
</script>
