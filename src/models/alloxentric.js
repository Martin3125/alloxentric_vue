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


const alloxentric=  mongoose.model('alloxentric', userSchema, loginSchema);
export default alloxentric;