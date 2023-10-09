import { useEffect, useState } from 'react'
import axios from 'axios'

// components
import CsvUpload from './CsvUpload'


export default function AnalyzerUser() {

  const [ formData, setFormData ] = useState({
    trades_table: '', 
  })


  return (
    <>
      <h1> ANALYZER USER </h1>
      < CsvUpload
        formData={formData}
        setFormData={setFormData}
      />
    </>

  )
}