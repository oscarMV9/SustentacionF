import { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from 'react-router-dom';
import Dashboard from "../componentsHome/dashboard";
import emailjs from '@emailjs/browser';
import './checkout.css';

function Checkout() {
    const [carrito, setCarrito] = useState([]);
    const [nombre_cliente, setNombreCliente] = useState("");
    const [N_documento, setNDocumento] = useState("");
    const [telefono, setTelefono] = useState("");
    const [direccion, setDireccion] = useState("");
    const [email, setEmail] = useState("");
    const [mensaje, setMensaje] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const storedCarrito = localStorage.getItem("carrito");
        if (storedCarrito) {
            setCarrito(JSON.parse(storedCarrito));
        }
    }, []);

    const calcularTotal = () => {
        return carrito.reduce((total, item) => total + item.precio * item.cantidad, 0);
    };

    const formatearPrecio = (precio) => {
        return new Intl.NumberFormat("es-CO", { style: "currency", currency: "COP" }).format(precio);
    };

    const formatearCarrito = () => {
        if (carrito.length === 0) return "No hay productos en el carrito.";
        return carrito.map(item => `${item.nombre} x ${item.cantidad} - ${formatearPrecio(item.precio)}`).join('\n');
    };

    const manejarPago = async (e) => {
        e.preventDefault();

        if (!nombre_cliente || !N_documento || !telefono || !direccion || !email) {
            setMensaje("Por favor, completa todos los campos.");
            return;
        }

        if (/^\d+$/.test(nombre_cliente)) {
            setMensaje("nombre valido por favor");
            return;
        }

        if (N_documento < 10000000 || N_documento > 9999999999 ) {
            setMensaje("numero de cedula no valida");

            return;
        }

        if (telefono < 3000000000 || telefono > 3999999999) {
            setMensaje("el telefono contiene 10 digitos y empieza por 3");
            return;
        }

        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            setMensaje("Correo electrónico no valido.");
            return;
        }

        try {
            const datos = await axios.post("http://127.0.0.1:8000/api/pagos/checkout/", {
                carrito,
                nombre_cliente,
                N_documento,
                telefono,
                direccion,
                email,
            });

            console.log("datos enviados: " + datos);


            const templateParams = {
                nombre_cliente,
                N_documento,
                telefono,
                direccion,
                email,
                carrito: formatearCarrito(),
                to_email: email,
            };

            console.log("Correo destinatario:", email);

            emailjs.send('service_3k4rhbg', 'template_6ddq28j', templateParams, 'a8lrAhtDAzPiawI3G')
            .then((response) => {
                console.log('Correo enviado con éxito...', response.text);
                setMensaje('Compra realizada con éxito!');
            }, (error) => {
                console.error('Error al enviar el correo:', error);
                setMensaje('Lo siento... hubo un error, intenta de nuevo...');
            });

            localStorage.removeItem("carrito");
            setTimeout(() => navigate("/confirmacion"), 1500);
        } catch (error) {
            console.error("Error en el pago:", error);
            setMensaje(error.response?.data?.error || "Lo siento... hubo un error, intenta de nuevo");
        }
    };

    return (
        <>
            <Dashboard />
            <div className="checkout">
                <h2 className="text-pagar">Pagar productos</h2>
                {carrito.length > 0 ? (
                    <div className="items-form">
                        <div className="checkout-items">
                            {carrito.map((item) => (
                                <div key={item.id} className="checkout-item">
                                    <img src={`http://127.0.0.1:8000${item.imagen}`} alt={item.nombre} width="80px"/>
                                    <span>{item.nombre}</span>
                                    <span>{formatearPrecio(item.precio)}</span>
                                    <span>Cantidad: {item.cantidad}</span>
                                </div>
                            ))}
                            <div className="checkout-total">
                                <strong>Total: {formatearPrecio(calcularTotal())}</strong>
                            </div>
                        </div>

                        <form onSubmit={manejarPago} className="form-pago">
                            <div className="inputs">
                                <label>Nombre del Cliente</label>
                                <input type="text" value={nombre_cliente} onChange={(e) => setNombreCliente(e.target.value)} required />
                            </div>
                            <div className="inputs">
                                <label>Número de Documento</label>
                                <input type="number" value={N_documento} onChange={(e) => setNDocumento(e.target.value)} required />
                            </div>
                            <div className="inputs">
                                <label>Teléfono</label>
                                <input type="text" value={telefono} onChange={(e) => setTelefono(e.target.value)} required />
                            </div>
                            <div className="inputs">
                                <label>Dirección de Envío</label>
                                <input type="text" value={direccion} onChange={(e) => setDireccion(e.target.value)} required />
                            </div>
                            <div className="inputs">
                                <label>Correo Electrónico</label>
                                <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
                            </div>
                            <button type="submit">Confirmar Pago</button>
                            {mensaje && <p>{mensaje}</p>}
                        </form>
                        
                    </div>
                ) : (
                    <p>Tu carrito está vacío.</p>
                )}
            </div>
        </>
    );
}

export default Checkout;
