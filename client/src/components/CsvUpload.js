import axios from 'axios'
import axiosAuth from '../lib/axios'

import Papa from 'papaparse'

import { useEffect, useState } from 'react'

export default function CsvUpload( { formData, setFormData }){
  const [ message, setMessage ] = useState('')

  const data = new FormData()

  const handleUpload = async (e) => {

    const file = e.target.files[0]

    Papa.parse(file, {
      header: true, 
      dynamicTyping: true,
      complete: function(results) {
        console.log('Finished:', results.data)
        console.log('Finished:', { ...results.data[0] })

        setFormData( { ...formData, ...results.data[0] } )

      } })


    console.log('data',  formData)

  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try { 
      const { res } = await axiosAuth.post('/api/trades/', formData )
      res && console.log(res.data)
      setMessage('CSV uploaded')

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