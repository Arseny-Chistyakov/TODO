import React from 'react';
import axios from 'axios';
import {BrowserRouter, Route, Routes, useLocation} from "react-router-dom";

import './bootstrap-css/bootstrap-css.min.css'
import './bootstrap-css/sticky-footer-navbar.css'
import './App.css';
import UserList from "./components/User";
import {ProjectDetail, ProjectList} from './components/Project.js'
import TODOList from "./components/TODO";
import Footer from "./components/Footer";
import Navbar from "./components/Menu";


const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`

function NotFound404() {
    let pageLocation = useLocation()
    return (
        <div>
            <h1 className='mt-4 text-lg-center'>Страница по адресу '{pageLocation.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            navbarItems: [
                {name: 'Users', href: '/'},
                {name: 'TODOs', href: '/TODOs'},
                {name: 'Projects', href: '/projects'},
            ],
            users: [],
            projects: [],
            todos: []
        }
    }

    componentDidMount() {
        axios.get(get_url('users/'))
            .then(response => {
                this.setState({'users': response.data.results})
            }).catch(error => console.log(error))

        axios.get(get_url('projects/'))
            .then(response => {
                this.setState({'projects': response.data.results})
            }).catch(error => console.log(error))

        axios.get(get_url('TODOs/'))
            .then(response => {
                this.setState({'TODOs': response.data.results})
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <header>
                        <Navbar navbarItems={this.state.navbarItems}/>
                    </header>
                    <main role="main" className="flex-shrink-0">
                        <Routes>
                            <Route exact path='/' element={<UserList users={this.state.users}/>}/>
                            <Route exact path='/users' element={<UserList users={this.state.users}/>}/>
                            <Route exact path='/TODOs' element={<TODOList TODOs={this.state.TODOs}/>}/>
                            <Route path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                            <Route path='/projects/:id' element={<ProjectDetail projects={this.state.projects}/>}/>
                            <Route path="*" element={<NotFound404/>}/>
                        </Routes>
                    </main>
                    <Footer/>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
