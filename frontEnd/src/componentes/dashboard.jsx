import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../componentes/styleAuth/home.css";
import { Link } from "react-router-dom";

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
            navigate("/formAuth");
        }
    }, [navigate]);

    const cerrarSesion = () => {
        localStorage.removeItem("user");
        localStorage.removeItem("carrito");
        navigate("/formAuth");
    };

    return (
        <div className="header">
            <h2 className="messaje_title">{user?.mensaje}</h2>
            <nav className="navbar-nav">
                <Link to="/carrito">
                    <button className="boton-carrito">Ver Carrito</button>
                </Link>
                <a onClick={cerrarSesion}>Cerrar sesión</a>
            </nav>
        </div>
    );
}

export default Dashboard;
