import React from 'react';
import axios from 'axios';
import {BrowserRouter, Route, Routes} from "react-router-dom";

import './bootstrap-css/bootstrap-css.min.css'
import './bootstrap-css/sticky-footer-navbar.css'
import './App.css';
import UserList from "./components/User";
import {ProjectDetail, ProjectList} from './components/Project.js'
import TODOList from "./components/TODO";
import Footer from "./components/Footer";
import Navbar from "./components/Menu";
import NotFound404 from "./components/NotFound404";
import LoginForm from "./components/Auth";
import ProjectCreateForm from "./components/ProjectCreateForm";
import ProjectUpdateForm from "./components/ProjectUpdateForm";
import TODOCreateForm from "./components/TODOCreateForm";


const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`

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

    create_project(name, creatorsProject, repository) {
        let headers = this.get_headers()
        const data = {name: name, creatorsProject: creatorsProject, repository: repository}
        axios.post(get_url(`projects/`), data, {headers}).then(response => {
            this.load_data()
        }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })
    }

    update_project(uid, name, creatorsProject, repository) {
        let headers = this.get_headers()
        const data = {uid: uid, name: name, creatorsProject: creatorsProject, repository: repository}
        console.log(data)
        axios.put(get_url(`projects/${uid}/`), data, {headers})
            .then(response => {
                this.load_data()
            }).catch(error => {
            console.log(error)
            this.setState({
                projects: []
            })
        })
    }

    delete_project(uid) {
        let headers = this.get_headers()
        axios.delete(get_url(`projects/${uid}/`), {headers}).then(response => {
            this.load_data()
        }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })
    }

    create_TODO(body, creatorKeep, project) {
        const headers = this.get_headers()
        const data = {body: body, creatorKeep: creatorKeep, project: project}
        axios.post(get_url(`TODOs/`), data, {headers}).then(response => {
            this.load_data()
        }).catch(error => {
            console.log(error)
            this.setState({TODOs: []})
        })
    }

    delete_TODO(uid) {
        let headers = this.get_headers()
        axios.delete(get_url(`TODOs/${uid}/`), {headers}).then(response => {
            this.load_data()
        }).catch(error => {
            console.log(error)
            this.setState({TODOs: []})
        })
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.state.auth.is_login) {
            const token = localStorage.getItem('access')
            headers['Authorization'] = 'Bearer ' + token
        }
        return headers
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
        let headers = this.get_headers()
        axios.get(get_url('users/'), {headers})
            .then(response => {
                this.setState({users: response.data.results})
            }).catch(error =>
            console.log(error)
        )

        axios.get(get_url('projects/'), {headers})
            .then(response => {
                this.setState({projects: response.data.results})
            }).catch(error => console.log(error))

        axios.get(get_url('TODOs/'), {headers})
            .then(response => {
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
                            <Route exact path='/TODOs' element={<TODOList TODOs={this.state.TODOs}
                                                                          delete_TODO={(uid) => this.delete_TODO(uid)}/>}/>
                            <Route path="/TODOs/create" element={<TODOCreateForm creatorKeep={this.state.users}
                                                                                 project={this.state.projects}
                                                                                 create_TODO={(body, creatorKeep, project) => this.create_TODO(body, creatorKeep, project)}/>}></Route>
                            <Route path='/projects' element={<ProjectList projects={this.state.projects}
                                                                          update_project={(uid) => this.update_project(uid)}
                                                                          delete_project={(uid) => this.delete_project(uid)}/>}/>
                            <Route path='/projects/:id' element={<ProjectDetail projects={this.state.projects}/>}/>
                            <Route exact path='/projects/create'
                                   element={<ProjectCreateForm creatorsProject={this.state.users}
                                                               create_project={(name, creatorsProject, repository) => this.create_project(name, creatorsProject, repository)}/>}/>
                            <Route exact path='/projects/update/:uid'
                                   element={<ProjectUpdateForm creatorsProject={this.state.users}
                                                               project={this.state.projects}
                                                               update_project={(uid, name, creatorsProject, repository, project) => this.update_project(uid, name, creatorsProject, repository, project)}/>}/>
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
