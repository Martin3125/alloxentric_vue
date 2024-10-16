<template>
    <link rel="stylesheet" href="src/assets/resultados.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
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

            <div class="general-resultados">

                <div class="pag-resultados">
                    <h5 style="margin-top: 3%;">Resultados del procesamiento</h5>
                </div>
    
                <div class="user">
                    <h5 style="margin-top: 3%;">Usuario</h5>
                    <!-- <p style="color: white; text-align: center; font-size: 13px;">Trabajador</p> -->
                </div>
    
            </div>

            <div class="ver-resultados">
                <div class="titulos">
                    <div class="btn_volver">
                        <a class="btn btn-primary" href="/generar_resultados" style="width: 100%;">VOLVER</a>
                    </div>

                    <div class="text_resultados">
                        <h1 style="text-align: left;">Resultados</h1>
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
                            <td style="border: 1px solid black;">28/07/2024</td>
                            <td style="text-align: center;">300</td>
                            <td style="border: 1px solid black;">Correo electrónico</td>
                            <td style="text-align: center;">100</td>
                            <td style="border: 1px solid black;"><button type="download" class="btn btn-primary" style="box-shadow: 2px 2px 2px black;"><img src="@/assets/btn_descargar.png" alt="" width="20px">Descargar</button></td>
                          </tr>
                          <tr>
                            <th scope="row">A001</th>
                            <td style="border: 1px solid black;">Documento 2</td>
                            <td style="border: 1px solid black;">28/07/2024</td>
                            <td style="text-align: center; border: 1px solid black;">300</td>
                            <td style="border: 1px solid black;">Whatsapp</td>
                            <td style="text-align: center; border: 1px solid black;">50</td>
                            <td style="border: 1px solid black;"><button type="download" class="btn btn-primary" style="box-shadow: 2px 2px 2px black;"><img src="@/assets/btn_descargar.png" alt="" width="20px">Descargar</button></td>
                          </tr>
                          <tr>
                            <th scope="row"></th>
                            <td style="border: 1px solid black;">Documento 3</td>
                            <td style="border: 1px solid black;">28/07/2024</td>
                            <td style="text-align: center; border: 1px solid black;">300</td>
                            <td style="border: 1px solid black;">Llamada por bot</td>
                            <td style="text-align: center; border: 1px solid black;">150</td>
                            <td style="border: 1px solid black;"><button type="download" class="btn btn-primary" style="box-shadow: 2px 2px 2px black;"><img src="@/assets/btn_descargar.png" alt="" width="20px">Descargar</button></td>
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
import Menu_P from './Menu-.vue';
export default {
  name: 'resultados-',// Definición del componente
  components: {
    Menu_P,

    
  }
}
</script>
<style>

</style>