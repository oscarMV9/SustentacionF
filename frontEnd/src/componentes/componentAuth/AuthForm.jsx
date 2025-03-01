import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../componentAuth/formAuth.css";

function AuthForm() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");
    const [passwordStrength, setPasswordStrength] = useState();
    const [email, setEmail] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const btnSignIn = document.getElementById("sign-in");
        const btnSignUp = document.getElementById("sign-up");
        const containerFormRegister = document.querySelector(".container-form.register");
        const containerFormLogin = document.querySelector(".container-form.login");

        btnSignIn.addEventListener("click", () => {
            containerFormRegister.classList.add("hide");
            containerFormLogin.classList.remove("hide");
        });

        btnSignUp.addEventListener("click", () => {
            containerFormLogin.classList.add("hide");
            containerFormRegister.classList.remove("hide");
        });

        
        return () => {
            btnSignIn.removeEventListener("click", () => {
                containerFormRegister.classList.add("hide");
                containerFormLogin.classList.remove("hide");
            });

            btnSignUp.removeEventListener("click", () => {
                containerFormLogin.classList.add("hide");
                containerFormRegister.classList.remove("hide");
            });
        };
    }, []);

    const manejoLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:8000/api/usuarios/ingreso/", {
                email,
                password,
            });
            localStorage.setItem("user", JSON.stringify(response.data));
            setMessage(response.data.mensaje);
            setTimeout(() => navigate("/dashboard"), 1500);
        } catch (error) {
            setMessage(error.response?.data?.error || "Lo siento, hubo un error.. intenta de nuevo");
        }
    };

    const passwordSecurity = (pass) => {
        if (pass.length < 6) return "demasiado debil";
        if (pass.length < 8) return "debil";
        if (/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/.test(pass)) return "Fuerte";
        return "Moderada";
    };

    const manejoRegistro = async (registro) => {
        registro.preventDefault();
        try {
            const response = await axios.post("http://127.0.0.1:8000/api/usuarios/registro/", {
                username,
                email,
                password,
            });
            setMessage(response.data.mensaje);
            setTimeout(() => navigate("/formAuth"), 1500);
        } catch (error) {
            setMessage(error.response?.data?.error || "Error al registrarse");
        }
    };

    return (
        <div className="body">
            <div className="container-form register">
                <div className="information">
                    <div className="info-childs">
                        <h2>Bienvenido</h2>
                        <p>Registrate para poder acceder a nuestro sistema y ver nuestro catalogo</p>
                        <input type="button" value="Iniciar Sesión" id="sign-in" />
                    </div>
                </div>
                <div className="form-information">
                    <div className="form-information-childs">
                        <h2>Registro</h2>
                        <div className="icons">
                            <i className="bx bxl-google"></i>
                            <i className="bx bxl-github"></i>
                            <i className="bx bxl-linkedin"></i>
                        </div>
                        <p>o usa tu usuario para registrarte</p>
                        <form onSubmit={manejoRegistro} noValidate className="form form-register">
                            <div>
                                <label>
                                    <i className='bx bx-user'></i>
                                    <input type="text" placeholder="Usuario" value={username} onChange={(registro) => setUsername(registro.target.value)} required autoComplete="off" />
                                </label>
                            </div>
                            <div>
                                <label>
                                    <i className='bx bx-envelope'></i>
                                    <input type="email" placeholder="Correo" value={email} onChange={(registro) => setEmail(registro.target.value)} required autoComplete="off" />
                                </label>
                            </div>
                            <div>
                                <label>
                                    <i className='bx bx-lock-alt'></i>
                                    <input type="password" placeholder="Contraseña" value={password} onChange={(registro) => {
                                        setPassword(registro.target.value);
                                        setPasswordStrength(passwordSecurity(registro.target.value));
                                    }} required />
                                </label>
                            </div>
                            <p>Seguridad: {passwordStrength}</p>
                            <button type="submit">Registrarse</button>
                        </form>
                        {message && <p>{message}</p>}
                    </div>
                </div>
            </div>
            <div className="container-form login hide">
                <div className="information">
                    <div className="info-childs">
                        <h2>Bienvenido</h2>
                        <p>Ingresa tus datos para poder acceder a nuestro sistema</p>
                        <input type="button" value="Registrarse" id="sign-up" />
                    </div>
                </div>
                <div className="form-information">
                    <div className="form-information-childs">
                        <h2>Ingreso</h2>
                        <div className="icons">
                            <i className="bx bxl-google"></i>
                            <i className="bx bxl-github"></i>
                            <i className="bx bxl-linkedin"></i>
                        </div>
                        <p>Ingresa tus datos para acceder</p>
                        <form onSubmit={manejoLogin} className="form form-login" noValidate> 
                            <div>
                                <label>
                                    <i className='bx bx-user'></i>
                                    <input type="text" placeholder="Correo" value={email} onChange={(e) => setEmail(e.target.value)} required autoComplete="off" />
                                </label>
                            </div>
                            <div>
                                <label>
                                    <i className='bx bx-lock-alt'></i>
                                    <input type="password" placeholder="Contraseña" value={password} onChange={(e) => setPassword(e.target.value)} required autoComplete="off" />
                                </label>
                            </div>
                            <button type="submit" value="Iniciar Sesión">Ingresar</button>
                        </form>
                        {message && <p>{message}</p>}
                    </div>
                </div>
            </div>
        </div>
    );
}

export default AuthForm;