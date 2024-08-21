<template>
    <link rel="stylesheet" href="src/assets/Login.css">
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@200;400;600&display=swap" rel="stylesheet">
    <div class="container-fluid h-100">
        <div class="row h-100 justify-content-end">
            <div class="card1">
                <img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\alloxentric_logo-3x.png" class="card-img" alt="...">   
            </div>
            <div class="col-md-4 d-flex align-items-center p-0">
                <div class="card w-100">
                    <div class="card-body">
                        <form method="post" id="formLogin" @submit.prevent="login">
                            <div id="logo_header" class="text-center mb-4">
                                <img src="C:\Users\Equipo PC\Desktop\Proyecto Vue\alloxentric\src\assets\2.png" alt="logo">
                                <h2>Alloxentric</h2>
                            </div>
                            <div class="form-group mb-3" id="formCorreo">
                                <label for="exampleInputEmail1">Correo electrónico</label>
                                <input v-model="email" name="email" type="email" class="form-control" id="inputCorreo" aria-describedby="emailHelp" placeholder="Ingrese su correo">
                            </div>
                            <div class="form-group mb-3" id="formContraseña">
                                <label for="exampleInputPassword1">Contraseña</label>
                                <input v-model="pwd" name="pwd" type="password" class="form-control" id="inputContraseña" placeholder="Ingrese su contraseña">
                            </div>
                            <!-- <button type="submit" class="btn btn-primary w-100 mb-2" id="btnIniciarSesion" >Iniciar sesión</button> -->
                            <button type="submit" class="btn btn-primary w-100 mb-2" id="btnIniciarSesion" >Iniciar sesión</button>
                            <a class="btn btn-secondary w-100" id="btnRegistrarse" href="/Registro">Registrarse</a>
                            <label for="" style="text-align: center; color: red;"></label>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
  name: 'Login-', // Definición del componente
  data() {
    return {
      email: '',
      pwd: ''
    };
  },
  methods: {
    async login() {
      try {
        const userData = {
          email: this.email,
          pwd: this.pwd
        };

        // Enviar la solicitud POST
        const response = await fetch('http://127.0.0.1:8000/api/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(userData)
        });

        // Verificar si la respuesta es exitosa
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Convertir la respuesta a JSON
        const responseData = await response.json();

        // Manejar la respuesta según sea necesario
        if (responseData.success) {
          this.$router.push('/Inicio');
        } else {
          alert('Inicio de sesión fallido: ' + responseData.message);
        }
      } catch (error) {
        console.error('Error al iniciar sesión:', error);
        alert('Error al iniciar sesión: ' + error.message);
      }
    }
  }
}
</script>

  
<style>

</style>
 
  