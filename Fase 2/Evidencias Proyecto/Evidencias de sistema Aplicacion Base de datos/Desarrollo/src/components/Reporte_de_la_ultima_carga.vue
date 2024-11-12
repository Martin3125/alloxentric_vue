<template>
    <link rel="stylesheet" href="src/assets/Reporte_de_la_ultima_carga.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
    <header>
        <div id="logo_header">
            <button class="toggle-btn" @click="toggleSidebar">
                <span class="icon" v-if="isCollapsed">☰</span>
                <span class="icon" v-else>✖</span>
            </button>
            <img src="@/assets/2.png" alt="logo">
            <h2>Alloxentric</h2>
        </div>
        <div class="input_search">
            <input v-model="busqueda" type="search" placeholder="Buscar" />
            <i class="bi bi-search" id="search"></i>
        </div>
        <div class="card-body">
            <h5 class="card-title2">Usuario: {{ usuarioLogueado }}</h5>
        </div>
    </header>
    <div id="general">
        <Menu_P v-if="!isCollapsed"/>
        <main id="cards">
            

            
                <div class="container">
                   
                    <!-- Header de la tabla -->
                    <div class="table_header">
                        <h2>Reporte de la última carga</h2>
                        <select v-model="tipoSeleccionado">
                            <option value="" selected>Tipo de acción</option>
                            <option value="Sin acciones">Sin acciones</option>
                            <option value="Correo electronico">Correo electrónico</option>
                            <option value="SMS">SMS</option>
                            <option value="Whatsapp">Whatsapp</option>
                            <option value="Llamada por bot">Llamada por bot</option>
                            <option value="Llamada directa">Llamada directa</option>
                            <option value="Acciones judiciales">Acciones judiciales</option>
                        </select>
                    </div>
                    
                    <!-- Tabla de resultados -->
                    <table>
                        <thead>
                            <tr>
                                <th>#</th>
                                <th>ID Procesamiento</th>
                                <th>Documento Cargado</th>
                                <th>Fecha de Carga</th>
                                <th>Deudores registrados</th>
                                <th>Acciones de Cobranza</th>
                                <th>Deudores por acción</th>
                                <!-- <th>Precio</th>
                                <th>Valor Multiplicado</th>  -->
                                <th>Operaciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(resultado, index) in paginatedResultados" :key="resultado.id_procesamiento">
                                <td>{{ (currentPage - 1) * itemsPerPage + index + 1 }}</td>
                                <td>{{ resultado.id_procesamiento }}</td>
                                <td>{{ resultado.documento_cargado }}</td>
                                <td>{{ resultado.fecha_carga }}</td>
                                <td>{{ resultado.registro_deudores }}</td>
                                <td>{{ resultado.accion_predicha}}</td> <!-- Campo corregido si es necesario -->
                                <td>{{ resultado.deudores_contactar }}</td>
                                
                                <td>
                                    <button @click="descargarPDF(resultado)">Descargar</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    
                      
                    <!-- Footer de la tabla con paginación -->
                    <div class="table_footer">
                        
                        <div class="pagination">
                            <button @click="changePage(1)" :disabled="currentPage === 1">Primera</button>
                            <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1">Anterior</button>
                            <span>Página {{ currentPage }} de {{ totalPages }}</span>
                            <button @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages">Siguiente</button>
                            <button @click="changePage(totalPages)" :disabled="currentPage === totalPages">Última</button>
                            
                        </div>

                        <!-- <p>Total de filas: {{ resultadosFiltrados.length }}</p> -->
                    </div>
                </div>
           
        </main>
    </div>
  </template>
  
  <script>
  import jsPDF from 'jspdf';
  import { initializeFilter } from './js/filtro.js';
  import Menu_P from './Menu-.vue';
  import axios from 'axios';
  
  export default {
    name: 'Reporte_ultima_carga',
    mounted() {
        initializeFilter();
        this.fetchResultados();
        this.cargarAcciones();
    },
    components: {
        Menu_P,
    },
    data() {
        return {
            busqueda: "",
            tipoSeleccionado: "",
            resultados: [],
            acciones: [],
            currentPage: 1,
            itemsPerPage: 7,
            isCollapsed: true,
        };
    },
    computed: {
        resultadosFiltrados() {
            return this.resultados.filter((resultado) => {
                const coincideBusqueda = resultado.documento_cargado.toLowerCase().includes(this.busqueda.toLowerCase());
                const coincideTipo = !this.tipoSeleccionado || resultado.accion_predicha === this.tipoSeleccionado;
                return coincideBusqueda && coincideTipo;
            });
        },
        paginatedResultados() {
            const start = (this.currentPage - 1) * this.itemsPerPage;
            const end = start + this.itemsPerPage;
            return this.resultadosFiltrados.slice(start, end);
        },
        totalPages() {
            return Math.ceil(this.resultadosFiltrados.length / this.itemsPerPage);
        }
    },
    methods: {
        async fetchResultados() {
            try {
                const response = await axios.get('http://localhost:8000/resultados');
                this.resultados = response.data;
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        },
        changePage(page) {
            this.currentPage = page;
        },
        editarResultado(resultado) {
            console.log("Editar resultado", resultado);
        },
        async eliminarResultado(id) {
            try {
                await axios.delete(`http://localhost:8000/resultados/${id}`);
                this.fetchResultados();
            } catch (error) {
                console.error('Error deleting result:', error);
            }
        },
        toggleSidebar() {
            this.isCollapsed = !this.isCollapsed;
        },
        async cargarAcciones() {
            try {
                const response = await axios.get('http://localhost:8000/api/acciones');
                this.acciones = response.data; // Asignar los datos a la propiedad acciones
            } catch (error) {
                console.error('Error al cargar acciones de cobranza:', error);
                // Manejo de errores, puedes mostrar un mensaje en la interfaz si lo deseas
            }
            },
        accionPorId(idAccion) {
            return this.acciones.find(accion => accion.Id_accion === idAccion);
        },
        descargarPDF(resultado) {
            const doc = new jsPDF();

            // Título principal en grande y en negrita
            doc.setFontSize(24);
            doc.setFont("helvetica", "bold");
            doc.text("Reporte de Carga", doc.internal.pageSize.getWidth() / 2, 20, { align: "center" });

            // Línea separadora debajo del título
            doc.setLineWidth(0.5);
            doc.line(20, 30, doc.internal.pageSize.getWidth() - 20, 30);

            // Cambiar fuente a tamaño normal y menos negrita para el contenido
            doc.setFontSize(12);
            doc.setFont("helvetica", "normal");

            // Espacio para cada campo con etiquetas en negrita y datos alineados
            const startY = 40; // Posición de inicio del contenido
            const lineSpacing = 10; // Espaciado entre líneas

            // Resumen de los datos cargados
            doc.setFont("helvetica", "bold");
            doc.text("ID Procesamiento:", 20, startY);
            doc.setFont("helvetica", "normal");
            doc.text(resultado.id_procesamiento.toString(), 70, startY);

            doc.setFont("helvetica", "bold");
            doc.text("Documento Cargado:", 20, startY + lineSpacing);
            doc.setFont("helvetica", "normal");
            doc.text(resultado.documento_cargado, 70, startY + lineSpacing);

            doc.setFont("helvetica", "bold");
            doc.text("Fecha de Carga:", 20, startY + lineSpacing * 2);
            doc.setFont("helvetica", "normal");
            doc.text(resultado.fecha_carga, 70, startY + lineSpacing * 2);

            doc.setFont("helvetica", "bold");
            doc.text("Deudores Registrados:", 20, startY + lineSpacing * 3);
            doc.setFont("helvetica", "normal");
            doc.text(resultado.registro_deudores.toString(), 70, startY + lineSpacing * 3);

            doc.setFont("helvetica", "bold");
            doc.text("Acciones de Cobranza:", 20, startY + lineSpacing * 4);
            doc.setFont("helvetica", "normal");
            doc.text(resultado.accion_predicha, 70, startY + lineSpacing * 4);

            doc.setFont("helvetica", "bold");
            doc.text("Deudores a contactar:", 20, startY + lineSpacing * 5);
            doc.setFont("helvetica", "normal");
            doc.text(resultado.deudores_contactar.toString(), 70, startY + lineSpacing * 5);

            // Agregar una nueva página para los deudores
            doc.addPage();

            // Introducción de la lista de deudores
            const startY2 = 20; // Iniciar la segunda página desde arriba
            doc.setFont("helvetica", "normal");
            doc.text("Los deudores que deberían ser contactados por " + resultado.accion_predicha + " son:", 20, startY2);

            // Ajustar la fuente para los deudores
            doc.setFontSize(10); // Reducir el tamaño de la fuente para los deudores

            let currentX = 20;
            let startLineY = startY2 + lineSpacing;  // Comenzamos desde abajo del texto introductorio
            const lineHeight = 6; // Ajustamos la altura de la línea
            let lineCount = 0;

            // Modificar  los  deudor en caso de tener informacíon como nombre, correo, teléfono, etc.
            // Convertir la lista de deudores a un arreglo de strings (si es necesario)
            let deudores = resultado.deudores.toString().split(',');

            // Definir número máximo de deudores por fila y columnas
            const maxDeudoresPorFila = 40;  // Ajustamos el máximo por fila
            const maxColumnas = 7;  // Ajustamos el número de columnas
            let columnCount = 0;
             
            
            deudores.forEach((deudor, index) => {
                // Imprimir cada deudor
                doc.text(deudor.trim(), currentX, startLineY + lineCount * lineHeight);

                lineCount++;
                // Si hemos alcanzado el máximo de deudores por fila, pasar a la siguiente columna
                if (lineCount >= maxDeudoresPorFila) {
                    lineCount = 0;
                    columnCount++;

                    // Si hemos usado 5 columnas, agregar una nueva página
                    if (columnCount >= maxColumnas) {
                        doc.addPage();
                        currentX = 20;  // Reiniciar posición X
                        startLineY = 20;  // Reiniciar posición Y
                        columnCount = 0;
                    } else {
                        currentX += (doc.internal.pageSize.getWidth() - 40) / maxColumnas; // Ajustar ancho de las columnas
                    }
                }
            });

            // Guardar el archivo PDF con un nombre personalizado
            doc.save(`${resultado.id_procesamiento}_${resultado.accion_predicha}.pdf`);
        }
    },
  };
  </script>
  


  <style scoped>

  body {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      font-family: "Raleway", sans-serif;
      background-color: #eef4fd;
      margin: 0;
  }
  
  
  .container {
  display: flex;
    flex-direction: column;
    box-shadow: 8px 8px 8px 8px #bdbdbdbf;
    width: 120%;
    max-width: 1400px; /* Limitar el ancho máximo */
    height: 90%;
    background-color: #ffffff;
    border-radius: 20px;
    margin: auto; /* Centrar horizontalmente */
    padding: 20px; /* Espaciado interno */
    overflow: hidden; /* Evitar que se desborde el contenido */
    }
  
  .table_header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px;
  }
  
  button {
      outline: none;
      border: none;
      background-color: #06B7B2;
      color: #ffffff;
      padding: 10px 30px;
      border-radius: 20px;
      text-transform: uppercase;
      cursor: pointer;
  }
  
  button:hover {
      background-color: #06B7B2;
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
  
  /* Contenedor de la tabla con scroll */
  .table_container {
      flex: 1; /* Permitir que crezca y ocupe el espacio disponible */
      overflow-y: auto; /* Habilitar desplazamiento vertical */
      margin-top: 1rem;
      margin-bottom: 1rem; /* Espacio para los botones de paginación */
      max-height: 55vh; /* Ajustar la altura máxima de la tabla */
  }
  
  table {
      border-spacing: 0;
      width: 100%; /* Asegurar que la tabla ocupe todo el ancho */
      height: 40%;
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
  
  /* Asegurarse de que el pie de la tabla y los botones de paginación estén separados */
  .table_footer {
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 10px 0;
  }
  
  .pagination {
      display: flex;
      gap: 10px; /* Espacio entre los botones de paginación */
  }
  
  .pagination button {
      padding: 5px 10px;
      border-radius: 5px;
      background-color: #06B7B2;
      color: white;
      border: none;
      cursor: pointer;
  }
  
  .pagination button:disabled {
      background-color: #c9c9c9;
      cursor: not-allowed;
  }
  
  .card-title2 {
      display: flex;
      justify-content: center;
      margin: auto;
      font-weight: 600;
  }
  
  </style>
  