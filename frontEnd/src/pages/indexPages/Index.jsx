import { useEffect } from "react";
import { Link } from "react-router-dom";
import "../indexPages/index.css";

function Index() {
    useEffect(() => {
        const menuButton = document.querySelector('.menu-button');
        const menu = document.querySelector('.menu');
        const menuItems = document.querySelectorAll('.menu li');

        const handleMenuToggle = () => {
            menuButton.classList.toggle('open');
            menu.classList.toggle('open');
        };

        const handleMenuItemClick = () => {
            menuButton.classList.remove('open');
            menu.classList.remove('open');
        };

        menuButton.addEventListener('click', handleMenuToggle);
        menuItems.forEach(item => item.addEventListener('click', handleMenuItemClick));

        return () => {
            menuButton.removeEventListener('click', handleMenuToggle);
            menuItems.forEach(item => item.removeEventListener('click', handleMenuItemClick));
        };
    }, []);

    return (
    <body>
            <header className="header-index">
                <div className="logo">BB</div>
                <div className="menu-container">
                    <div className="menu-button"></div>
                    <ul className="menu">
                        <li>
                            <Link to="/formAuth">
                                <span>Login</span>
                                <div className="menu-text no-reverse">Login</div>
                            </Link>
                        </li>
                        <li>
                            <Link to="/formAuth">
                                <span>Registro</span>
                                <span className="menu-text">Registro</span>
                            </Link>
                        </li>
                        <li>
                            <Link to="/productos">
                                <span>Productos</span>
                                <span className="menu-text">Productos</span>
                            </Link>
                        </li>
                    </ul>
                </div>
            </header>
            <div className="contenido">
                <h2><span className="color">Ana</span> Style</h2>
                <p>Moda fresca <span className="color">para el alcance de todos</span></p>
            </div>
    </body>
    );
}

export default Index;