import { useState, useEffect } from 'react'

export default function PricesTable( { pricesOrDividents }){
  const [ counter, setCounter ] = useState(0)
  const [ colnames, setColnames ] = useState('')
  useEffect(() => {
    setColnames(Object.keys(pricesOrDividents[Object.keys(pricesOrDividents)[0]][0]))
  }, [])

  return (
    <div className="table">
      <table>
        <thead>
          <tr>
            <th>Ticker</th>
            {Object.keys(pricesOrDividents[Object.keys(pricesOrDividents)[0]][0]).map((key) => (
              <th key={key}>{key}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {Object.entries(pricesOrDividents).map(([ticker, data]) => (
            data.map((entry, index) => (
              <tr key={index}>
                <td>{ticker}</td>
                {Object.values(entry).map((value, index) => (
                  <td key={index}>{value}</td>
                ))}
              </tr>
            ))
          ))}
        </tbody>
      </table>
    </div>
  )
}