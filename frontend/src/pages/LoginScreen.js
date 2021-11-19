import React, {useEffect, useRef} from 'react';
import { image } from "../helpers/image";

const isMobile = () => {
    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ){
        return true;
    }
    else {
        return false;
    }
}

export const LoginScreen = () => {
    const login = useRef(null);

    const resize = (e) => {
        if ( isMobile() ){
            if ( !login.current.classList.contains('fix') ){
                login.current.classList.add('fix');
            }
        }
    }

    const originalSize = () => {
        if ( isMobile() ){
            if ( login.current.classList.contains('fix') ){
                login.current.classList.remove('fix');
            }
        }
    }

    useEffect(() => {
        
    }, [])

    return (
       <div className="login" ref={login}>
            <header className="header">
                <img className="header__img" src={image('./UAS.png').default} alt="Logo - UAS" />
                <h3 className="header__title">Universidad Autonóma de Sinaloa</h3>
                <img className="header__img" src={image('./VISION.png').default} alt="Logo - UAS" />
            </header>
            <main className="main">
                <div className="container">
                    <h3 className="container__title">Sistema Integral de<br/>Información Administrativa</h3>
                    <h3 className="container__subtitle">Modulo de servicios a los alumnos</h3>
                    <form className="form">
                        <h3 className="form__title">Inicio de sesión</h3>
                        <div className="numCuenta">
                            <input 
                                className="numCuenta__input"
                                type="text"
                                placeholder="Número de cuenta"
                                onFocus={resize}
                                onBlur={originalSize}
                            />
                            <i className="numCuenta__icon fas fa-user-graduate fa-lg"></i>
                        </div>
                        <div className="nip">
                            <input 
                                className="nip__input"
                                type="password" pattern="[0-9]*"
                                inputMode="numeric" placeholder="NIP"
                                onFocus={resize}
                                onBlur={originalSize}
                            />
                            <i className="nip__icon fas fa-lock fa-lg"></i>
                        </div>
                        <button className="form__submit" type="summit">Acceder</button>
                    </form>
                </div>
            </main>
       </div> 
    );
};
