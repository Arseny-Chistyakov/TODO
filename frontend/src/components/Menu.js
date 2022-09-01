import React from 'react'
import {Link} from "react-router-dom";

function NavbarItem({name, href}) {
    return (
        <li className="nav-item active">
            <Link className="nav-link" to={href}>{name}</Link>
        </li>
    )
}


export default function Navbar({navbarItems}) {
    return (
        <nav className="navbar navbar-expand-sm bg-dark navbar-dark justify-content-end">
            <a className="navbar-brand" href="/">Arseny Chistyakov</a>
            <div className="collapse navbar-collapse" id="navbarCollapse">
                <ul className="navbar-nav mr-auto">
                    {navbarItems.map((item) => <NavbarItem name={item.name} href={item.href}/>)}
                </ul>
            </div>
        </nav>
    )
}
