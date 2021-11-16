import { Link } from "react-router-dom";

export const Navbar = props => {

    const show = () => {
        const ele = document.querySelector('.navbar-menu');
        ele.classList.toggle('is-active');
    };
    
    return (
        <nav></nav>  
    )
};