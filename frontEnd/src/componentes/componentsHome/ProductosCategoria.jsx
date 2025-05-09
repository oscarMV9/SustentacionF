import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Dashboard from "./dashboard";
import "./productos.css";

const ProductosCategoria = () => {
    const { categoria, genero, talla } = useParams(); 
    const [productos, setProductos] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        let url = `http://localhost:8000/api/productos/${categoria}/`;
        if (genero) {
            url = `http://localhost:8000/api/productos/genero/${genero}/`;
        } else if (talla) {
            url = `http://localhost:8000/api/productos/tallas/${talla}/`;
        }

        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    setError(data.error);
                    setProductos([]);
                } else {
                    setProductos(data.productos);
                    setError(null);
                }
                setLoading(false);
            })
            .catch(error => {
                console.error("No se pudieron cargar los productos:", error);
                setError("No se pudieron cargar los productos");
                setLoading(false);
            });
    }, [categoria, genero, talla]);

    const agregarCarrito = (producto) => {
        let carrito = JSON.parse(localStorage.getItem("carrito")) || [];
        let productoExistente = carrito.find(item => item.id === producto.id);

        if (productoExistente) {
            alert("Este producto ya está en el carrito");
            return;
        } else {
            carrito.push({ ...producto, cantidad: 1 });
        }

        localStorage.setItem("carrito", JSON.stringify(carrito));
        alert(`${producto.nombre} agregado al carrito`);
    };

    if (loading) return <p>Cargando Productos...</p>;

    return (
        <>
            <Dashboard />
            <section className="contenedor">
                <div className="contenedor-items">
                    {error ? (
                        <p>{error}</p>
                    ) : (
                        productos.length > 0 ? (
                            productos.map(producto => (
                                <div key={producto.id} className="item">
                                    <span>{producto.nombre}</span>
                                    <img src={`http://127.0.0.1:8000${producto.imagen}`} alt={producto.nombre} width="150px" height="200px" />
                                    <p>Talla: {producto.talla}</p>
                                    <p>Color: {producto.color}</p>
                                    <p>Precio: ${producto.precio}</p>
                                    <p>Stock: {producto.cantidad}</p>
                                    <button
                                        onClick={() => agregarCarrito(producto)}
                                        disabled={producto.cantidad <= 0}
                                        className="boton-item"
                                    >
                                        {producto.cantidad <= 0 ? "Sin Stock" : "Agregar al Carrito"}
                                    </button>
                                </div>
                            ))
                        ) : (
                            <p>No hay productos en esta categoría.</p>
                        )
                    )}
                </div>
            </section>
        </>
    );
};

export default ProductosCategoria;