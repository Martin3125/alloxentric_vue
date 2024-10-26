<template>
    <link rel="stylesheet" href="src/assets/resultados.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">

    <header>
        <div id="logo_header">
            <img src="@/assets/2.png" alt="logo">
            <h2>Alloxentric</h2>
        </div>
        <div id="menu">
            <!-- Menu content can be added here -->
        </div>
    </header>

    <div class="main">
        <Menu_P />
        <div class="general">
            <div class="general-resultados">
                <div class="pag-resultados">
                    <h5 style="margin-top: 3%;">Resultados del procesamiento</h5>
                </div>
                <div class="user">
                    <h5 style="margin-top: 3%;">Usuario</h5>
                </div>
            </div>

            <div class="tbl_resultados">
                <table class="table table-borderless" id="table">
                    <thead>
                        <tr>
                            <th style="border: 1px solid black;">Acción Predicha</th>
                            <th scope="col" style="border: 1px solid black;">Total Deudores</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(resultado, index) in predictions" :key="index">
                            <td style="border: 1px solid black;">{{ resultado.accion_predicha }}</td>
                            <td style="border: 1px solid black;">{{ resultado.total_deudores }}</td>
                        </tr>
                    </tbody>
                </table>
                <p v-if="predicciones.length === 0">No hay resultados disponibles.</p>

             
            </div>
        </div>
    </div>
</template>

<script>
import Menu_P from './Menu-.vue';
import axios from 'axios';

export default {
    name: 'resultados-',
    components: {
        Menu_P,
    },
    data() {
    return {
      predicciones: [], // Almacena las predicciones desde el backend
      predictions: JSON.parse(localStorage.getItem('predicciones')) || [], // Recupera las predicciones del local storage
    };
  },
  mounted() {
        this.fetchPredictions(); // Llamar a la función para obtener las predicciones cuando el componente se monte
    },
    methods: {
        async fetchPredicciones() {
            try {
                const response = await axios.get('/api/predicciones');
                if (response.data && response.data.predicciones) {
                    this.predicciones = response.data.predicciones; // Asigna las predicciones al array
                }
            } catch (error) {
                console.error('Error al obtener las predicciones:', error);
            }
        },
    },
}
</script>

<style scoped>

body {
	display: flex;
	justify-content: center;
	align-items: center;
	min-height: 100vh;
	font-family: "Raleway", sans-serif;
	background-color: #eef4fd;
}

.container {
	display: flex;
	flex-direction: column;
	box-shadow: 8px 8px 5px 0px #bdbdbdbf;
	width: 90%;
	background-color: #ffffff;
	border-radius: 30px;
  justify-content: center;
  margin: auto;
}

.table_header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 20px 30px 0;
}

button {
	outline: none;
	border: none;
	background-color: #27bb13;
	color: #ffffff;
	padding: 10px 30px;
	border-radius: 20px;
	text-transform: uppercase;
	font-size: 14px;
	cursor: pointer;
}

button:hover {
	background-color: #27bb13;
}

select {
	border: none;
	border-bottom: 1px solid #c9c9c9;
	width: 200px;
	padding: 10px 0;
	font-size: 16px;
}

.input_search {
	position: relative;
}

.input_search input {
	border-radius: 30px;
	width: 400px;
	outline: none;
	padding: 10px 20px;
	border: 1px solid #c9c9c9;
	box-sizing: border-box;
	padding-right: 50px;
}

.input_search #search {
	position: absolute;
	top: 50%;
	right: 0;
	margin-right: 1rem;
	transform: translate(-50%, -50%);
}

table {
	border-spacing: 0;
	margin-top: 1rem;
}

thead {
	background-color: #fff7b3;
}

th {
	padding: 10px;
}

tbody tr {
	border-bottom: 1px solid #dfdfdf;
}

tbody td {
	padding: 10px;
	border-bottom: 1px solid #dfdfdf;
	text-align: center;
}

tbody td #icons {
	font-size: 20px;
	cursor: pointer;
	margin-left: 10px;
	color: #797979;
}

tbody tr:hover {
	background-color: #f5f5f5;
}

.table_fotter {
	margin-top: 1rem;
	padding: 0 30px 20px;
}
</style>
