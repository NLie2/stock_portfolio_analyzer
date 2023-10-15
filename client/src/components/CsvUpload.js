import axios from 'axios'
import axiosAuth from '../lib/axios'

import Papa from 'papaparse'

import { useEffect, useState } from 'react'

import JSONPretty from 'react-json-pretty'

import Table from './PricesTable'

export default function CsvUpload( { formData, setFormData, setTradeData, message, setMessage }){
  const [ owner, setOwner ] = useState('')

  const data = new FormData()

  const handleUpload = async (e) => {

    const file = e.target.files[0]

    Papa.parse(file, {
      header: true, 
      dynamicTyping: true,
      complete: function(results) {
        console.log('Finished:', results.data)

        setFormData( { ...formData, trade_table: { owner: owner }, trades: results.data } )
        console.log('check formdata... ', formData)

      } })

  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try { 
      console.log(formData)
      setMessage( 'CSV uploaded' )
      const { data }  = await axiosAuth.post('/api/tradetables/', formData )
      if (data) {
        console.log('response...', data)
        setTradeData( data )
      } else {
        setMessage('something went wrong')
      }


    } catch (error) {
      console.log(error)
      setMessage(error.response.data.detail)
    }
  }

  return (
    <div className="shadow-lg">
      <h3> Upload new table ... </h3>
      <form onSubmit={handleSubmit}> 
        {/* This should be a select later, so that the user can select between all existing tables*/}
        <input type="string" name="owner" placeholder="owner"  onChange={ (e) => setOwner(e.target.value) }></input>

        <input className="input-upload" type="file" name="trades_table" placeholder="trades_table"  onChange={handleUpload}></input>
        <br />
        <input className="input-submit" type = "submit" value= "Submit"></input>

        { message && <p className="message-to-user"> {message} </p>}
      </form>
      
    </div>
  )
}