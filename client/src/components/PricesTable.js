import { useState, useEffect } from 'react'

export default function PricesTable( { pricesOrDividents }){
  const [ counter, setCounter ] = useState(0)
  const [ colnames, setColnames ] = useState('')
  useEffect(() => {
    setColnames(Object.keys(pricesOrDividents[Object.keys(pricesOrDividents)[0]][0]))
  }, [])

  return (
    <div className="table">
      <table > 
        <thead>
          <tr>
            <th>Ticker</th>
            {colnames && colnames.map((colname, index) => (
              <th key={index}>{colname}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {Object.entries(pricesOrDividents).map(([symbol, data]) => (
            data.map((priceOrDivident, index) => (
              <tr key={index}>
                {Object.keys(pricesOrDividents).map( (ticker, ind) => <td key={ind}>{ticker}</td>)}
                {colnames &&
                  colnames.map((colname, ind) => (
                    
                    <td key={ind}>{priceOrDivident[colname]}</td>
                  ))}
              </tr>
            ))
          ))}
        </tbody>
      </table>
    </div>
  )
}