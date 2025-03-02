import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../componentsHome/home.css";
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
        <div>
            <div className="header">
                <h2 className="messaje_title">{user?.mensaje}</h2>
                <nav className="navbar-nav">
                    <Link to="/dashboard" className="link-dashboard">
                        <button className="boton-dashboard">Productos</button>
                    </Link>
                    <Link to="/carrito" className="link-carrito">
                        <button className="boton-carrito">Ver Carrito</button>
                    </Link>
                    <Link to="/productos/genero/hombre" className="link-genero">
                        <button className="boton-carrito">Hombre</button>
                    </Link>
                    <Link to="/productos/genero/mujer" className="link-genero">
                        <button className="boton-carrito">Mujer</button>
                    </Link>
                    <a onClick={cerrarSesion} className="cerrar-session">Cerrar sesión</a>
                </nav>
            </div>
        </div>
    );
}

export default Dashboard;
