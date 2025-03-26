import { useState, useEffect } from "react";
import BuscadorProducto from "./buscador";
import "../ventas/ventas.css";
import DashboardVentas from "./dashboardventas";

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
    const [total, setTotal] = useState(0);

    const formatCurrency = (value) => {
        return new Intl.NumberFormat("es-CO", {
            style: "currency",
            currency: "COP",
            minimumFractionDigits: 0,
        }).format(value);
    };

    const calcularTotal = () => {
        const totalVenta = cliente.items.reduce((acc, item) => acc + item.precio * item.cantidadSeleccionada, 0);
        setTotal(totalVenta);
    };

    useEffect(() => {
        calcularTotal();
    }, [cliente.items]);

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

        if(cliente.nombre_cliente || cliente.apellido_cliente) {
            const regex = /^[a-zA-Z\s]*$/;
            if (!regex.test(cliente.nombre_cliente) || !regex.test(cliente.apellido_cliente)) {
                setError("El nombre y apellido solo pueden contener letras.");
                return;
            }
        }
        

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
            setTotal(0);

        } catch (error) {
            setError("Hubo un error al enviar los datos.");
            console.error(error);
        }
    };

    return (
        <div>
            <DashboardVentas />
            <div className="container">
                <div className="venta-container">
                    <h2 className="titulo">Datos del cliente</h2>
                    {mensaje && <p className="mensaje">{mensaje}</p>}
                    {error && <p className="error">{error}</p>}
                    <form onSubmit={handleSubmit} className="formulario">
                        <input type="text" name="nombre_cliente" placeholder="Nombre" value={cliente.nombre_cliente} onChange={handleChange} required className="input" />
                        <input type="text" name="apellido_cliente" placeholder="Apellido" value={cliente.apellido_cliente} onChange={handleChange} required className="input" />
                        <input type="number" name="cedula" placeholder="Cédula" value={cliente.cedula} onChange={handleChange} required className="input" />
                        <input type="email" name="correo" placeholder="Correo" value={cliente.correo} onChange={handleChange} className="input" />
                        <input type="text" name="direccion" placeholder="Dirección" value={cliente.direccion} onChange={handleChange} className="input" />
                        {cliente.items.length > 0 && <button type="submit" className="btn-enviar">Confirmar Venta</button>}
                    </form>
                    <h3 className="total">Total: {formatCurrency(total)}</h3>
                </div>
                <div className="buscador-container">
                    <BuscadorProducto onAgregarProducto={agregarProducto} />
                </div>
            </div>
            <div className="container-items">
                <h3 className="subtitulo">Productos en la Venta</h3>
                {cliente.items.length === 0 ? (
                    <p className="mensaje">Aún no hay productos</p>
                ) : (
                    cliente.items.map((prod, index) => (
                        <div key={index} className="producto-en-venta">
                            <div className="producto-info">
                                <h3>{prod.nombre}</h3>
                                <p><strong>Precio: </strong>{formatCurrency(prod.precio)}</p>
                                <p><strong>Categoría: </strong> {prod.categoria_prenda}</p>
                                <label className="label">Cantidad: </label>
                                <input
                                    type="number"
                                    value={prod.cantidadSeleccionada}
                                    min="1"
                                    max={prod.cantidad}
                                    onChange={(e) => modificarCantidad(index, parseInt(e.target.value))}
                                    className="input-cantidad"
                                />
                            </div>
                            <button onClick={() => eliminarProducto(index)} className="btn-eliminar">Eliminar</button>
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default FormularioVenta;