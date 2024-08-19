import mongoose from 'mongoose';

const Schema=  mongoose.Schema;

// Esquema de usuario
const userSchema = new Schema({
    email: { type: String, unique: true },
    password: String,
    nombre: String,
  });

  // Esquema de usuario
const loginSchema = new Schema({
  email: { type: String, unique: true },
  password: String,
});

const cobranzaSchema = new Schema({
  id: { type: String, unique: true },
  accion_cobranza: String,
  fecha_cobranza: Date,
  intervalo: Number,
  valor: Number

})

const alloxentric=  mongoose.model('alloxentric', userSchema, loginSchema, cobranzaSchema, );
export default alloxentric;