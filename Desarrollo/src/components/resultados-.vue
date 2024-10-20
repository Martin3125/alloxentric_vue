<template>
    <link rel="stylesheet" href="src/assets/resultados.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
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
                <p v-if="predictions.length === 0">No hay resultados disponibles.</p>
            </div>
        </div>
    </div>
</template>

<script>
import Menu_P from './Menu-.vue';
export default {
    name: 'resultados',
    components: {
        Menu_P,
    },
    data() {
        return {
            predictions: JSON.parse(localStorage.getItem('predicciones')) || [], // Recupera las predicciones del local storage
        };
    },
}
</script>

<style>
/* Aquí puedes agregar estilos adicionales si es necesario */
</style>
