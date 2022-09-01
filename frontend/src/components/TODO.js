import React from 'react'


const TODOItem = ({TODO}) => {
    return (
        <tr>
            <td>{TODO.body}</td>
            <td>{TODO.creatorKeep}</td>
            <td>{TODO.project}</td>
            <td>{TODO.created}</td>
            <td>{TODO.modified}</td>
            <td>{TODO.isActive ? 'Active' : 'CLose'}</td>
        </tr>
    )
}

const TODOList = ({TODOs}) => {
    return (
        <table className="table container-md mt-5">
            <thead>
            <tr>
                <th>Text</th>
                <th>Creator keep</th>
                <th>Project</th>
                <th>Created</th>
                <th>Modified</th>
                <th>Active</th>
            </tr>
            </thead>
            <tbody>
            {Array.isArray(TODOs) ? TODOs.map((TODO) => <TODOItem TODO={TODO} key={TODO.uid}/>) : null}
            </tbody>
        </table>
    )
}

export default TODOList
