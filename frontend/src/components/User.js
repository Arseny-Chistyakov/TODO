import React from 'react'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.username}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
            <td>{user.created}</td>
            <td>{user.modified}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table className="table">
            <tr>
                <th>Username</th>
                <th>First name</th>
                <th>Last name</th>
                <th>Email</th>
                <th>Created</th>
                <th>Modified</th>
            </tr>
            {users.map((user) => <UserItem user={user}/>)}
            {/*{Array.isArray(users) ? users.map((user) => <UserItem user={user}/>) : null}*/}
        </table>
    )
}

export default UserList