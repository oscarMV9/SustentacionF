import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function Dashboard() {
    const [user, setUser] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const storedUser = localStorage.getItem("user");
        if (storedUser) {
            setUser(JSON.parse(storedUser));
        } else {
            navigate("/ingreso");
        }
    }, [navigate]);

    const cerrarSesion = () => {
        localStorage.removeItem("user");
        navigate("/ingreso");
    };

    return (
        <div>
            <h2>Bienvenido {user?.mensaje}</h2>
            <button onClick={cerrarSesion}>Cerrar sesión</button>
            <h1>Prueba de detalles</h1>
        </div>
    );
}

export default Dashboard;
