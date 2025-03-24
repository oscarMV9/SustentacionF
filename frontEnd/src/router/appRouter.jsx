import {BrowserRouter as Router, Route, Routes} from "react-router-dom"
import PrivateRoute from "../componentes/privateRoute";
import ProductosCategoria from "../componentes/componentsHome/ProductosCategoria";
import Carrito from "../componentes/componentsHome/carrito";
import "@fortawesome/fontawesome-free/css/all.min.css";
import AuthForm from "../componentes/componentAuth/AuthForm";
import Index from "../pages/indexPages/Index";
import DashboardPage from "../pages/productosPage/dashboardPage";
import Checkout from "../componentes/cpmponentCheckout/Checkout";
import Confirmacion from "../componentes/cpmponentCheckout/confirmacion";
import FormRecuperacion from "../componentes/componentAuth/FormRecuperacion";
import RestablecerContraseña from "../componentes/componentAuth/ResetPassword";
import Ventas from "../componentes/rolesComponents/ventas/ventas";
import BuscadorProducto from "../componentes/rolesComponents/ventas/buscador";
import RutasProtegidas from "./RutasProtegidas";

function App() {
  const user = JSON.parse(localStorage.getItem("user"));
  return (
    <Router>
      <Routes>
          <Route path="/" element={<Index/>}/>
          <Route path="/formAuth" element={<AuthForm/>}/>
          <Route path="/restablecer-contraseña" element={<FormRecuperacion/>}/>
          <Route path="/reset-password/:token" element={<RestablecerContraseña/>}/>

          <Route path="/buscador" element={<BuscadorProducto/>}/>
          <Route element={<PrivateRoute />}>
            <Route element={<RutasProtegidas isAllowed={user?.rol === "vendedor"}/>}>
              <Route path="/ventas" element={<Ventas/>}/>
            </Route>
            <Route path="/productos/:categoria" element={<ProductosCategoria/>}/>
            <Route path="/productos/genero/:genero" element={<ProductosCategoria/>}/>
            <Route path="/carrito" element={<Carrito/>}/>
            <Route path="/dashboard" element={<DashboardPage/>}/>
            <Route path="/checkout" element={<Checkout/>}/>
            <Route path="/confirmacion" element={<Confirmacion/>}/>
          </Route>
      </Routes>
    </Router>
  );
}
export default App;