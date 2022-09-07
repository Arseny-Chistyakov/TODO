import React from 'react'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.username}</td>
            <td>{user.firstName}</td>
            <td>{user.lastName}</td>
            <td>{user.email}</td>
            <td>{user.created}</td>
            <td>{user.modified}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table className="table container-md mt-5">
            <thead>
            <tr>
                <th>Логин</th>
                <th>Имя</th>
                <th>Фамилия</th>
                <th>Email</th>
                <th>Создан</th>
                <th>Изменен</th>
            </tr>
            </thead>
            <tbody>
            {Array.isArray(users) ? users.map((user) => <UserItem user={user} key={user.uid}/>) : null}
            </tbody>
        </table>
    )
}

export default UserList