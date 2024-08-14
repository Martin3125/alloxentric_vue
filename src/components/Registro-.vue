<template>
    <link rel="stylesheet" href="src/assets/Registro.css">
     <div class="container-fluid h-100">
        <div class="row h-100 justify-content-end">
            <div class="card1">
                <img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\alloxentric_logo-3x.png" class="card-img" alt="...">   
            </div>
            <div class="col-md-4 d-flex align-items-center p-0">
                <div class="card w-100">
                    <div class="card-body">
                        <form method="post" id="formLogin2" @submit.prevent="registrarUsuario">
                            <div id="logo_header" class="text-center mb-4">
                                <img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\2.png" alt="logo">
                                <h2>Alloxentric</h2>
                            </div>
                            <div class="form-group mb-3" id="formCorreo">
                                <label for="exampleInputEmail1">Nombre</label>
                                <input v-model="nombre" name="nombre" type="nombre" class="form-control" id="inputCorreo" aria-describedby="emailHelp" placeholder="Ingrese su Nombre">
                            </div>
                            <div class="form-group mb-3" id="formCorreo">
                                <label for="exampleInputEmail1">Correo electrónico</label>
                                <input v-model="email" name="email" type="email" class="form-control" id="inputCorreo" aria-describedby="emailHelp" placeholder="Ingrese su correo">
                            </div>
                            <div class="form-group mb-3" id="formContraseña">
                                <label for="exampleInputPassword1">Contraseña</label>
                                <input v-model="pwd" name="pwd" type="password" class="form-control" id="inputContraseña" placeholder="Ingrese su contraseña">
                            </div>
                            <div class="form-group mb-3" id="formContraseña">
                                <label for="exampleInputPassword1">Repetir Contraseña</label>
                                <input v-model="passwordConfirm" name="password" type="password" class="form-control" id="inputContraseña" placeholder="Repita su contraseña">
                            </div>
                            <!-- <button type="submit" class="btn btn-primary w-100 mb-2" id="btnIniciarSesion" >Iniciar sesión</button> -->
                            <button  type="submit" class="btn btn-primary w-100 mb-2" id="btnRegistrarse">Registrar</button>
                            <a  class="btn btn-secondary w-100" id="btnRegistrarse" href="/">Volver</a>
                            <label  v-if="errorMessage" style="text-align: center; color: red;">{{ errorMessage }}</label>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {

  name: 'Registro-',// Definición del componente
  data() {
    return {
      nombre: '',
      email: '',
      pwd: ''
    };
  },
  methods: {
    async registrarUsuario() {
      try {
        const userData = {
          nombre: this.nombre,
          email: this.email,
          pwd: this.pwd
        };
        const respuesta = await fetch('http://127.0.0.1:8000/api/register', {
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

