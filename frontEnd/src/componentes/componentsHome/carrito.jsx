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

    const formatearPrecio = (precio) => {
        return new Intl.NumberFormat("en-CO", { style: "currency", currency: "COP" }).format(precio);
    }

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
                            <img src={`http://127.0.0.1:8000${item.imagen}`} alt={item.nombre} width="80px"/>
                            <div className="carrito-item-detalles">
                                <span className="carrito-item-titulo">{item.nombre}</span>
                                <div className="selector-cantidad">
                                    <i onClick={() => actualizarCantidad(item.id, item.cantidad - 1)} className="fa-solid fa-minus restar-cantidad"></i>
                                    <span className="carrito-item-cantidad">{item.cantidad}</span>
                                    <i onClick={() => actualizarCantidad(item.id, item.cantidad + 1)} className="fa-solid fa-plus sumar-cantidad"></i>
                                </div>
                                <span className="carrito-item-precio">Precio: ${formatearPrecio(item.precio)}</span>
                                <p>Talla: {item.talla} | Color: {item.color}</p>
                                <button className="btn-eliminar" onClick={() => eliminarProducto(item.id)}>
                                <i className="fa-solid fa-trash"></i>
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
                <div className="carrito-total">
                    <div className="fila">
                        <strong>Tu Total</strong>
                        <span className="carrito-precio-total">${formatearPrecio(calcularTotal().toFixed(2))}</span>
                    </div>
                    <button className="btn-pagar" onClick={() => navigate("/checkout")}>Pagar  <i className="fa-solid fa-bag-shopping"></i> </button>
                </div>
            </>
        ) : (
            <p>Tu carrito está vacío.</p>
        )}
        </div>
        </>
    );
}

export default Carrito;