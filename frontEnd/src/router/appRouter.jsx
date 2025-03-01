import {BrowserRouter as Router, Route, Routes} from "react-router-dom"
import PrivateRoute from "../componentes/privateRoute";
import ProductosCategoria from "../componentes/componentsHome/ProductosCategoria";
import Carrito from "../componentes/componentsHome/carrito";
import "@fortawesome/fontawesome-free/css/all.min.css";
import AuthForm from "../componentes/componentAuth/AuthForm";
import Index from "../pages/indexPages/Index";
import DashboardPage from "../pages/productosPage/dashboardPage";

function App() {
  return (
    <Router>
      <Routes>
          <Route path="/" element={<Index/>}/>
          <Route path="/formAuth" element={<AuthForm/>}/>
          <Route element={<PrivateRoute />}>
            <Route path="/productos/:categoria" element={<ProductosCategoria/>}/>
            <Route path="/productos/genero/:genero" element={<ProductosCategoria/>}/>
            <Route path="/carrito" element={<Carrito/>}/>
            <Route path="/dashboard" element={<DashboardPage/>}/>
          </Route>
      </Routes>
    </Router>
  );
}
export default App;