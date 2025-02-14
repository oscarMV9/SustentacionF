import {BrowserRouter as Router, Route, Routes} from "react-router-dom"
import Registro from "./componentes/registro";
import Login from "./componentes/login";
import Dashboard from "./componentes/dashboard";
import PrivateRoute from "./componentes/privateRoute";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/registro" element={<Registro />} />
          <Route path="/ingreso" element={<Login />} />
          
          <Route element={<PrivateRoute />}>
              <Route path="/dashboard" element={<Dashboard />} />
          </Route>

        <Route path="*" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;