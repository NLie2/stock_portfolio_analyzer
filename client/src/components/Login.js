import { useEffect, useState } from 'react'
import axios from 'axios'

import { setToken } from '../lib/auth'




export default function Login() {
  const [ message, setMessage ] = useState('')
  const [ formData, setFormData ] = useState( {
    username: '', 
    password: '',
  })

  const handleChange = (e) => {
    setFormData( { ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      
      const { data } = await axios.post('/api/auth/login/', formData) 
      setToken('access-token', data.access)
      setToken('refresh-token', data.refresh)
      setMessage('Login was successful')
    } catch (error) {
      console.log(error)
      setMessage(error.response.data.detail)
    }
  }


  return (
    <form onSubmit={handleSubmit}> 
      <input type="username" name="username" value={FormData.username} onChange={handleChange}></input>
      <br />
      <input type="password" name="password" value={FormData.username} onChange={handleChange}></input>
      <br />
      { message && <p> {message}</p>}
      <input type = "submit" value= "Submit"></input>
    </form>
  )
}