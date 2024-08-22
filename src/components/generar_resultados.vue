<template>
    <link rel="stylesheet" href="src\assets\generar_resultados.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
    <body>
    <header>
        <div id="logo_header">
            <img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\2.png" alt="logo">
            <h2>Alloxentric</h2>
        </div>

        <div id="menu">
        </div>
        
    </header>
    

</body>
<div class="main">
    <Menu_P  />
        <div class="general">

            <div class="general-resultados">

                <div class="pag-resultados">
                    <h5 style="margin-top: 3%;">Generar resultados</h5>
                </div>
    
                <div class="user">
                    <h5 style="margin-top: 3%;">Usuario</h5>
                    
                </div>
    
            </div>
            <div class="resultados">
                <div class="main-documentos">
    
                    <div class="mb-3" id="select_documentos">
                        <input class="form-control" type="file" id="formFile" style="width: 100%;">
                    </div>
                    
                    <div class="mb-3" id="btn_documentos">
                        <button type="submit" id="btn_documentos" class="btn btn-secondary" style="width: 100%; background-color: black;">Subir</button>
                    </div>
    
                </div>
                <div class="main-procesamiento">
                    
                    <div class="lista-documentos">
                        <h2 style="text-align: center;">Documentos subidos</h2>
                        <br>
                        <div class="clear-doc">
                            <p>Documento 1</p>
                            <a href="#"><img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\clear.png" alt=""></a>
                        </div>

                        <div class="clear-doc">
                            <p>Documento 2</p>
                            <a href="#"><img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\clear.png" alt=""></a>
                        </div>

                        <div class="clear-doc">
                            <p>Documento 3</p>
                            <a href="#"><img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\clear.png" alt=""></a>
                        </div>

                        <div class="clear-doc">
                            <p>Documento 4</p>
                            <a href="#"><img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\clear.png" alt=""></a>
                        </div>

                        <div class="clear-doc">
                            <p>Documento 5</p>
                            <a href="#"><img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\clear.png" alt=""></a>
                        </div>

                        <div class="clear-doc">
                            <p>Documento 6</p>
                            <a href="#"><img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\clear.png" alt=""></a>
                        </div>
                    
                    </div>

                  
                </div>

                <div class="b_procesar">
                    <button class="btn btn-primary" style="width: 100%;" @click="openModal()">Iniciar Ahora</button>
                </div>
                <div class="b_procesar">
                    <button class="btn btn-primary" style="width: 100%;" @click="openModal2()">Iniciar Despues</button>
                </div>
            </div>  
        </div>
</div>

<div class="modal" tabindex="-1" id="modal_pesos2">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p>¿Quiere modificar los pesos de sus acciones de cobranza?</p>
            </div>
            <div class="modal-footer">
                <a class="btn btn-secondary" href="/cobranza">SI</a>
                <a class="btn btn-primary"  type="submit" @click="iniciarDespues()">NO</a>
           </div>
        </div>
    </div>
</div>

<div class="modal" tabindex="-1" id="modal_programar">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h2 style="text-align: center;">Programar procesamiento</h2>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body" style="padding: 10%;">

                <form action="" method="post">
                    <div class="btn_ahora" style="margin: auto; display: flex; justify-content: center;">
                        <input class="form-control" type="text" name="nombre_procesamiento" id="nombre_procesamiento" placeholder="Nombre del procesamiento">
                    </div>
                    <br>
                    <div class="btn_ahora" style="margin: auto; display: flex; justify-content: center;">
                        <input class="form-control" type="date" name="fecha_procesamiento" id="fecha_procesamiento">
                    </div>
                    <br>
                    <div class="btn_ahora" style="margin: auto; display: flex; justify-content: center;">
                        <input class="form-control" type="time" name="fecha_procesamiento" id="fecha_procesamiento">
                    </div>
                    <br>
    
                    <div class="btn_despues" style="margin: auto; display: flex; justify-content: center;">
                        <a class="btn btn-success"  href="/generar_resultados"  style="width: 40%;" @click="cerrarModalProgramar()">Confirmar</a>
                    </div>
                </form>
                
             
                
            </div>
           
        </div>
    </div>
</div>

<div class="modal" tabindex="-1" id="modal_pesos">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p>¿Quiere modificar los pesos de sus acciones de cobranza?</p>
            </div>
            <div class="modal-footer">
                <a class="btn btn-secondary" href="/cobranza">SI</a>
                <a class="btn btn-primary" href="/resultados" type="submit">NO</a>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import { openModal, openModal2, cerrarModal,  cerrarModal2 , cerrarModalProgramar, iniciarDespues} from './js/generar_resultados.js';
import Menu_P from './Menu-.vue';

export default {
  name: 'generar_resultados',
  components: {
    Menu_P,
  },
  data() {
    return {
      nombre: '',
      email: '',
      pwd: ''
    };
  },
  methods: {
    openModal,
    cerrarModal,
    openModal2,
    cerrarModal2,
    iniciarDespues,
    cerrarModalProgramar,
    async g_resultados() {
      try {
        const userData = {
          nombre: this.nombre,
          email: this.email,
          pwd: this.pwd
        };
        const respuesta = await fetch('http://127.0.0.1:8000/api/procesamiento', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(userData)
        });
        
        if (!respuesta.ok) {
          const errorData = await respuesta.json();
          console.error('Error en la respuesta:', errorData);
          this.errorMessage = errorData.detail || 'Error en el registro';
        } else {
          const data = await respuesta.json();
          console.log(data);
          this.$router.push('/');// Aquí puedes redirigir al usuario o limpiar el formulario
        }
      } catch (error) {
        console.error('Error en la solicitud:', error);
      }
    }
  }
};
</script>
  
<style>

</style>