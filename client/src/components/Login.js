import { useEffect, useState } from 'react'
import axios from 'axios'

import { setToken } from '../lib/auth'

import { Link } from 'react-router-dom'




export default function Login({ user, setUser, userName, setUserName }) {

  const [ message, setMessage ] = useState('')
  const [ formData, setFormData ] = useState({
    username: '', 
    password: '',
  })

  const handleChange = (e) => {
    setFormData( { ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      setUserName(formData.username)

      
      const { data } = await axios.post('/api/auth/login/', formData) 
      setUser(JSON.parse(atob(data.access.split('.')[1])).user_id )

      setToken('access-token', data.access)
      setToken('refresh-token', data.refresh)
      setMessage(`You are logged in as ${userName}`)
    } catch (error) {
      console.log(error)
      setMessage(error.response.data.detail)
    }
  }


  return (
    <form onSubmit={handleSubmit}> 
      <input type="username" name="username" placeholder="username" value={FormData.username} onChange={handleChange}></input>
      <br />
      <input type="password" name="password" placeholder="password" value={FormData.password} onChange={handleChange}></input>
      <br />
      
      <input className="input-submit" type = "submit" value= "Submit"></input>

      { message && <p className="message-to-user"> {message} <br/> {<Link to={`/analyze/${user}/`}> analyze portfolio </Link>}</p>}
    </form>
  )
}