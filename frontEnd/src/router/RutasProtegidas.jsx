import { Navigate, Outlet } from "react-router-dom";
import PropTypes from "prop-types";

const RutasProtegidas = ({ isAllowed, redirectTo = "/dashboard"}) => {
    if (!isAllowed) {
        return <Navigate to={redirectTo} replace/>;
    }
    return <Outlet/>;
};

RutasProtegidas.propTypes = {
    isAllowed: PropTypes.bool.isRequired,
    redirectTo: PropTypes.string,
};

export default RutasProtegidas;