import {BrowserRouter as Router, Route, Routes} from "react-router-dom"
import Registro from "./componentes/registro";
import Login from "./componentes/login";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/registro" element={<Registro />} />
          <Route path="/ingreso" element={<Login />} />
          
          <Route element={<privateRoute />}>
              <Route path="/dashboard" element={<dashboard />} />
          </Route>

        <Route path="*" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;