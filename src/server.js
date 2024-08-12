import express from 'express';
import mongoose from 'mongoose';
import bodyParser from 'body-parser';
import cors from 'cors';
import process from 'process';

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Conexión a MongoDB
mongoose.connect('mongodb://localhost:27017/alloxentric', { 
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => {
  console.log('Conectado a MongoDB');
}).catch((err) => {
  console.error('Error al conectar a MongoDB:', err);
});

// Esquema de usuario
const UsuarioSchema = new mongoose.Schema({
  email: { type: String, unique: true },
  password: String,
  nombre: String,
});

const Usuario = mongoose.model('Usuario', UsuarioSchema);

// Ruta de inicio de sesión
app.post('/api/login', async (req, res) => {
  const { email, pwd } = req.body;

  try {
    const usuario = await Usuario.findOne({ email, pwd });
    if (usuario) {
      res.json({ success: true });
    } else {
      res.json({ success: false });
    }
  } catch (error) {
    res.status(500).json({ success: false, message: 'Error interno del servidor' });
  }
});

// Ruta de registro
app.post('/api/register', async (req, res) => {
  const { nombre, email, pwd } = req.body;
  console.log(`Nombre: ${nombre}, Email: ${email}, Contraseña: ${pwd}`);

  try {
    // Verificar si el usuario ya existe
    const existingUsuario = await Usuario.findOne({ email });
    if (existingUsuario) {
      return res.status(400).json({ success: false, message: 'El usuario ya existe' });
    }

    // Crear un nuevo usuario
    const usuario = new Usuario({ nombre, email, password: pwd });
    await usuario.save();
    console.log('Usuario registrado:', usuario);

    res.json({ success: true, message: 'Usuario registrado exitosamente' });
  } catch (error) {
    console.error('Error al registrar el usuario:', error);
    res.status(500).json({ success: false, message: 'Error al registrar el usuario' });
  }
});

// Iniciar servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
