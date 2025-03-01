import { Link } from "react-router-dom";
import camisetas from "../../assets/imagenes/camiseta.webp";
import pantalones from "../../assets/imagenes/pantalon.webp";
import sacos from "../../assets/imagenes/sacos.webp";
import gorros from "../../assets/imagenes/gorros.webp";
import chaquetas from "../../assets/imagenes/chaqueta.webp";
import accesorios from "../../assets/imagenes/accesorios.webp";
import Dashboard from "../../componentes/componentsHome/dashboard";
import "../productosPage/home.css";
const DashboardPage = () => {
    return (
    <div>
        <Dashboard/>
        <div className="contenedor">
            <div className="contenedor-items">
                <div className="item">
                    <span className="titulo-item">Camisetas</span>
                    <img src={camisetas} alt="camisetas" className="img-item" width="150px" height="200px"/>
                    <Link to="/productos/camisetas" className="boton-item">Ver Productos</Link>
                </div>
                <div className="item">
                    <span className="titulo-item">Pantalones</span>
                    <img src={pantalones} alt="camisetas" className="img-item" width="150px" height="200px"/>
                    <Link to="/productos/pantalones" className="boton-item">Ver Productos</Link>
                </div>
                <div className="item">
                    <span className="titulo-item">Sacos</span>
                    <img src={sacos} alt="camisetas" className="img-item" width="150px" height="200px"/>
                    <Link to="/productos/sacos" className="boton-item">Ver Productos</Link>
                </div>
                <div className="item">
                    <span className="titulo-item">Gorros</span>
                    <img src={gorros} alt="camisetas" className="img-item" width="150px" height="200px"/>
                    <Link to="/productos/gorros" className="boton-item">Ver Productos</Link>
                </div>
                <div className="item">
                    <span className="titulo-item">Chaquetas</span>
                    <img src={chaquetas} alt="camisetas" className="img-item" width="150px" height="200px"/>
                    <Link to="/productos/chaquetas" className="boton-item">Ver Productos</Link>
                </div>
                <div className="item">
                    <span className="titulo-item">Accesorios</span>
                    <img src={accesorios} alt="camisetas" className="img-item" width="150px" height="200px"/>
                    <Link to="/productos/accesorios" className="boton-item">Ver Productos</Link>
                </div>
            </div>
        </div>
        </div>

    );
};

export default DashboardPage;