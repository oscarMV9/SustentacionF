import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Dashboard from "./dashboard";
import "../componentsHome/carrito.css";

function Carrito() {
    const [carrito, setCarrito] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const storedCarrito = localStorage.getItem("carrito");
        if (storedCarrito) {
            setCarrito(JSON.parse(storedCarrito));
        }
    }, []);

    const eliminarProducto = (id) => {
        const nuevoCarrito = carrito.filter(item => item.id !== id);
        setCarrito(nuevoCarrito);
        localStorage.setItem("carrito",JSON.stringify(nuevoCarrito));
    };

    const actualizarCantidad = (id,cantidad) => {
        const nuevoCarrito = carrito.map(item => 
            item.id === id ? { ...item, cantidad:Math.max(1,cantidad) } : item
        );
        setCarrito(nuevoCarrito);
        localStorage.setItem("carrito",JSON.stringify(nuevoCarrito));
    };

    const calcularTotal = () => {
        return carrito.reduce((total, item) => total + item.precio * item.cantidad,0);
    };

    return (
        <>
        <Dashboard/>
        <div className="carrito">
            <div className="header-carrito">
                <h2 className="">Carrito de Compras</h2>
            </div>
        {carrito.length > 0 ? (
            <>                  
                <div className="carrito-items">
                    {carrito.map((item) => (
                        <div key={item.id} className="carrito-item">
                            <img src={item.imagen} alt={item.nombre} width="80px"/>
                            <div className="carrito-item-detalles">
                                <span className="carrito-item-titulo">{item.nombre}</span>
                                <div className="selector-cantidad">
                                    <button onClick={() => actualizarCantidad(item.id, item.cantidad - 1)}>-</button>
                                    <span className="carrito-item-cantidad">{item.cantidad}</span>
                                    <button onClick={() => actualizarCantidad(item.id, item.cantidad + 1)}>+</button>
                                </div>
                                <span className="carrito-item-precio">Precio: ${item.precio}</span>
                                <p>Talla: {item.talla} | Color: {item.color}</p>
                                <button className="btn-eliminar" onClick={() => eliminarProducto(item.id)}>
                                <i className="fa-solid fa-trash"></i>
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
                <span>Total: ${calcularTotal().toFixed(2)}</span>
                <button className="checkout-btn" onClick={() => navigate("/checkout")}>Finalizar Compra</button>
            </>
        ) : (
            <p>Tu carrito está vacío.</p>
        )}
        </div>
        </>
    );
}

export default Carrito;