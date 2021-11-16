import React from "react";
import { image } from "../../helpers/image";

export const LoginScreen = () => {
    return (
       <div className="login">
            <header className="header">
                <div className="header_container">
                    <img className="header_container-image" src={image('./UAS.png').default} alt="Logo - UAS" />
                    <h3 className="header_container-title">Universidad Autonóma de Sinaloa</h3>
                    <img className="header_container-image" src={image('./VISION.png').default} alt="Logo - UAS" />
                </div>
            </header>
            <main className="container">
                <div className="subcontainer">
                    <h3>Sistema Integral de<br/>Información Administrativa</h3>
                    <h3>Modulo de servicios a los alumnos</h3>
                    <form className="form-container">
                        <h3>Inicio de sesión</h3>
                        <div className="numCuenta">
                            <input type="text" placeholder="Número de cuenta"/>
                            <i class="fas fa-user-graduate fa-lg"></i>
                        </div>
                        <div className="password">
                            <input type="password" placeholder="NIP"/>
                            <i class="fas fa-lock fa-lg"></i>
                        </div>
                        <button type="summit">Iniciar</button>
                    </form>
                </div>
            </main>
       </div> 
    );
};
