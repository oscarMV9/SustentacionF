import axios from "axios";
import { useState } from "react";
import "../componentAuth/FormRecuperacion.css";

const FormRecuperacion = () => {
    const [email, setEmail] = useState('');
    const [mensaje, setMensaje] = useState('');

    const manejoEnvio = async (e) => {
        e.preventDefault();
        if (!email) {
            setMensaje("el campo de correo es obligatorio");
            return;
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            setMensaje("El correo tiene que ser valido");
            return;
        }
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/usuarios/solicitar-recuperacion/', { email });
            setMensaje(response.data.mensaje);
        } catch (error) {
            setMensaje(error.response?.data?.error || "Error al enviar la solicitud");
        }
    };

    return(
        <div className="contenedor">
            <div className="form-recuperacion">
            <h2>Recuperar tu contraseña</h2>
                <form onSubmit={manejoEnvio} className="form">
                    <label>
                        <input type="email"
                        placeholder="Tu correo electronico"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required/>
                    </label>
                    <button type="submit">Enviar</button>
                </form>
                {mensaje && <p>{mensaje}</p>}
            </div>
        </div>
    );
};
export default FormRecuperacion;
