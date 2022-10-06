import "./NotesIndex.css"
import { useState, useEffect } from "react";

const NotesIndex = () => {

let [notes, setNotes] = useState([])

useEffect( () => {
    getNotes()
}, [])

let getNotes = async () => {
    const res = await fetch("http://localhost:8000/api/users/")
    const data = await res.json()
    console.log(data)
    setNotes(data)
}


return(
    <div className="todo-list-container">
        <div className="todo-list">
            {notes.map( note => {
                return (
                    <div>{note.name}</div>
                )
            })}
        </div>
    </div>
)
}


export default NotesIndex;
