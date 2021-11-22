import React from 'react';

import { image } from '../../helpers/image';

export const Header = () => {
    return (
        <header className="header n">
            <div className="h-25 w-100">
                <div className="bg-yellow d-flex justify-content-around align-items-center">
                    <img alt="Logo" src={image('./UAS.png').default} className="logo"/>
                    <h2 className="fw-bold">Universidad Autónoma de Sinaloa</h2>
                    <img alt="Logo" src={image('./VISION.png').default} className="logo"/>
                </div>
                <div className="bg-blue w-100">
                    <nav className="Navbar d-flex">
                        <div className="dropdown me-4">
                            <button className="btn btn-secondary" type="button" id="dropdownMenuButton1"  data-bs-toggle="dropdown" aria-expanded="false">
                                Consultas
                            </button>
                                <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                    <li><a className="dropdown-item" href="/#">Datos generales</a></li>
                                    <li><a className="dropdown-item" href="/#">Estudios</a></li>
                                    <li><a className="dropdown-item" href="/#">Credencial digital de estudios</a></li>
                                    <li><a className="dropdown-item" href="/#">Carga académica</a></li>
                                    <li><a className="dropdown-item" href="/#">Horario de clases</a></li>
                                    <li><a className="dropdown-item" href="/#">Historial académico</a></li>
                                    <li><a className="dropdown-item" href="/#">Imprimir solicitud de examen</a></li>
                                    <li><a className="dropdown-item" href="/#">Corrección de calificaciones</a></li>
                                </ul>
                        </div>
                        <div className="dropdown me-4">
                            <button className="btn btn-secondary " type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                            Tramites
                            </button>
                                <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                    <li><a className="dropdown-item" href="/#">Generar formato de pago</a></li>
                                    <li><a className="dropdown-item" href="/#">Estado de trámite</a></li>
                                    <li><a className="dropdown-item" href="/#">Imprimir solicitud de cambio de unidad académica</a></li>
                                    <li><a className="dropdown-item" href="/#">Solicitud de certificado</a></li>
                                    <li><a className="dropdown-item" href="/#">Solicitud de título</a></li>
                                    <li><a className="dropdown-item" href="/#">Pago en línea</a></li>
                                </ul>
                        </div>
                        <div className="dropdown me-4">
                            <button className="btn btn-secondary " type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                            Reinscripción
                            </button>
                                <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                    <li><a className="dropdown-item" href="/#">Guías</a></li>
                                    <li><a className="dropdown-item" href="/#">Imprimir formatos</a></li>
                                    <li><a className="dropdown-item" href="/#">Certificado médico</a></li>
                                    <li><a className="dropdown-item" href="/#">Datos de contacto</a></li>
                                    <li><a className="dropdown-item" href="/#">Carta autorización</a></li>
                                    <li><a className="dropdown-item" href="/#">Constancia de kardex</a></li>
                                    <li><a className="dropdown-item" href="/#">Actualizar fotografía</a></li>
                                    <li><a className="dropdown-item" href="/#">Incorporar expediente de reingreso</a></li>
                                </ul>
                        </div>
                        <div className="dropdown me-4">
                            <button className="btn btn-secondary " type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                            Examenes 
                            </button>
                                <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                    <li><a className="dropdown-item" href="/#">Solicitud de examen</a></li>
                                    <li><a className="dropdown-item" href="/#">Impresión de hoja de pago</a></li>
                                    <li><a className="dropdown-item" href="/#">Imprime materias solicitadas</a></li>
                                    <li><a className="dropdown-item" href="/#">Pagos</a></li>
                                </ul>
                        </div>
                        <div className="dropdown me-4">
                            <button className="btn btn-secondary " type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                            Idiomas
                            </button>
                                <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                    <li><a className="dropdown-item" href="/#">Solicitar hoja de pago de reinscripción</a></li>
                                    <li><a className="dropdown-item" href="/#">Imprimir hoja de pago</a></li>
                                    <li><a className="dropdown-item" href="/#">Imprimir constancia de pago de reinscripción</a></li>
                                    <li><a className="dropdown-item" href="/#">Asignar grupo y aula de clases</a></li>
                                    <li><a className="dropdown-item" href="/#">Estado de tu Reinscripción</a></li>
                                    <li><a className="dropdown-item" href="/#">Impresión de constancia de reinscripción</a></li>

                                </ul>
                        </div>
                        <div className="dropdown me-4">
                            <button className="btn btn-secondary " type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                            Encuestas
                            </button>
                                <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                    <li><a className="dropdown-item" href="/#">Evaluacion docente</a></li>
                                    <li><a className="dropdown-item" href="/#">EDAOM</a></li>
                                </ul>
                        </div>    
                        <div className="dropdown perfil me-4">
                            <button className="btn btn-secondary " type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
                                <span>Mi perfil</span>
                                <img alt="Logo" src={image('./ruben.jpg').default} className="rounded-circle"/>
                            </button>
                            <ul className="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                                <li><a className="dropdown-item" href="/#">Ir a Mi perfil</a></li>
                                <li><a className="dropdown-item" href="/#">Cerrar Sesion</a></li>
                            </ul>
                        </div>
                    </nav>
                </div>
            </div>
        </header>
    )
}
