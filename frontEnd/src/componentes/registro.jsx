import { useState } from "react";
import { useNavigate } from "react-router-dom"
import axios from "axios";
import "../componentes/styleAuth/registro.css"

function Registro() {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const [passwordStrength, setPasswordStrength] = useState();
    const navigate = useNavigate();

    const checkPasswordStrength = (pass) => {
        if (pass.length < 6) return "demasiado debil";
        if (pass.length < 8) return "debil";
        if (/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/.test(pass)) return "Fuerte";
        return "Moderada"
    };

    const manejoRegistro = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:8000/api/usuarios/registro/", {
                username,
                email,
                password,
            });
            setMessage(response.data.mensaje);
            setTimeout(() => navigate("/ingreso"), 1500)
            navigate("/ingreso");
        } catch (error) {
            setMessage(error.response?.data?.error || "Error al registrarse");
        }
    };

    return (
        <div className="registro-container">
          <h2>Registro</h2>
          <form onSubmit={manejoRegistro}>
            <input type="text" placeholder="Usuario" value={username} onChange={(e) => setUsername(e.target.value)} required autoComplete="off" />
            <input type="email" placeholder="Correo" value={email} onChange={(e) => setEmail(e.target.value)} required autoComplete="off"/>
            <input type="password" placeholder="Contraseña" value={password} 
                   onChange={(e) => {
                     setPassword(e.target.value);
                     setPasswordStrength(checkPasswordStrength(e.target.value));
                   }} required />
            <p>Seguridad: {passwordStrength}</p>
            <button type="submit">Registrarse</button>
          </form>
          {message && <p>{message}</p>}
        </div>
    );
}

export default Registro;