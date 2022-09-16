import React, {useState} from 'react'
import {Link, useParams} from "react-router-dom";

const ProjectItem = ({project, delete_project}) => {
    return (
        <tr>
            <td><Link to={`${project.uid}`} className={"table-link"}>{project.name}</Link></td>
            <td>{project.repository}</td>
            <td>{project.creatorsProject.join(", ")}</td>
            <td>
                <button onClick={() => delete_project(project.uid)} type='button' className={"btn btn-secondary"}>
                    Удалить
                </button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects, delete_project}) => {
    const [inputValue, setInputValue] = useState();
    const handleChange = (event) => {
        let lowerCase = event.target.value.toLowerCase();
        setInputValue(lowerCase);
    };
    const filteredData = projects.filter((projects) => {
            let input = document.getElementById("input");
            let inputVal = ''
            if (input) {
                inputVal = input.value
            } else {
                inputVal = ''
            }
            if (inputVal === '') {
                return projects;
            } else {
                return (projects.name.toLowerCase().includes(inputValue))
            }
        }
    )

    return (
        <div className="container">
            <div className={"mt-4 d-flex justify-content-center"}>
                <input type={"search"} placeholder="Поиск по имени проекта" id="input" value={inputValue}
                       onChange={handleChange}/>
                <button className={"btn btn-secondary ml-5"}>
                    <Link to="/projects/create" className={"text-decoration-none text-white"}>Создать проект</Link>
                </button>
                <button type='button' className={"btn btn-secondary ml-5"}>
                    <Link to={"/projects/update/"} className={"text-decoration-none text-white"}>Обновить</Link>
                </button>
            </div>
            <table className="table table-hover mt-3">
                <thead>
                <tr>
                    <th>Название проекта</th>
                    <th>Репозитории</th>
                    <th>Создатели проекта</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {Array.isArray(filteredData) ? filteredData.map((project) => <ProjectItem project={project}
                                                                                          delete_project={delete_project}/>) : null}
                </tbody>
            </table>
        </div>
    )
}


const ProjectDetail = ({projects}) => {
    let detailedProjectId = useParams()
    let filteredProject = projects.filter((project) => project.uid === detailedProjectId.id)[0]

    return (
        <div className={"container"}>
            <div className={"d-flex justify-content-center"}>
                <div className={"card shadow-lg border-0 rounded-lg mt-5"}>
                    <div className="card-header">
                        <h3 className="text-center my-2">
                            <em>Название проекта:</em> {filteredProject.name}</h3>
                    </div>
                    <div className={"card-body text-left"}>
                        <p className="card-text "><em>Ссылка на проект:</em>
                            <a className={"table-link"} href={filteredProject.repository}>
                                {filteredProject.repository}</a>
                        </p>
                        <div className={"form-group"}>
                            <label className={"mb-0 card-text text-decoration-underline"}><em>Список
                                разработчиков проекта:</em></label>
                            {filteredProject.creatorsProject.map((creatorsProject, index) => {
                                return (
                                    <p className="card-text">{index + 1}. {creatorsProject} </p>)
                            })}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export {ProjectList, ProjectDetail}