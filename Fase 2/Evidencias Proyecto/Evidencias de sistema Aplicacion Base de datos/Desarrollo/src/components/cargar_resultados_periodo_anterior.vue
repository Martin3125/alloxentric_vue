<template>
    <link rel="stylesheet" href="src\assets\cargar_resultados_periodo_anterior.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;400;600&display=swap" rel="stylesheet">
<body>
    <header>
        <div id="logo_header">
            <img src="@/assets/2.png" alt="logo">
            <h2>Alloxentric</h2>
        </div>

        <div id="menu">
        </div>
        
    </header>
    

</body>
    <div class="main">
        <Menu_P  />

            <div class="general">

                <div id="arriba">
                    <div class="card-body"  id="Titulo1" >
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
                            <input class="form-control"  id="formFile" style="width: 100%;">
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
                    <a id="guardar" type="submit" class="btn btn-primary" href="/res_periodo_anterior">Confirmar</a>
                </div>   
            </div>  

        </div>
    </div>
            
          
</template>
<script>
import { directories, getFiles } from './js/directorios.js';
import Menu_P from './Menu-.vue';

export default {
  name: 'cargar_resultados', // Definición del componente
  components: {
    Menu_P,
 
  },
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


