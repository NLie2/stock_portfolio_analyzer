import { useState, useEffect } from 'react'

export default function PricesTable( { title, prices }){
  const [ counter, setCounter ] = useState(0)
  const [ colnames, setColnames ] = useState('')
  useEffect(() => {
    setColnames(Object.keys(prices[Object.keys(prices)[0]][0]))
  }, [])


  console.log('COLNAMES',colnames)

  console.log('keys', Object.keys(prices[Object.keys(prices)[0]][0]), Object.keys(prices))
  for (const price in prices){
    console.log(Object.keys(price), 'one by one...')
  }
  Object.keys(prices).map( ticker => console.log(ticker))

  return (
    <div >
      <h2> {title} </h2>
      <table>
        <thead>
          <td>Ticker</td>
          {colnames && colnames.map((colname, index) => (
            <td key={index}>{colname}</td>
          ))}
        </thead>
        <tbody>
          {Object.entries(prices).map(([symbol, data]) => (
            data.map((price, index) => (
              <tr key={index}>
                {Object.keys(prices).map( (ticker, ind) => <td key={ind}>{ticker}</td>)}
                {colnames &&
                  colnames.map((colname, ind) => (
                    
                    <td key={ind}>{price[colname]}</td>
                  ))}
              </tr>
            ))
          ))}
        </tbody>
      </table>
    </div>
  )
}