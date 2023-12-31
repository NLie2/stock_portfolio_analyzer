import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'

import axios from 'axios'

import { setToken } from '../lib/auth'

export default function Login() {

  const [ message, setMessage ] = useState('')
  const [ formData, setFormData ] = useState({
    username: '', 
    password: '',
    password_confirmation: '',
  })

  const handleChange = (e) => {
    setFormData( { ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      
      const { data } = await axios.post('/api/auth/register/', formData) 
      console.log(data, data.username)
      setMessage(`Registered as ${data.username}`)
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
      <input type="password" name="password_confirmation" placeholder="confirm password" value={FormData.password_confirmation} onChange={handleChange}></input>
      <br />
      
      <input className="input-submit" type = "submit" value= "Submit"></input>

      { message && <p> {message} <br/> <Link to={'/login'}> Login </Link></p>}
    </form>
  )
}