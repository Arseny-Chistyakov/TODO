import React from 'react';
import axios from 'axios';

import './bootstrap-css/bootstrap-css.min.css'
import './bootstrap-css/sticky-footer-navbar.css'
import './App.css';
import UserList from "./components/User";
import Footer from "./components/Footer";
import Navbar from "./components/Menu";

const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            navbarItems: [
                {name: 'Users', href: '/'},
                {name: 'Todo', href: '/todo'},
                {name: 'Project', href: '/project'},
            ],
            users: []

        }
    }

    componentDidMount() {
        axios.get(get_url('users/'))
            .then(response => {
                this.setState({'users': response.data.results})
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <div>
                    <header>
                        <Navbar navbarItems={this.state.navbarItems}/>
                    </header>
                    <main role="main" className="flex-shrink-0">
                        <div className="container">
                            <UserList users={this.state.users}/>
                        </div>
                    </main>
                    <Footer/>
                </div>
            </div>
        )
    }
}

export default App;
