import { useEffect, useState } from 'react'
import axios from 'axios'


export default function AnalyzerGuest() {
  const [ message, setMessage ] = useState('')
  const [ formData, setFormData ] = useState({
    trades_table: '', 
  })

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      
      // const { data } = await axios.post('/api/auth/login/', formData) 

      setMessage('CSV uploaded')
    } catch (error) {
      console.log(error)
      setMessage(error.response.data.detail)
    }
  }

  const handleChange = (e) => {
    setFormData( { ...formData, [e.target.name]: e.target.value })
  }


  return (
    <form onSubmit={handleSubmit}> 
      <input type="file" name="trades_table" placeholder="trades_table" value={FormData.trades_table} onChange={handleChange}></input>
      <br />
      { message && <p> {message}</p>}
      <input type = "submit" value= "Submit"></input>
    </form>
  )
}