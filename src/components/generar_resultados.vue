<template>
    <link rel="stylesheet" href="src\assets\generar_resultados.css">
   
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

            <div class="general-resultados">

                <div class="pag-resultados">
                    <p style="color: white; text-align: center;">Generar resultados</p>
                </div>
    
                <div class="user">
                    <h6 style="color: white; text-align: center; font-style: italic;">Usuario</h6>
                    <!-- <p style="color: white; text-align: center; font-size: 13px;">Trabajador</p> -->
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
                    <button class="btn btn-primary" style="width: 100%;" onclick="openModal()">Iniciar Ahora</button>
                </div>
                <div class="b_procesar">
                    <button class="btn btn-primary" style="width: 100%;" onclick="openModal2()">Iniciar Despues</button>
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
                <a class="btn btn-secondary" href="C:\Users\Equipo PC\Desktop\Alloxentric\Cobranza.html">SI</a>
                <a class="btn btn-primary"  type="submit" onclick="iniciarDespues()">NO</a>
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
                        <button class="btn btn-success"  style="width: 40%;" onclick="cerrarModalProgramar()">Confirmar</button>
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
                <a class="btn btn-secondary" href="C:\Users\Equipo PC\Desktop\Alloxentric\Cobranza.html">SI</a>
                <a class="btn btn-primary" href="resultados.html" type="submit">NO</a>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default {
  name: 'generar_resultados',
  // Definición del componente
}
</script>
  
<style>

</style>