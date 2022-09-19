import React from "react";

class ProjectCreateForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {name: '', creatorsProject: [], repository: ''}
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleCreatorsProjectChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({
                'creatorsProject': []
            })
            return;
        }
        let creatorsProject = []
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            creatorsProject.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({'creatorsProject': creatorsProject})
    }

    handleSubmit(event) {
        this.props.create_project(this.state.name, this.state.creatorsProject, this.state.repository)
        window.location.href = '/projects';
        event.preventDefault()
    }

    render() {
        return (
            <div className={"container"}>
                <div className={"d-flex justify-content-center"}>
                    <div className={"card shadow-lg border-0 rounded-lg mt-5"}>
                        <div className="card-header">
                            <h3 className="text-center font-weight-light my-4">______Создание проекта______</h3>
                        </div>
                        <div className={"card-body"}>
                            <form onSubmit={(event) => this.handleSubmit(event)}>
                                <div className={"form-group"}>
                                    <label className={"mb-0"}>Введите название проекта</label>
                                    <input className={"form-control"} type="text" name="name"
                                           placeholder="Название"
                                           value={this.state.name}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                                <div className={"form-group"}>
                                    <label className={"mb-0 mt-1"}>Введите ссылку на репозитории</label>
                                    <input className={"form-control"} type="text" name="repository"
                                           placeholder="Репозитории" value={this.state.repository}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                                <div className={"form-group"}>
                                    <label className={"mb-0 mt-1"}>Выберете участника(ов) проекта</label>
                                    <select className={"form-control"} name="creatorsProject" multiple
                                            onChange={(event) => this.handleCreatorsProjectChange(event)}>
                                        {this.props.creatorsProject.map((item) => <option
                                            value={item.uid}>{item.username}</option>)}
                                    </select>
                                </div>
                                <input className={"btn btn-secondary mt-1"} type="submit" value="Добавить"/>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default ProjectCreateForm