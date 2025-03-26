import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./listadoVentas.css";
import DashboardVentas from "./dashboardventas";

const AllVentas = () => {
    const [ventas, setVentas] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [buscarCedula, setBuscarCedula] = useState("");
    const [buscarCorreo, setBuscarCorreo] = useState("");
    const navigate = useNavigate();

    const formatCurrency = (value) => {
        return new Intl.NumberFormat("es-CO", {
            style: "currency",
            currency: "COP",
            minimumFractionDigits: 0,
        }).format(value);
    };

    useEffect(() => {
        const fetchVentas = async () => {
            try {
                const response = await axios.get("http://localhost:8000/api/ventas/");
                setVentas(response.data);
                setLoading(false);
            } catch (error) {
                setError(error);
                setLoading(false);
            }
        };

        fetchVentas();
    }, []);

    const filtroVentas = ventas.filter((venta) => {
        const coincideCedula = buscarCedula
            ? venta.cedula.toString().includes(buscarCedula)
            : true;
        const coincideCorreo = buscarCorreo
            ? venta.correo.toString().includes(buscarCorreo)
            : true;
        return coincideCedula && coincideCorreo;
    });

    if (loading) {
        return <h2>Cargando...</h2>;
    }

    if (error) {
        return <h2>Hubo un error al cargar las ventas</h2>;
    }

    return (
        <div className="ventas-container">
            <DashboardVentas />
            <div className="search-container">
                <label>Buscar ventas por Número de cédula</label>
                <input
                    type="text"
                    placeholder="Buscar por número de cédula"
                    value={buscarCedula}
                    onChange={(e) => setBuscarCedula(e.target.value)}
                    className="search-input"
                />
                <label>Buscar ventas por Correo</label>
                <input
                    type="text"
                    placeholder="Buscar por correo"
                    value={buscarCorreo}
                    onChange={(e) => setBuscarCorreo(e.target.value)}
                    className="search-input"
                />
            </div>
            <h2 className="title-ventas">Ventas Realizadas</h2>
            <table className="ventas-table">
                <thead>
                    <tr>
                        <th>Id venta</th>
                        <th>Nombre(s) Del Cliente</th>
                        <th>Apellido(s) Del Cliente</th>
                        <th>Numero de cedula</th>
                        <th>Correos asociado</th>
                        <th>Direccion de residencia</th>
                        <th>Total</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {filtroVentas.map((venta) => (
                        <tr key={venta.idVenta}>
                            <td>{venta.idVenta}</td>
                            <td>{venta.nombre_cliente}</td>
                            <td>{venta.apellido_cliente}</td>
                            <td>{venta.cedula}</td>
                            <td>{venta.correo}</td>
                            <td>{venta.direccion}</td>
                            <td>{formatCurrency(venta.total)}</td>
                            <td>
                                <button
                                    className="boton-ver-items"
                                    onClick={() => navigate(`/ventas/${venta.idVenta}`)}
                                >
                                    Ver items
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default AllVentas;