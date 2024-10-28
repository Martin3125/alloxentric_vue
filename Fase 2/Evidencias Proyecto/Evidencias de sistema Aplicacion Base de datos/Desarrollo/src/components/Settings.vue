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
            loadedData: null, // Para cargar los datos guardados
            busqueda: "",
            isCollapsed: true
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