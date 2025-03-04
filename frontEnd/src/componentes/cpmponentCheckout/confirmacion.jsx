import { Link } from "react-router-dom";

function Confirmacion() {
    return (
        <div className="confirmacion">
            <h2 className="confirmacion-mensaje">Compra realizada con exito!</h2>
            <p className="tanks"> Gracias por comprar... enviamos tu recibo a tu correo</p>
            <Link to="/dashboard">Volver al inicio</Link>
        </div>
    );
}

export default Confirmacion;