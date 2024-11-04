<template>
<div id="MENU_P">
        <div id="MenuPrincipal">
            <ul class="nav flex-column">
                <li class="nav-item">
                        <a class="nav-link d-flex align-items-center gap-2 active" aria-current="page" href="/" style="color: #ffffff;">
                            <svg class="bi"><use xlink:href="#house-fill"></use></svg>
                            Inicio
                        </a>
                        </li>
                        <li class="nav-item">
                        <a class="nav-link d-flex align-items-center gap-2" href="/cobranza" style="color: #ffffff;">
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
                                    <a color="#06B7B2" class="nav-link d-flex align-items-center gap-2" href="/cargar_resultados" style="color: #ffffff;">
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
                                    <a class="nav-link d-flex align-items-center gap-2" href="/generar_resultados" style="color: #ffffff;">
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
                                    <a class="nav-link d-flex align-items-center gap-2" href="/Reporte_de_la_ultima_carga" style="color: #ffffff;">
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
                                    <a class="nav-link d-flex align-items-center gap-2" href="/Reporte_de_d" style="color: #ffffff;">
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
                    <a class="nav-link d-flex align-items-center gap-2" href="/settings" style="color: #ffffff;">
                        <svg class="bi"><use xlink:href="#gear-wide-connected"></use></svg>
                        Settings
                    </a>
                    </li>
                    <li class="nav-item">
                    <a class="nav-link d-flex align-items-center gap-2" href="http://localhost:8080/realms/Alloxentric/account?referrer=security-admin-console&referrer_uri=http%3A%2F%2Flocalhost%3A8080%2Fadmin%2FAlloxentric%2Fconsole%2F%23%2FAlloxentric"  style="color: #ffffff;">
                        <svg class="bi"><use xlink:href="#door-closed"></use></svg>
                        Sign out
                    </a>
                    </li>
                </ul>
        </div>
   
</div>
</template>

<!-- <script>
// import Inicio from './Inicio-.vue';
// import Cobranza from './Cobranza-.vue';

export default {
  name: 'Menu_P',
  // Definición del componente
//   components: {
//     Inicio,
//     Cobranza,
//   }
  
 
}
</script> -->

<script>
export default {
  name: 'Menu_P',
  data() {
    return {
      isCollapsed: true,
    };
  },
  methods: {
    toggleSidebar() {
      this.isCollapsed = !this.isCollapsed;
    },
  },
};
</script>