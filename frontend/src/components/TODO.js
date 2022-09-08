import React from 'react'


const TODOItem = ({TODO}) => {
    return (
        <tr>
            <td>{TODO.body}</td>
            <td>{TODO.creatorKeep}</td>
            <td>{TODO.project}</td>
            <td>{TODO.created}</td>
            <td>{TODO.modified}</td>
            <td>{TODO.isActive ? 'Активна' : 'Закрыта'}</td>
        </tr>
    )
}

const TODOList = ({TODOs}) => {
    return (
        <table className="table container-md mt-5">
            <thead>
            <tr>
                <th>Текст заметки</th>
                <th>Создатель заметки</th>
                <th>Проект</th>
                <th>Создана</th>
                <th>Изменена</th>
                <th>Статус</th>
            </tr>
            </thead>
            <tbody>
            {Array.isArray(TODOs) ? TODOs.map((TODO) => <TODOItem TODO={TODO} key={TODO.uid}/>) : null}
            </tbody>
        </table>
    )
}

export default TODOList
