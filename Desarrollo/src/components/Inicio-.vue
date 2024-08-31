<template>
   <link rel="stylesheet" href="src\assets\Inicio.css">
   <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;400;600&display=swap" rel="stylesheet">
    <header>
        <div id="logo_header">
          <img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\Desarrollo\src\assets\2.png" alt="logo" />
          <h2>Alloxentric</h2>
        </div>
        <div id="menu"></div>
    </header>
    <div class="my-component">
      <div id="general">
        <Menu_P/>
            <!-- Paginas -->
            <main id="cards">
                <div id="arriba">
                    <div class="card-body"  id="Titulo" >
                        <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" placeholder="Buscar">
                    </div>
                    <div class="card-body" id="usuario">
                        <h5 class="card-title2">Usuario</h5>
                    </div>
                </div>
                <div id="bodycard">
                    <div  id="card"  class="card">
                        <div class="card-body" >
                            <h5 class="card-title3">Últimos archivos subidos</h5>
                            <table id="documentTable">
                                <thead>
                                    <tr>
                                        <th>Archivos</th>
                                        <th>Fechas</th>
                                    </tr>
                                    <!-- <tr>
                                    <th>Documento 1 .csv</th>
                                    <th>24/06/2024</th>
                                    </tr>
                                    <tr>
                                    <th>Documento 2 .xlsx</th>
                                    <th>24/06/2024</th>
                                    </tr>
                                    <tr>
                                    <th>Documento 3 .csv</th>
                                    <th>24/06/2024</th>
                                    </tr> -->
                                </thead>
                                <!-- <tbody>
                                    <tr v-for="archivo in archivos" :key="archivo.Id_archivo">
                                        <td>{{ archivo.nombre }}</td>
                                        <td>{{ archivo.fecha }}</td>
                                    </tr>
                                </tbody> -->
                                <tbody>
                                  <tr v-for="archivo in archivos" :key="archivo.Id_archivo">
                                    <!-- <td>{{ archivo.Id_archivo }}</td> -->
                                    <td>{{ archivo.nombre }}</td>
                                    <td>{{ archivo.fecha }}</td>
                                  </tr>
                                </tbody>

                            </table>
                        </div>
                    </div>
                    <div  id="card2"  class="card2">
                    <div class="card-body" >
                        <h5 class="card-title3">Procesamientos programados</h5>
                            <table id="documentTable">
                            <thead>
                                <tr>
                                    <th>Nombre del procesamiento</th>
                                    <th>Fechas</th>
                                    <th>Hora</th>
                                    <th>Cancelar</th>
                                </tr>
                                <!-- <tr>
                                    <th>Proceso 1 </th>
                                    <th>24/06/2024</th>
                                    <th>12:50</th>
                                    <th><button type="download" class="btn btn-danger" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Cancelar</button></th>
                                </tr> -->
                                <!-- <tr>
                                    <th>Proceso 2 </th>
                                    <th>24/06/2024</th>
                                    <th>14:30</th>
                                    <th><button type="download" class="btn btn-danger" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Cancelar</button></th>
                                </tr> -->
                            </thead>
                                <tbody>
                                  <tr v-for="procesamiento in procesamientos" :key="procesamiento.Id_procesamiento">
                                    <!-- <td>{{ procesamiento.Id_procesamiento }}</td> -->
                                    <td>{{ procesamiento.nombre }}</td>
                                    <td>{{ procesamiento.fecha }}</td>
                                    <td>{{ procesamiento.hora }}</td>
                                    <td>
                                      <button @click="deleteProcesamiento(procesamiento.Id_procesamiento)" class="btn btn-danger" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">
                                        Cancelar
                                      </button>
                                    </td>
                                  </tr>
                                </tbody>   
                        </table>
                    </div>
                    </div>
                </div>
                </main>
      </div> 
</div>
</template>

<script>
import Menu_P from './Menu-.vue';
import axios from 'axios';

export default {
  name: 'Inicio-', // Definición del componente

  components: {
    Menu_P,
  },

  data() {
    return {
      archivos: [], 
      procesamientos: [], // Lista de documentos
    //   message: '',     // Mensaje de éxito
    };
  },
  mounted() {
    this.getArchivos(22); 
    this.getProcesamiento('66d294aaf0a12588663fde03'); 
     // Llamar al método cuando el componente se monte
  },
  methods: {
    async getArchivos(archivo_id) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/inicio/${archivo_id}`);
        console.log(response.data);  // Verifica el formato de los datos en la consola
        // Agrega el reporte a la lista, en caso de que sea un solo objeto
        if (Array.isArray(response.data)) {
          this.archivos = response.data;
        } else {
          this.archivos = [response.data];  // Convierte el objeto en un array
        }
      } catch (error) {
        console.error("Error al obtener los archivos:", error);
      }
    },

    async getProcesamiento(procesamiento_id) {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/procesamiento_P/${procesamiento_id}`);
        console.log(response.data);  // Verifica el formato de los datos en la consola
        // Agrega el reporte a la lista, en caso de que sea un solo objeto
        if (Array.isArray(response.data)) {
          this.procesamientos = response.data;
        } else {
          this.procesamientos = [response.data];  // Convierte el objeto en un array
        }
      } catch (error) {
        console.error("Error al obtener el procesamiento:", error);
      }
    },
    async deleteProcesamiento(procesamiento_id) {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/procesamiento_P/${procesamiento_id}`);
        // Eliminar el procesamiento localmente después de que se haya eliminado del backend
        this.procesamientos = this.procesamientos.filter(p => p.Id_procesamiento !== procesamiento_id);
        console.log("Procesamiento eliminado exitosamente.");
      } catch (error) {
        console.error("Error al eliminar el procesamiento:", error);
      }
    }
  }
}
</script>
<style>

</style>