import { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import DashboardVentas from "./dashboardventas";
import "./itemsVenta.css";

const VentaItems = () => {
    const { idVenta } = useParams();
    const [venta, setVenta] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Formateador para pesos colombianos
    const formatCurrency = (value) => {
        return new Intl.NumberFormat("es-CO", {
            style: "currency",
            currency: "COP",
            minimumFractionDigits: 0,
        }).format(value);
    };

    useEffect(() => {
        const fetchVenta = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/api/ventas/${idVenta}/`);
                setVenta(response.data);
                setLoading(false);
            } catch (error) {
                setError(error);
                setLoading(false);
            }
        };

        fetchVenta();
    }, [idVenta]);

    if (loading) {
        return <h2>Cargando...</h2>;
    }

    if (error) {
        return <h2>Hubo un error al cargar los items de la venta</h2>;
    }

    return (
        <div className="items-container">
            <DashboardVentas />
            <h2 className="title-items-venta">Items de la Venta</h2>
            <table className="items-table">
                <thead>
                    <tr>
                        <th>Producto</th>
                        <th>Nombre del Producto</th>
                        <th>Cantidad</th>
                        <th>Precio Unitario</th>
                        <th>Subtotal</th>
                    </tr>
                </thead>
                <tbody>
                    {venta.items.map((item, index) => (
                        <tr key={index}>
                            <td>{item.producto}</td>
                            <td>{item.nombre_producto}</td>
                            <td>{item.cantidad}</td>
                            <td>{formatCurrency(item.precio_unitario)}</td>
                            <td>{formatCurrency(item.precio_unitario * item.cantidad)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default VentaItems;