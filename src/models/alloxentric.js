import mongoose from 'mongoose';

const Schema=  mongoose.Schema;

// Esquema de usuario
const userSchema = new Schema({
    email: { type: String, unique: true },
    password: String,
    nombre: String,
  });

const alloxentric=  mongoose.mmodel('alloxentric', userSchema);
export default alloxentric;