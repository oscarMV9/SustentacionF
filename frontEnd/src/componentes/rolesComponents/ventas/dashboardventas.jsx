import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function DashboardVentas () {
    const [user, setUser] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
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
        navigate("/formAuth");
    };

    return (
        <div>
            <div className="header">
                <h2 className="messaje_title">{user?.mensaje}</h2>
                <nav className="navbar-nav">
                    <a onClick={cerrarSesion} className="cerrar-session">Cerrar sesión</a>
                </nav>
            </div>
        </div>
    );
};

export default DashboardVentas;