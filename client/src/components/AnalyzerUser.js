import { useEffect, useState } from 'react'
import axios from 'axios'

// components
import CsvUpload from './CsvUpload'
import CsvUploadRow from './CsvUploadRow'

import PricesTable from './PricesTable'


export default function AnalyzerUser() {
  const [ tradeData, setTradeData ] = useState('')
  const [ formData, setFormData ] = useState({
    trade_table: '',
    trades: '', 
  })
  const [ message, setMessage ] = useState('')


  return (
    <div className='analyzer-container'>
      <a className= "file-template" href={'../assets/TestBuchführung.csv'} download> Download File Template </a>
      < CsvUpload
        formData={formData}
        setFormData={setFormData}
        setTradeData={setTradeData}
        message={message}
        setMessage={setMessage}
      />
      <br />
      {/* <h2> Add entry to existing table ... </h2>
      < CsvUploadRow
        formData={formData}
        setFormData={setFormData}
      /> */}

      <div className="table-container shadow-lg">
        { tradeData ?
          <div>
            <div>
              <h2> Trades </h2>
              <table>
                <thead>
                  <tr>
                    {Object.keys(tradeData.trades[0]).map((key) => (
                      <th key={key}>{key}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {tradeData.trades.map((trade, index) => (
                    <tr key={index}>
                      {Object.keys(trade).map((key) => (
                        <td key={key}>{trade[key]}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div> 

            <div >
              <h2> Prices </h2>
              <PricesTable 
                pricesOrDividents={tradeData.prices}
              />
            </div>
            {/* ! Do not return dividents */}

            
          </div> 
          : message &&
          <div className="m-3 d-flex justify-content-center">
            <div className="spinner-grow" role="status">
              <span className="sr-only"></span>
            </div>
          </div>}
      </div>
    </div>

  )
}