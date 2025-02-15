import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../componentes/styleAuth/login.css"

function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const navigate = useNavigate();

    const manejoLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:8000/api/usuarios/ingreso/", {
                username,
                password,
            });

            localStorage.setItem("user", JSON.stringify(response.data));
            setMessage(response.data.mensaje);

            setTimeout(() => navigate("/dashboard"), 1500);
        } catch (error) {
            setMessage(error.response?.data?.error || "Lo siento, hubo un error.. intenta de nuevo");
        }
    };

    return (
        <div className="login-container">
          <h2>Ingreso</h2>
          <form onSubmit={manejoLogin}>
            <input type="text" placeholder="Usuario" value={username} 
                   onChange={(e) => setUsername(e.target.value)} required autoComplete="off" />
            <input type="password" placeholder="Contraseña" value={password} 
                   onChange={(e) => setPassword(e.target.value)} required autoComplete="off" />
            <button type="submit">Ingresar</button>
          </form>
          {message && <p>{message}</p>}
        </div>
    );
}

export default Login;
