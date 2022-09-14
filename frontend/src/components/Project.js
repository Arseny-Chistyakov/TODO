import React from 'react'
import {Link, useParams} from "react-router-dom";

const ProjectItem = ({project, delete_project}) => {
    return (
        <tr>
            <td><Link to={`${project.uid}`} className={"text-decoration-none text-dark "}>{project.name}</Link></td>
            <td>{project.repository}</td>
            <td>{project.creatorsProject}</td>
            <button className={"btn btn-secondary"} onClick={() => delete_project(project.uid)} type='button'>Удалить
            </button>
        </tr>
    )
}

const ProjectList = ({projects, delete_project}) => {
    return (
        <div className="container">
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
                {Array.isArray(projects) ? projects.map((project) => <ProjectItem project={project}
                                                                                  delete_project={delete_project}
                                                                                  key={project.uid}/>) : null}
                </tbody>
            </table>
            <button className={"btn btn-secondary"}><Link className={"text-decoration-none text-white"}
                                                          to="/projects/create">Создать проект</Link></button>
        </div>
    )
}


const ProjectDetail = ({projects}) => {
    let detailedProjectId = useParams()
    let filteredProject = projects.filter((project) => project.uid === detailedProjectId.id)[0]

    return (
        <div className="container">
            <div className="card-body">
                <h5 className=''>Название проекта: {filteredProject.name}</h5>
                <p className="card-text">Ссылка на проект: <a
                    href={filteredProject.repository}> {filteredProject.repository}</a>
                </p>
                {filteredProject.creatorsProject.map((creatorsProject, index) => {
                    return (
                        <p>Создатель {index + 1}. {creatorsProject} </p>)
                })}
            </div>
        </div>
    );
};

export {ProjectList, ProjectDetail}