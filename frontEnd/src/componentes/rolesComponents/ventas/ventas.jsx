import { useState } from "react";
import PropTypes from "prop-types";
import "../ventas/ventas.css";

const BuscadorProducto = ({ onAgregarProducto }) => {
    const [id, setId] = useState("");
    const [producto, setProducto] = useState(null);
    const [error, setError] = useState("");

    const buscarProducto = async () => {
        if (!id) return;
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/producto/${id}`);
            const data = await response.json();

            if (!response.ok) throw new Error("No se encontró el producto");

            setProducto(data);
            setError("");
        } catch (err) {
            setProducto(null);
            setError(err.message);
        }
    };

    const agregarProducto = () => {
        if (producto) {
            onAgregarProducto({ ...producto, cantidadSeleccionada: 1 });
            setProducto(null);
            setId("");
            setError("");
        }
    };

    return (
        <div className="buscador-container">
            <input
                type="number"
                placeholder="Ingrese ID del producto..."
                value={id}
                onChange={(e) => setId(e.target.value)}
                className="input"
            />
            <button onClick={buscarProducto} className="btn">Buscar</button>

            {error && <p className="error">{error}</p>}

            {producto && (
                <div className="producto-card">
                    <h3>{producto.nombre}</h3>
                    <p><strong>Descripción:</strong> {producto.descripcion}</p>
                    <p><strong>Precio:</strong> ${producto.precio}</p>
                    <p><strong>Categoría:</strong> {producto.categoria_prenda}</p>
                    <p><strong>Stock:</strong> {producto.cantidad}</p>
                    <button onClick={agregarProducto} className="btn-agregar">Agregar Producto</button>
                </div>
            )}
        </div>
    );
};

BuscadorProducto.propTypes = {
    onAgregarProducto: PropTypes.func.isRequired
};

const FormularioVenta = () => {
    const [cliente, setCliente] = useState({
        nombre_cliente: "",
        apellido_cliente: "",
        cedula: "",
        correo: "",
        direccion: "",
        items: []
    });

    const [mensaje, setMensaje] = useState("");
    const [error, setError] = useState("");

    const handleChange = (e) => {
        setCliente({ ...cliente, [e.target.name]: e.target.value });
    };

    const agregarProducto = (producto) => {
        setCliente((prev) => ({
            ...prev,
            items: [...prev.items, producto],
        }));
    };

    const modificarCantidad = (index, nuevaCantidad) => {
        const nuevosItems = [...cliente.items];
        nuevosItems[index].cantidadSeleccionada = nuevaCantidad;
        setCliente({ ...cliente, items: nuevosItems });
    };

    const eliminarProducto = (index) => {
        setCliente({ ...cliente, items: cliente.items.filter((_, i) => i !== index) });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (cliente.items.length === 0) {
            alert("Debes agregar al menos un producto.");
            return;
        }

        try {
            console.log("Enviando datos:", cliente);
            const response = await fetch("http://localhost:8000/api/ventas/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    ...cliente,
                    items: cliente.items.map(item => ({
                        producto: item.id,
                        cantidad: item.cantidadSeleccionada,
                        precio_unitario: item.precio
                    }))
                }),
            });

            if (!response.ok) throw new Error("Error al enviar la venta");

            setMensaje("Venta creada con éxito!");
            setCliente({
                nombre_cliente: "",
                apellido_cliente: "",
                cedula: "",
                correo: "",
                direccion: "",
                items: [],
            });

        } catch (error) {
            setError("Hubo un error al enviar los datos.");
            console.error(error);
        }
    };

    return (
        <div className="container">
            <div className="venta-container">
                <h2 className="titulo">Formulario de Venta</h2>
                {mensaje && <p className="mensaje">{mensaje}</p>}
                {error && <p className="error">{error}</p>}
                <form onSubmit={handleSubmit} className="formulario">
                    <input type="text" name="nombre_cliente" placeholder="Nombre" value={cliente.nombre_cliente} onChange={handleChange} required className="input" />
                    <input type="text" name="apellido_cliente" placeholder="Apellido" value={cliente.apellido_cliente} onChange={handleChange} required className="input" />
                    <input type="text" name="cedula" placeholder="Cédula" value={cliente.cedula} onChange={handleChange} required className="input" />
                    <input type="email" name="correo" placeholder="Correo" value={cliente.correo} onChange={handleChange} className="input" />
                    <input type="text" name="direccion" placeholder="Dirección" value={cliente.direccion} onChange={handleChange} className="input" />
                    <h3 className="subtitulo">Buscar Productos</h3>
                    <BuscadorProducto onAgregarProducto={agregarProducto} />
                    <h3 className="subtitulo">Productos en la Venta</h3>
                    {cliente.items.length === 0 ? (
                        <p className="mensaje">Aún no hay productos</p>
                    ) : (
                        cliente.items.map((prod, index) => (
                            <div key={index} className="producto-en-venta">
                                <h3>{prod.nombre}</h3>
                                <p><strong>Precio:</strong> ${prod.precio}</p>
                                <p><strong>Categoría:</strong> {prod.categoria_prenda}</p>
                                <label className="label">Cantidad:</label>
                                <input 
                                    type="number" 
                                    value={prod.cantidadSeleccionada} 
                                    min="1" 
                                    max={prod.cantidad} 
                                    onChange={(e) => modificarCantidad(index, parseInt(e.target.value))}
                                    className="input-cantidad"
                                />
                                <button onClick={() => eliminarProducto(index)} className="btn-eliminar">❌ Eliminar</button>
                            </div>
                        ))
                    )}
                    {cliente.items.length > 0 && <button type="submit" className="btn-enviar">Confirmar Venta</button>}
                </form>
            </div>
        </div>
    );
};

export default FormularioVenta;