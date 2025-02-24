import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import "../componentes/styleAuth/productosComponente.css"

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
        <div className="productContainer">
            <h2>Productos en la categoría: {categoria}</h2>
            <div className="productos-grid">
                {productos.length > 0 ? (
                    productos.map(producto => (
                        <div key={producto.id} className="producto-card">
                            <img src={producto.imagen} alt={producto.nombre} />
                            <h3>{producto.nombre}</h3>
                            <p>{producto.descripcion}</p>
                            <p>talla: {producto.talla}</p>
                            <p>Color: {producto.color}</p>
                            <p>Precio: ${producto.precio}</p>
                            <p>Stock: {producto.cantidad}</p>
                            <button
                             onClick={() => agregarCarrito(producto)}
                             disabled={producto.cantidad <= 0}
                             >
                                {producto.cantidad <= 0 ? "Sin Stock" : "Agregar al Carrito"}
                             </button>
                        </div>
                    ))
                ) : (
                    <p>No hay productos en esta categoría.</p>
                )}
            </div>
        </div>
    );
};

export default ProductosCategoria;
