import { Navigate, Outlet } from "react-router-dom";

const PrivateRoute = () => {
    const isAuthenticated = localStorage.getItem("user");
    return isAuthenticated ? <Outlet /> : <Navigate to="/formAuth" />;
};

export default PrivateRoute;
