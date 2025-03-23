import axios from "axios";
import { useState } from "react";
import { useParams } from "react-router-dom";
import "../componentAuth/ResetPassword.css";

const RestablecerContraseña = () => {
    const { token } = useParams();
    const [nuevaContraseña, setNuevaContraseña] = useState('');
    const [mensaje, setMensaje] = useState('');
    const [isPasswordValid, setIsPasswordValid] = useState(false);
    const [passwordError, setPasswordError] = useState("");

    const validatePassword = (pass) => {
        const passwordRegex = /^(?=.*[A-Z])(?=.*\d{2,}).{8,}$/;
        return passwordRegex.test(pass);
    };

    const handlePasswordChange = (e) => {
        const pass = e.target.value;
        setNuevaContraseña(pass);
        const isValid = validatePassword(pass);
        setIsPasswordValid(isValid);
        setPasswordError(isValid ? "" : "Al menos 8 caracteres, 2 números y 1 mayúscula");
    };

    const ManejoEnvio = async (e) => {
        e.preventDefault();
        if (!isPasswordValid) {
            setMensaje("La contraseña no cumple con los requisitos");
            return;
        }
        try {
            const response = await axios.post(`http://127.0.0.1:8000/api/usuarios/restablecer-contraseña/${token}/`, { nueva_contraseña: nuevaContraseña });
            setMensaje(response.data.mensaje);
        } catch (error) {
            setMensaje(error.response?.data?.error || 'Hubo un error, intenta más tarde');
        }
    };

    return (
        <div className="container-reset">
            <form onSubmit={ManejoEnvio} className="form-restablecer">
            <h2 className="title-restablecer">Restablecer contraseña</h2>
                    <label>
                        <input
                            type="password"
                            placeholder="Nueva contraseña"
                            value={nuevaContraseña}
                            onChange={handlePasswordChange}
                            required
                        />
                    </label>
                    {passwordError && <p className="error">{passwordError}</p>}
                    <button type="submit">Restablecer</button>
                </form>
                {mensaje && <p>{mensaje}</p>}
            </div>
    );
};

export default RestablecerContraseña;