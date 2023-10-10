import { useEffect, useState } from 'react'
import axios from 'axios'

// components
import CsvUpload from './CsvUpload'
import CsvUploadRow from './CsvUploadRow'


export default function AnalyzerUser() {

  const [ formData, setFormData ] = useState({
    trade_table: '',
    trades: '', 
  })


  return (
    <>
      <h1> ANALYZER USER </h1>

      <h2> Upload new table ... </h2>

      < CsvUpload
        formData={formData}
        setFormData={setFormData}
      />
      <br />
      <h2> Add entry to existing table ... </h2>
      < CsvUploadRow
        formData={formData}
        setFormData={setFormData}
      />
    </>

  )
}