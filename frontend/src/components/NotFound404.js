import {useLocation} from "react-router-dom";
import React from "react";


function NotFound404() {
    let pageLocation = useLocation()
    return (
        <div className='container'>
            <h1 className='mt-4 text-lg-center'>Страница по адресу '{pageLocation.pathname}' не найдена</h1>
        </div>
    )
}

export default NotFound404