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

                    <h2>Configura los Pesos para las Acciones</h2>

                    <form @submit.prevent="submitForm">
                        <label for="sin_acciones">Peso para Sin acciones:</label>
                        <input type="number" id="sin_acciones" v-model="weights[0]" step="0.01" value="0.85">
                        <br>

                        <label for="correo_electronico">Peso para Correo electrónico:</label>
                        <input type="number" id="correo_electronico" v-model="weights[1]" step="0.01" value="0.05">
                        <br>

                        <label for="sms">Peso para SMS:</label>
                        <input type="number" id="sms" v-model="weights[2]" step="0.01" value="0.05">
                        <br>

                        <label for="whatsapp">Peso para Whatsapp:</label>
                        <input type="number" id="whatsapp" v-model="weights[3]" step="0.01" value="0.05">
                        <br>

                        <label for="llamada_bot">Peso para Llamada por bot:</label>
                        <input type="number" id="llamada_bot" v-model="weights[4]" step="0.01" value="0.01">
                        <br>

                        <label for="llamada_directa">Peso para Llamada directa:</label>
                        <input type="number" id="llamada_directa" v-model="weights[5]" step="0.01" value="0.01">
                        <br>

                        <label for="acciones_judiciales">Peso para Acciones judiciales:</label>
                        <input type="number" id="acciones_judiciales" v-model="weights[6]" step="0.01" value="0.1">
                        <br>

                        <button class="btn btn-primary" type="submit">Guardar cambios</button>
                    </form>

                    <div v-if="message" class="message">{{ message }}</div>

                    <div v-if="loadedData">
                        <h3>Pesos Guardados:</h3>
                        <ul>
                            <li>Peso para Sin acciones: {{ loadedData.pond_sin_acciones }}</li>
                            <li>Peso para Correo electrónico: {{ loadedData.pond_correo_electronico }}</li>
                            <li>Peso para SMS: {{ loadedData.pond_sms }}</li>
                            <li>Peso para Whatsapp: {{ loadedData.pond_whatsapp }}</li>
                            <li>Peso para Llamada por bot: {{ loadedData.pond_llamada_por_bot }}</li>
                            <li>Peso para Llamada directa: {{ loadedData.pond_llamada_directa }}</li>
                            <li>Peso para Acciones judiciales: {{ loadedData.pond_acciones_judiciales }}</li>
                        </ul>
                    </div>

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
            message: '',
            loadedData: null // Para cargar los datos guardados
        };
    },
    methods: {
        async submitForm() {
            try {
                const formData = new FormData();
                this.weights.forEach((weight, index) => {
                    formData.append(`weights`, weight); // 'weights' es el nombre del campo esperado en FastAPI
                });

                const response = await axios.post('http://localhost:8000/api/manipular-modelo', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data' // Asegúrate de que el tipo de contenido sea correcto
                    }
                });
                this.message = response.data.message; // Muestra el mensaje de éxito
                this.loadWeights(); // Carga los pesos después de guardar
            } catch (error) {
                console.error(error); // Para depurar
                this.message = error.response ? error.response.data.detail : 'Error al guardar los cambios';
            }
        },
        
        async loadWeights() {
            try {
                const response = await axios.get('http://localhost:8000/api/modelo');
                this.loadedData = response.data; // Carga los datos guardados
            } catch (error) {
                console.error(error); // Para depurar
                this.loadedData = null; // Resetear si hay error
            }
        }
    },
    mounted() {
        this.loadWeights(); // Cargar los pesos cuando el componente se monta
    }
}
</script>

