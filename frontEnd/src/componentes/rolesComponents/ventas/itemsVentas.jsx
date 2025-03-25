import { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
const VentaItems = () => {
    const { idVenta } = useParams();
    const [venta, setVenta] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

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
        <div className="venta-items-container">
            <h2>Items de la Venta</h2>
            <ul>
                {venta.items.map((item, index) => (
                    <li key={index}>
                        Producto: {item.producto} - Cantidad: {item.cantidad} - Precio Unitario: ${item.precio_unitario}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default VentaItems;