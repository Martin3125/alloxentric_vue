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
                        <form method="post" id="formLogin2" @submit.prevent="registerUser">
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
import axios from 'axios';

export default {
  name: 'Registro-',
  data() {
    return {
      nombre: '',
      email: '',
      pwd: '',
      passwordConfirm: '',
      errorMessage: ''
    };
  },
  methods: {
    async registerUser() {
      // Verificar que las contraseñas coincidan
      if (this.pwd !== this.passwordConfirm) {
        this.errorMessage = 'Las contraseñas no coinciden';
        return;
      }

      try {
        const response = await axios.post('http://localhost:3000/api/register', {
          nombre: this.nombre,
          email: this.email,
          pwd: this.pwd
        });

        // Redirigir al usuario a la página de Login después del registro exitoso
        if (response.data.success) {
          this.$router.push('/');
        } else {
          this.errorMessage = response.data.message;
        }
      } catch (error) {
        this.errorMessage = 'Hubo un error en el registro. Por favor, inténtelo nuevamente.';
        console.error('Error en el registro:', error);
      }
    }
  }
}
</script>
  
<style>

</style>

