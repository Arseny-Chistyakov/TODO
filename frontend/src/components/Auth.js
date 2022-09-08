import React from 'react'

class LoginForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {login: '', password: ''}
    }


    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.login(this.state.login, this.state.password)
        event.preventDefault()
    }


    render() {
        return (
            <div className="container">
                <form onSubmit={(event) => this.handleSubmit(event)}>
                    <div className="row justify-content-center p-5">
                        <div className="col-lg-5">
                            <div className={"card shadow-lg border-0 rounded-lg mt-5"}>
                                <div className="card-header"><h3
                                    className="text-center font-weight-light my-4">Авторизация</h3></div>
                                <div className="card-body">
                                    <div className="form-group">
                                        <label className="small mb-1" htmlFor="login">Логин</label>
                                        <input type="text" className="form-control" name="login"
                                               value={this.state.login}
                                               onChange={(event) => this.handleChange(event)}/>
                                    </div>
                                    <div className="form-group">
                                        <label className="small mb-1" htmlFor="password">Пароль</label>
                                        <input type="password" className="form-control" name="password"
                                               value={this.state.password}
                                               onChange={(event) => this.handleChange(event)}/>
                                    </div>
                                    <input type="submit" className="btn btn-secondary" value="Авторизоваться"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        );
    }
}

export default LoginForm
