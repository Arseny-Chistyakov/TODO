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
import LoginForm from "./components/Auth";


const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`

function NotFound404() {
    let pageLocation = useLocation()
    return (
        <div className='container'>
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
            TODOs: [],
            auth: {username: '', is_login: false}
        }
    }

    login(username, password) {
        axios.post(get_url('token/'), {username: username, password: password})
            .then(response => {
                const result = response.data
                const access = result.access
                const refresh = result.refresh
                localStorage.setItem('login', username)
                localStorage.setItem('access', access)
                localStorage.setItem('refresh', refresh)
                this.setState({'auth': {username: username, is_login: true}})
                this.load_data()
            }).catch(error => {
            if (error.response.status === 401) {
                alert('Неверный логин или пароль')
            } else {
                console.log(error)
            }
        })
    }


    logout() {
        localStorage.setItem('login', '')
        localStorage.setItem('access', '')
        localStorage.setItem('refresh', '')
        this.setState({'auth': {username: '', is_login: false}})
    }


    load_data() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.state.auth.is_login) {
            const token = localStorage.getItem('access')
            headers['Authorization'] = 'Bearer ' + token
        }
        axios.get(get_url('users/'), {headers})
            .then(response => {
                this.setState({users: response.data.results})
                console.log(response.data)
            }).catch(error =>
            console.log(error)
        )

        axios.get(get_url('projects/'), {headers})
            .then(response => {
                this.setState({projects: response.data.results})
            }).catch(error => console.log(error))

        axios.get(get_url('TODOs/'), {headers})
            .then(response => {
                console.log(response.data)
                this.setState({TODOs: response.data.results})
            }).catch(error =>
            console.log(error)
        )
    }

    componentDidMount() {
        const username = localStorage.getItem('login')
        if ((username !== "") && (username != null)) {
            this.setState({'auth': {username: username, is_login: true}}, () => this.load_data())
        }
    }

    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <header>
                        <Navbar navbarItems={this.state.navbarItems} auth={this.state.auth}
                                logout={() => this.logout()}/>
                    </header>
                    <main role="main" className="flex-shrink-0">
                        <Routes>
                            <Route exact path='/login' element={<LoginForm
                                login={(username, password) => this.login(username, password)}/>}/>
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
