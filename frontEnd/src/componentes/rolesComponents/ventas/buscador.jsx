import { useState } from "react";

export default function BuscadorProducto() {
  const [id, setId] = useState("");
  const [producto, setProducto] = useState(null);
  const [error, setError] = useState("");

  const buscarProducto = async (idProducto) => {
    if (!idProducto) return;
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/producto/${idProducto}`);
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "No se encontró el producto");
      }

      setProducto(data);
      setError("");
    } catch (err) {
      setProducto(null);
      setError(err.message);
    }
  };

  return (
    <div className="flex flex-col items-center p-4">
      <input
        type="number"
        placeholder="Ingrese ID del producto..."
        className="border p-2 rounded"
        value={id}
        onChange={(e) => {
          setId(e.target.value);
          buscarProducto(e.target.value);
        }}
      />

      {error && <p className="text-red-500 mt-2">{error}</p>}

      {producto && (
        <div className="mt-4 p-4 border rounded shadow-lg">
          <h2 className="text-xl font-bold">{producto.nombre}</h2>
          <p><strong>Descripción:</strong> {producto.descripcion}</p>
          <p><strong>Precio:</strong> ${producto.precio}</p>
          <p><strong>Talla:</strong> {producto.talla || "No especificada"}</p>
          <p><strong>Color:</strong> {producto.color || "No especificado"}</p>
          <p><strong>Categoría:</strong> {producto.categoria_prenda}</p>
          <p><strong>Cantidad en stock:</strong> {producto.cantidad}</p>
          {producto.imagen && <img src={producto.imagen} alt={producto.nombre} className="w-32 h-32 mt-2" />}
        </div>
      )}
    </div>
  );
}
