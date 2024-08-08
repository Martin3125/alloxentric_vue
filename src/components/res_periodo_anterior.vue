<template>
    <link rel="stylesheet" href="src/assets/res_periodo_anterior.css">
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
                <!-- <li class="nav-item">
                <a class="nav-link d-flex align-items-center gap-2" href="documentos.html" style="color: #ffffff;">
                    <svg class="bi"><use xlink:href="#file-earmark"></use></svg>
                    Documentos
                </a>
                </li> -->
                <li class="nav-item">
                <a class="nav-link d-flex align-items-center gap-2" href="#" style="color: #ffffff;">
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
                            <a class="nav-link d-flex align-items-center gap-2" href="C:\Users\Equipo PC\Desktop\Allexontric\Cargar resultados del periodo anterior.html" style="color: #ffffff;">
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
                            <a class="nav-link d-flex align-items-center gap-2" href="Cargar resultados del periodo anterior.html" style="color: #ffffff;">
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
            <a class="nav-link d-flex align-items-center gap-2" href="#" style="color: #ffffff;">
                <svg class="bi"><use xlink:href="#door-closed"></use></svg>
                Sign out
            </a>
            </li>
        </ul>
        </div>
        
    
        <div class="general">

            <div class="general-resultados">

                <div class="pag-resultados">
                    <p style="color: white; text-align: center;">Resultados del período anterior</p>
                </div>
    
                <div class="user">
                    <h6 style="color: white; text-align: center; font-style: italic;">Usuario</h6>
                    <!-- <p style="color: white; text-align: center; font-size: 13px;">Trabajador</p> -->
                </div>
    
            </div>

            <div class="ver-resultados">
                <div class="titulos">
                    <div class="btn_volver">
                        <a class="btn btn-primary" href="C:\Users\Equipo PC\Desktop\Alloxentric\Cargar resultados del periodo anterior.html" style="width: 100%;">VOLVER</a>
                    </div>

                    <div class="text_resultados">
                        <h1 style="text-align: left;">Resultados del período anterior </h1>
                    </div>
                    
                    
                </div>
                
                <div class="tbl_resultados">
                    <table class="table table-borderless" id="table">
                        <thead>
                          <tr>
                            <th style="border: 1px solid black;">ID</th>
                            <th scope="col" style="border: 1px solid black;">Nombre del documento</th>
                            <th scope="col" style="border: 1px solid black;">Fecha</th>
                            <th scope="col" style="border: 1px solid black;">Registro de gente</th>
                            <th scope="col" style="border: 1px solid black;">Tipo de acción</th>
                            <th scope="col" style="border: 1px solid black;">Cantidad de gente a contactar</th>
                            <th>Descargar</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <th></th>
                            <td style="border: 1px solid black;">Documento 1</td>
                            <td style="border: 1px solid black;">01/07/2024</td>
                            <td style="text-align: center;">300</td>
                            <td style="border: 1px solid black;">Correo electrónico</td>
                            <td style="text-align: center;">100</td>
                            <td style="border: 1px solid black;"><a type="download" class="btn btn-primary" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Descargar</a></td>
                          </tr>
                          <tr>
                            <th scope="row">A001</th>
                            <td style="border: 1px solid black;">Documento 2</td>
                            <td style="border: 1px solid black;">01/07/2024</td>
                            <td style="text-align: center; border: 1px solid black;">300</td>
                            <td style="border: 1px solid black;">Whatsapp</td>
                            <td style="text-align: center; border: 1px solid black;">50</td>
                            <td style="border: 1px solid black;"><a type="download" class="btn btn-primary" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Descargar</a></td>
                          </tr>
                          <tr>
                            <th scope="row"></th>
                            <td style="border: 1px solid black;">Documento 3</td>
                            <td style="border: 1px solid black;">01/07/2024</td>
                            <td style="text-align: center; border: 1px solid black;">300</td>
                            <td style="border: 1px solid black;">Llamada por bot</td>
                            <td style="text-align: center; border: 1px solid black;">150</td>
                            <td style="border: 1px solid black;"><a type="download" class="btn btn-primary" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Descargar</a></td>
                          </tr>
                        </tbody>
                      </table>
                </div>
                
            </div>
    

            
        </div>


        

        

</div>

<div class="modal" tabindex="-1" id="modal_procesar">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h2>Iniciar procesamiento</h2>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body" style="padding: 10%;">

                <div class="btn_ahora" style="margin: auto; display: flex; justify-content: center;">
                    <a class="btn btn-secondary" href="#" style="width: 40%;">Iniciar ahora</a>
                </div>
                <br>

                <div class="btn_despues" style="margin: auto; display: flex; justify-content: center;">
                    <a class="btn btn-primary" href="#" type="submit" style="width: 40%;">Iniciar después</a>
                </div>
                <!-- <br>
                <br> -->
                
            </div>
            <!-- <div class="modal-footer">
                <a class="btn btn-secondary" href="#">SI</a>
                <a class="btn btn-primary" href="#" type="submit">NO</a>
            </div> -->
        </div>
    </div>
</div>
</template>
<script>
export default {
  name: 'Inicio-',
  // Definición del componente
}
</script>
  
<style>

</style>