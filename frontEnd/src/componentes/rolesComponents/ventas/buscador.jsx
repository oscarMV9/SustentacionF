import { useState, useEffect } from "react";
import PropTypes from "prop-types";
import "../ventas/ventas.css";

const BuscadorProducto = ({ onAgregarProducto}) => {
    const [id, setId] = useState("");
    const [producto, setProducto] = useState(null);
    const [error, setError] = useState("");

    useEffect(() => {
        const buscarProducto = async () => {
            if (!id) {
                setProducto(null);
                return;
            }
            try {
                const response = await fetch(`http://127.0.0.1:8000/api/producto/${id}`);
                const data = await response.json();

                if (!response.ok) throw new Error("no se encontro el producto");

                setProducto(data);
                setError("");

            } catch (error) {
                setProducto(null);
                setError(error.message);
            }
        };
        buscarProducto();
    }, [id]);

    const agregarProducto = () => {
        if (producto) {
            onAgregarProducto({...producto, cantidadSeleccionada: 1});
            setProducto(null);
            setId("");
            setError("");
        }
    };

    return (
        <div className="buscador">
            <input type="number"
            placeholder="Codigo del producto"
            value={id}
            onChange={(e) => setId(e.target.value)}
            className="input-buscar"
            />

            {error && <p className="error">{error}</p>}

            {producto && (
                <div className="producto-card">
                    <h3>{producto.nombre}</h3>
                    <p><strong>Precio: </strong>{producto.precio}</p>
                    <p><strong>talla: </strong>{producto.talla}</p>
                    <p><strong>cantidades: </strong>{producto.cantidad}</p>
                    <button onClick={agregarProducto} className="btn-agregar">Agregar Producto</button>
                </div>
            )}
        </div>
    );
};

BuscadorProducto.prototype = {
    onAgregarProducto: PropTypes.func.isRequired,
};

export default BuscadorProducto;
