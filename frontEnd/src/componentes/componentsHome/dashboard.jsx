import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "../componentsHome/home.css";
import { Link } from "react-router-dom";

function Dashboard() {
    const [user, setUser] = useState(null);
    const [menu, setMenu] = useState(false);
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

    const toggleMenu = () => {
        setMenu(!menu);
    };
    return (
        <div>
            <div className="header">
                <div className="menu-desplegable" onClick={toggleMenu}>
                    <a>
                    <span className="material-symbols-outlined">
                        apps
                    </span>
                    </a>
                    <h2 className="messaje_title">{user?.mensaje}</h2>
                </div>
                {menu && (
                    <div className="menu-opciones">
                        <p className="title-menu">Tallas disponibles</p>
                        <ul>
                            <li><Link to="/productos/tallas/S" className="menu-item">tallas S</Link></li>
                            <li><Link to="/productos/tallas/XS" className="menu-item">tallas XS</Link></li>
                            <li><Link to="/productos/tallas/L" className="menu-item">tallas L</Link></li>
                            <li><Link to="/productos/tallas/XL" className="menu-item">tallas XL</Link></li>
                            <li><Link to="/productos/tallas/XXL" className="menu-item">tallas XXL</Link></li>
                            <li><Link to="/productos/tallas/UNICA" className="menu-item">tallas UNICAS</Link></li>
                        </ul>
                        <p className="title-menu">Ropa para diferentes generos</p>
                        <ul>
                            <li><Link to="/productos/genero/HOMBRE" className="menu-item">Hombre</Link></li>
                            <li><Link to="/productos/genero/MUJER" className="menu-item">Mujer</Link></li>
                            <li><Link to="/productos/genero/NIÑO" className="menu-item">Niño</Link></li>
                            <li><Link to="/productos/genero/NIÑA" className="menu-item">Niña</Link></li>
                            <li><Link to="/productos/genero/BEBE" className="menu-item">Bebes</Link></li>
                        </ul>
                    </div>
                )}
                <nav className="navbar-nav">
                    <Link to="/dashboard" className="link-dashboard">
                        <button className="boton-dashboard">Catalogo</button>
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
