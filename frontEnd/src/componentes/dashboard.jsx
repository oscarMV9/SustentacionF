import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../componentes/styleAuth/home.css";

function Dashboard() {
    const [user, setUser] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        console.log("verificando si existe usuario...")
        const storedUser = localStorage.getItem("user");
        if (storedUser) {
            console.log("usuario Encontrado" + storedUser);
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
        <div className="header">
            <h2>{user?.mensaje}</h2>
            <nav className="navbar-nav">
                <a onClick={cerrarSesion}>Cerrar sesión</a>
            </nav>
        </div>
    );
}

export default Dashboard;
