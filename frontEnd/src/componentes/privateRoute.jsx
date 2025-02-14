import { Navigate, Outlet } from "react-router-dom";

const PrivateRoute = () => {
    const isAuthenticated = localStorage.getItem("user");
    return isAuthenticated ? <Outlet /> : <Navigate to="/ingreso" />;
};

export default PrivateRoute;
