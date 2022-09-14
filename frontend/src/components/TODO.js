import React from 'react'
import {Link} from "react-router-dom";


const TODOItem = ({TODO, delete_TODO}) => {
    return (
        <tr>
            <td>{TODO.body}</td>
            <td>{TODO.creatorKeep}</td>
            <td>{TODO.project}</td>
            <td>{TODO.created}</td>
            <td>{TODO.modified}</td>
            <td>{TODO.isActive ? 'Активна' : 'Закрыта'}</td>
            <button className={"btn btn-secondary"} onClick={() => delete_TODO(TODO.uid)} type='button'>Удалить</button>
        </tr>
    )
}

const TODOList = ({TODOs, delete_TODO}) => {
    return (
        <div className={"container mb-4"}>
            <table className="table table-hover mt-3">
                <thead>
                <tr>
                    <th>Текст заметки</th>
                    <th>Создатель заметки</th>
                    <th>Проект</th>
                    <th>Создана</th>
                    <th>Изменена</th>
                    <th>Статус</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {Array.isArray(TODOs) ? TODOs.map((TODO) => <TODOItem TODO={TODO} delete_TODO={delete_TODO}/>) : null}
                </tbody>
            </table>
            <button className={"btn btn-secondary"}><Link className={"text-decoration-none text-white"}
                                                          to="/TODOs/create">Создать заметку</Link></button>
        </div>
    )
}

export default TODOList
