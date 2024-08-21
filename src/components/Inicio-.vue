<template>
   <link rel="stylesheet" href="src\assets\Inicio.css">
   <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600&display=swap" rel="stylesheet">
    <header>
        <div id="logo_header">
          <img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\2.png" alt="logo" />
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
                            <h5 class="card-title3">Últimos documentos subidos</h5>
                            <table id="documentTable">
                                <thead>
                                    <tr>
                                        <th>Documentos</th>
                                        <th>Fechas</th>
                                    </tr>
                                    <tr>
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
                                    </tr>
                                </thead>
                                <tbody>
                                    <!-- Filas de datos irán aquí -->
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
                                <tr>
                                    <th>Proceso 1 </th>
                                    <th>24/06/2024</th>
                                    <th>12:50</th>
                                    <th><button type="download" class="btn btn-danger" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Cancelar</button></th>
                                </tr>
                                <tr>
                                    <th>Proceso 2 </th>
                                    <th>24/06/2024</th>
                                    <th>14:30</th>
                                    <th><button type="download" class="btn btn-danger" style="box-shadow: 2px 2px 2px black;"><img src="#" alt="" width="20px">Cancelar</button></th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Filas de datos irán aquí -->
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

export default {
  name: 'Inicio-', // Definición del componente

  components: {
    Menu_P,

    
  }
  
 
}

</script>
  
<style>
    
</style>