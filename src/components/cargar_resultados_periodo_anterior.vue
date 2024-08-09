<template>
    <link rel="stylesheet" href="src\assets\cargar_resultados_periodo_anterior.css">

<body>
    <header>
        <div id="logo_header">
            <img src="C:\Users\Equipo PC\Desktop\Alloxentric\2.png" alt="logo">
            <h2>Alloxentric</h2>
        </div>

        <div id="menu">
        </div>
        
    </header>
    

</body>
    <div class="main">
        <div id="MenuPrincipal">
                <ul class="nav flex-column">
                    <li class="nav-item">
                    <a class="nav-link d-flex align-items-center gap-2 active" aria-current="page" href="inicio.html" style="color: #ffffff;">
                        <svg class="bi"><use xlink:href="#house-fill"></use></svg>
                        Inicio
                    </a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\Cobranza.html" style="color: #ffffff;">
                        <svg class="bi"><use xlink:href="#cart"></use></svg>
                        Cobranza
                    </a>
                    </li>
                    <li class="nav-item">
                    <div class="accordion accordion-flush" id="accordionFlushExample" >
                        <div class="accordion-item" style="background-color: #06B7B2; color: #ffffff;"  >
                        <h2 class="accordion-header" id="procesamiento">
                            <button class="accordion-button collapsed" style="background-color: #06B7B2; margin-left: 6%; width: 93%; color: #ffffff;" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne" >
                            Procesamiento
                            </button>
                        </h2>
                        <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                            <div class="accordion-body" >
                            <ul class="list-group">
                                <li class="nav-item">
                                <a color="#06B7B2" class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\Cargar resultados del periodo anterior.html" style="color: #ffffff;">
                                    <svg class="bi"><use xlink:href="#cart"></use></svg>
                                    Cargar resultados del periodo anterior
                                </a>
                                </li>
                            </ul>
                            </div>
                        </div>
                        <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                            <div class="accordion-body">
                            <ul class="list-group">
                                <li class="nav-item">
                                <a class="nav-link d-flex align-items-center gap-2" href="generar_resultados.html" style="color: #ffffff;">
                                    <svg class="bi"><use xlink:href="#cart"></use></svg>
                                    Generar resultados del periodo
                                </a>
                                </li>
                            </ul>
                            </div>
                        </div>
                        </div>
                        <div class="accordion-item" style="background-color: #06B7B2; color: #ffffff;">
                        <h2 class="accordion-header">
                            <button class="accordion-button collapsed" style="background-color: #06B7B2; color: #ffffff;  margin-left: 6%; width: 93%;" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
                            Informes
                            </button>
                        </h2>
                        <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                            <div class="accordion-body">
                            <ul class="list-group">
                                <li class="nav-item">
                                <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\Reporte de la ultima carga.html" style="color: #ffffff;">
                                    <svg class="bi"><use xlink:href="#cart"></use></svg>
                                    Reporte de la ultima carga
                                </a>
                                </li>
                            </ul>
                            </div>
                        </div>
                        <div id="flush-collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                            <div class="accordion-body">
                            <ul class="list-group">
                                <li class="nav-item">
                                <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\Reporte de desempeño.html" style="color: #ffffff;">
                                    <svg class="bi"><use xlink:href="#cart"></use></svg>
                                    Reporte de desempeño
                                </a>
                                </li>
                            </ul>
                            </div>
                        </div>
                        </div>
                    </div>
                    </li> 
                </ul>
                
                <hr class="my-3">
        
            <ul class="nav flex-column mb-auto">
                <li class="nav-item">
                <a class="nav-link d-flex align-items-center gap-2" href="#" style="color: #ffffff;">
                    <svg class="bi"><use xlink:href="#gear-wide-connected"></use></svg>
                    Settings
                </a>
                </li>
                <li class="nav-item">
                <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Alloxentric\Login.html" style="color: #ffffff;">
                    <svg class="bi"><use xlink:href="#door-closed"></use></svg>
                    Sign out
                </a>
                </li>
            </ul>
        </div>

            <div class="general">

                <div id="arriba">
                    <div class="card-body"  id="Titulo" >
                        <h5 class="card-title1">Cargar resultados</h5>
                    </div>
                    <div class="card-body" id="usuario">
                        <h5 class="card-title2">Usuario</h5>
                    </div>
                </div>


                <div class="resultados">

                <form action="" method="post">
                    <div class="main-resultados">
                        <div class="mb-3" id="select_resultados">
                            <input class="form-control" type="file" id="formFile" style="width: 100%;">
                        </div>
                        <!-- <div class="input-container">
                            <input type="text" id="filePathInput" placeholder="Ingrese la ruta del archivo">
                            <button @click="openModal()">Ver Contenido</button>
                        </div> -->
                    </div>


                    <div class="main-directorios">

                        <div class="lugar">

                            <div class="home">
                                <h3 style="color: white; text-align: center;">Home</h3>
                            </div>

                            <div class="dir">
                                <h3 style="color: white; text-align: center;">Directorios</h3>
                            </div>

                            
                        </div>
                        


                        <div class="directorios">
                        

                            <div class="carpetas">
                                <h3 style="text-align: center;">Directorios</h3>
                                <div style="text-align: center;"
                                    v-for="directory in directories"
                                    :key="directory"
                                    :class="{ selected: directory === selectedDirectory }"
                                    class="directory"
                                    id="directories"
                                    @click="selectDirectory(directory)"
                                >
                                    {{ directory }}
                                </div>
                            </div>

                            <div class="archivos">
                                <h4 style="text-align: center;" >Archivos</h4>
                                <div style="text-align: center;" id="files"  v-for="file in currentFiles" :key="file" class="file">
                                    {{ file }}
                                </div>
                            </div>
                            
                        </div>
                    </div>

                </form>

                <div class="b_confirmar">
                    <a class="btn btn-primary" style="width: 50%; align-self: center; background-color: rgb(22, 201, 22); border: 1px solid rgb(22, 201, 22)" href="res_periodo_anterior.html">Confirmar</a>
                </div>   
            </div>  

        </div>
    </div>
            
          
</template>
<script>
import { directories, getFiles } from './js/directorios.js';

export default {
  name: 'cargar_resultados', // Definición del componente
  data() {
    return {
      directories: directories,
      selectedDirectory: null,
      currentFiles: []
    };
  },
  methods: {
    selectDirectory(directory) {
      this.selectedDirectory = directory;
      this.currentFiles = getFiles(directory);
    }
  }
};
</script>

<style>

</style>


