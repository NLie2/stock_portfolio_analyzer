import axios from 'axios'

import Papa from 'papaparse'

import { useEffect, useState } from 'react'

export default function CsvUpload( { formData, setFormData }){
  const [ message, setMessage ] = useState('')

  const data = new FormData()

  const handleUpload = async (e) => {

    // data.append('file', e.target.files[0] ) 
    // console.log('FILE CHANGED', data)

    const file = e.target.files[0]

    Papa.parse(file, {
      header: true, 
      dynamicTyping: true,
      complete: function(results) {
        console.log('Finished:', results.data)
      } })

    // const reader = new FileReader()

    // reader.onload = function(event) {
    //   // The file's text will be printed here
    //   console.log(event.target.result)
    // }
  
    // reader.readAsText(file)

  }

  const handleSubmit = async (e) => {
    try { 
      const { res } = await axios.post('/api/auth/trades/', data )
      console.log(res.data)

      setFormData = { ...formData, trades_table: res }

    } catch (error) {
      console.log(error)
      setMessage(error.response.data.detail)
    }
  }

  return (
    <form onSubmit={handleSubmit}> 
      <input type="file" name="trades_table" placeholder="trades_table"  onChange={handleUpload}></input>
      <br />
      { message && <p> {message}</p>}
      <input type = "submit" value= "Submit"></input>
    </form>
  )
}