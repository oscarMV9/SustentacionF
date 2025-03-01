import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Dashboard from "./dashboard";
import "./productos.css";

const ProductosCategoria = () => {
    const { categoria } = useParams();
    const [productos, setProductos] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch(`http://localhost:8000/api/productos/${categoria}/`)
            .then(response => response.json())
            .then(data => {
                setProductos(data.productos);
                setLoading(false);
            })
            .catch(error => {
                console.error("No se pudieron cargar los productos:", error);
                setLoading(false);
            });
    }, [categoria]);

    const agregarCarrito = (producto) => {

        let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
        let productoExistente = carrito.find(item => item.id === producto.id);

        if (productoExistente) {
            alert("Este producto ya está en el carrito");
            return;
        } else {
            carrito.push({ ...producto,cantidad:1 });
        }

        localStorage.setItem("carrito", JSON.stringify(carrito));
        alert(`${producto.nombre} agregado al carrito`)
    };

    if (loading) return <p>Cargando Productos...</p>;

    return (
        <>
        <Dashboard/>
        <section className="contenedor">
            <div className="contenedor-items">
                {productos.length > 0 ? (
                    productos.map(producto => (
                        <div key={producto.id} className="item">
                            <span>{producto.nombre}</span>
                            <img src={producto.imagen} alt={producto.nombre} width="150px" height="200px"/>
                            <p>talla: {producto.talla}</p>
                            <p>Color: {producto.color}</p>
                            <p>Precio: ${producto.precio}</p>
                            <p>Stock: {producto.cantidad}</p>
                            <button
                             onClick={() => agregarCarrito(producto)}
                             disabled={producto.cantidad <= 0} className="boton-item">
                                {producto.cantidad <= 0 ? "Sin Stock" : "Agregar al Carrito"}
                             </button>
                        </div>
                    ))
                ) : (
                    <p>No hay productos en esta categoría.</p>
                )}
            </div>
        </section>
    </>
    );
};

export default ProductosCategoria;
