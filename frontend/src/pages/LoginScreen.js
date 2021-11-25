import React from 'react';
import { Carousel, Row } from 'react-bootstrap';

import { image } from "../helpers/image";

export const LoginScreen = () => {
    return (
        <section className="login | bg-uas">
            <Row className="g-0">
                <div className="col-lg-7 d-none d-lg-block">
                    <Carousel>
                        <Carousel.Item>
                            <img
                                className="d-block w-100 vh-100"
                                src={ image('./img-1.png').default }
                                alt="First slide"
                            />
                            <Carousel.Caption>
                                <h3 className="teds">Rectoria</h3>
                                <p>
                                    La Universidad Autónoma de Sinaloa, aunque con diversas denominaciones en sus 148 años
                                    de existencia, ha sido un significativo soporte cultural y moral de 
                                    Sinaloa y el noroeste de México.
                                </p>
                            </Carousel.Caption>
                        </Carousel.Item>
                        <Carousel.Item>
                            <img
                                className="d-block w-100 vh-100"
                                src={ image('./img-2.jpg').default }
                                alt="Torre Academica"
                            />
                            <Carousel.Caption>
                                <h3>Torre Academica</h3>
                                <p>La Torre academica que se encuentra en la capital del estado y sirve para los eventos oficiales de la universidad.</p>
                            </Carousel.Caption>
                        </Carousel.Item>
                        <Carousel.Item>
                            <img
                                className="d-block w-100 vh-100"
                                src={ image('./img-3.jpg').default }
                                alt="Third slide"
                            />
                            <Carousel.Caption>
                                <h3>Rotonda Univesitaria</h3>
                                <p>Dentro de la torre academica contamos con estatuas de nuestros ilustres y mas reconocidos estudiantes,</p>
                            </Carousel.Caption>
                        </Carousel.Item>
                    </Carousel>
                </div>
                <div className="col-lg-5 d-flex flex-column min-vh-100 | login__form">
                    <div className="d-flex | justify-content-between | align-items-center | px-lg-5 | p-4 | pb-4 | w-100 | logo">
                        <img src={ image('./UAS.png').default } className="img-fluid" alt="logo" />
                        <img src={ image('./VISION.png').default } className="img-fluid d-none d-lg-block" alt="logo" />
                    </div>
                    <div className="align-self-center w-100 px-lg-5 py-lg-4 p-4">
                        <h1 className="fw-bold mb-4 | title">Inicio de Sesión</h1>
                        <form className="mb-5">
                            <div className="mb-4 | numCuenta">
                                <label htmlFor="numCuenta" className="form-label fw-bold">Número de Cuenta</label>
                                <div className="numCuenta__input">
                                    <input 
                                        inputMode="numeric"
                                        className="form-control border-0"
                                        id="numCuenta"
                                        placeholder="Ingresa tu número de cuenta"
                                        aria-describedby="emailHelp"
                                    />
                                    <i className="numCuenta__icon fas fa-user-graduate fa-lg"></i>
                                </div>
                            </div>
                            <div className="mb-4 | nip">
                                <label htmlFor="nip" className="form-label fw-bold">NIP</label>
                                <div className="nip__input">
                                    <input 
                                        className="form-control border-0" 
                                        placeholder="Ingresa tu NIP"
                                        id="nip"
                                        type="password"
                                        pattern="[0-9]*"
                                        inputMode="numeric"
                                    />
                                    <i className="nip__icon fas fa-lock fa-lg"></i>
                                </div>
                            </div>
                            <button type="submit" className="btn btn-primary w-100 mt-4">Iniciar</button>
                        </form>
                   </div>
                </div>
            </Row>
        </section>
    );
};
