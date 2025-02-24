import {BrowserRouter as Router, Route, Routes} from "react-router-dom"
import Dashboard from "./componentes/dashboard";
import PrivateRoute from "./componentes/privateRoute";
import ProductosCategoria from "./componentes/ProductosCategoria";
import Carrito from "./componentes/carrito";
import "@fortawesome/fontawesome-free/css/all.min.css";
import AuthForm from "./componentes/AuthForm";

function App() {
  return (
    <Router>
      <Routes>
          <Route path="/formAuth" element={<AuthForm/>}/>
          <Route element={<PrivateRoute />}>
              <Route path="/dashboard" element={<Dashboard />} />
              <Route path="/productos/:categoria" element={<ProductosCategoria/>}/>
              <Route path="/carrito" element={<Carrito/>}/>
          </Route>
      </Routes>
    </Router>
  );
}
export default App;