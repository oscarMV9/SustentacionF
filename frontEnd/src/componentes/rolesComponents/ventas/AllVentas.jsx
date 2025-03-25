import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "./listadoVentas.css";
import DashboardVentas from "./dashboardventas";

const AllVentas = () => {
    const [ventas, setVentas] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

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

    if (loading) {
        return <h2>Cargando...</h2>;
    }

    if (error) {
        return <h2>Hubo un error al cargar las ventas</h2>;
    }

    return (
        <div className="ventas-container">
            <DashboardVentas/>
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
                    {ventas.map((venta) => (
                        <tr key={venta.idVenta}>
                            <td>{venta.idVenta}</td>
                            <td>{venta.nombre_cliente}</td>
                            <td>{venta.apellido_cliente}</td>
                            <td>{venta.cedula}</td>
                            <td>{venta.correo}</td>
                            <td>{venta.direccion}</td>
                            <td>${venta.total.toFixed(2)}</td>
                            <td>
                                <button className="boton-ver-items" onClick={() => navigate(`/ventas/${venta.idVenta}`)}>Ver items</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default AllVentas;