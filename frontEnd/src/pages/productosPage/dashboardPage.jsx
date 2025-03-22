import { Link } from "react-router-dom";
import camisetas from "../../assets/imagenes/camiseta.webp";
import pantalones from "../../assets/imagenes/pantalon.webp";
import sacos from "../../assets/imagenes/sacos.webp";
import gorros from "../../assets/imagenes/gorros.webp";
import chaquetas from "../../assets/imagenes/chaqueta.webp";
import accesorios from "../../assets/imagenes/accesorios.webp";
import blusas from "../../assets/imagenes/blusas.webp";
import sudaderas from "../../assets/imagenes/sudaderas.webp";
import medias from "../../assets/imagenes/medias.webp";
import Dashboard from "../../componentes/componentsHome/dashboard";
import calzados from "../../assets/imagenes/calzados.png";
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
                        <img src={pantalones} alt="pantalones" className="img-item" width="150px" height="200px"/>
                        <Link to="/productos/pantalones" className="boton-item">Ver Productos</Link>
                    </div>
                    <div className="item">
                        <span className="titulo-item">Sacos</span>
                        <img src={sacos} alt="sacos" className="img-item" width="150px" height="200px"/>
                        <Link to="/productos/sacos" className="boton-item">Ver Productos</Link>
                    </div>
                    <div className="item">
                        <span className="titulo-item">Gorros</span>
                        <img src={gorros} alt="gorros" className="img-item" width="150px" height="200px"/>
                        <Link to="/productos/gorros" className="boton-item">Ver Productos</Link>
                    </div>
                    <div className="item">
                        <span className="titulo-item">Chaquetas</span>
                        <img src={chaquetas} alt="chaquetas" className="img-item" width="150px" height="200px"/>
                        <Link to="/productos/chaquetas" className="boton-item">Ver Productos</Link>
                    </div>
                    <div className="item">
                        <span className="titulo-item">Accesorios</span>
                        <img src={accesorios} alt="accesorios" className="img-item" width="150px" height="200px"/>
                        <Link to="/productos/accesorios" className="boton-item">Ver Productos</Link>
                    </div>
                    <div className="item">
                        <span className="titulo-item">Calzados</span>
                        <img src={calzados} alt="calzados" className="img-item" width="150px" height="200px"/>
                        <Link to="/productos/zapatos" className="boton-item">Ver Productos</Link>
                    </div>
                    <div className="item">
                        <span className="titulo-item">Blusas</span>
                        <img src={blusas} alt="blusas" className="img-item" width="150px" height="200px"/>
                        <Link to="/productos/blusas" className="boton-item">Ver Productos</Link>
                    </div>
                    <div className="item">
                        <span className="titulo-item">Sudaderas</span>
                        <img src={sudaderas} alt="sudaderas" className="img-item" width="150px" height="200px"/>
                        <Link to="/productos/sudaderas" className="boton-item">Ver Productos</Link>
                    </div>
                    <div className="item">
                        <span className="titulo-item">Medias</span>
                        <img src={medias} alt="medias" className="img-item" width="150px" height="200px"/>
                        <Link to="/productos/medias" className="boton-item">Ver Productos</Link>
                    </div>
                </div>
            </div>
            </div>
    
        );
};

export default DashboardPage;