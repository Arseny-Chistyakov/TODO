import React from "react";

class TODOCreateForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {body: '', creatorKeep: '', project: ''}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
    }

    handleSubmit(event) {
        this.props.create_TODO(this.state.body, this.state.creatorKeep, this.state.project)
        window.location.href = '/TODOs';
        event.preventDefault()
    }

    render() {
        return (
            <div className={"container"}>
                <div className={"d-flex justify-content-center"}>
                    <div className={"card shadow-lg border-0 rounded-lg mt-5"}>
                        <div className={"card-header"}>
                            <h3 className={"text-center font-weight-light my-4"}>______Создание заметки______</h3>
                        </div>
                        <div className={"card-body"}>
                            <form onSubmit={(event) => this.handleSubmit(event)}>
                                <div className={"form-group"}>
                                    <label className={"mb-0"}>Введите содержимое заметки</label>
                                    <input className={"form-control"} type="text" name="body" placeholder="Текст"
                                           value={this.state.body}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                                <div className={"form-group"}>
                                    <label className={"mb-0 mt-1"}>Выберете проект</label>
                                    <select className={"form-control"} name="project"
                                            onChange={(event) => this.handleChange(event)}>{this.props.project.map((item) =>
                                        <option value={item.uid}>{item.name}</option>)}
                                    </select>
                                </div>
                                <div className={"form-group"}>
                                    <label className={"mb-0 mt-1"}>Выберете создателя заметки</label>
                                    <select className={"form-control"} name="creatorKeep"
                                            onChange={(event) => this.handleChange(event)}>
                                        {this.props.creatorKeep.map((item) => <option
                                            value={item.uid}>{item.username}</option>)}
                                    </select>
                                </div>
                                <label className={"form-text text-muted"}>*перед добавлением, следует обязательно
                                    выбрать все поля</label>
                                <input className={"btn btn-secondary mt-1"} type="submit" value="Добавить"/>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default TODOCreateForm