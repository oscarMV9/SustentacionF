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
import IndexLogistica from "../componentes/rolesComponents/logistica/logistica";
import BuscadorProducto from "../componentes/rolesComponents/ventas/buscador";
import FormRecuperacion from "../componentes/componentAuth/FormRecuperacion";

function App() {
  return (
    <Router>
      <Routes>
          <Route path="/" element={<Index/>}/>
          <Route path="/formAuth" element={<AuthForm/>}/>
          <Route path="/restablecer-contraseña" element={<FormRecuperacion/>}/>
          <Route path="/buscar" element={<BuscadorProducto/>}/>
          <Route element={<PrivateRoute />}>
            <Route path="/productos/:categoria" element={<ProductosCategoria/>}/>
            <Route path="/productos/genero/:genero" element={<ProductosCategoria/>}/>
            <Route path="/carrito" element={<Carrito/>}/>
            <Route path="/dashboard" element={<DashboardPage/>}/>
            <Route path="/checkout" element={<Checkout/>}/>
            <Route path="/confirmacion" element={<Confirmacion/>}/>
            <Route path="/logistica" element={<IndexLogistica/>}/>
          </Route>
      </Routes>
    </Router>
  );
}
export default App;