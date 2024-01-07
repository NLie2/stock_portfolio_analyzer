import React, { useEffect } from 'react'

export default function TestBuchführung() {
  const data = [
    { ticker: 'GOOGL.US', price: 705.7, shares: 1, costs: 0, taxes: 0, date: '2015-11-05', currencyPair: 'EURUSD.FOREX' },
    { ticker: 'AAPL.US', price: 264.425, shares: 20, costs: 0, taxes: 0, date: '2015-11-05', currencyPair: '-'  }

  ]

  const convertToCSV = (arr) => {
    const array = [Object.keys(arr[0])].concat(arr)
    return array.map(it => {
      return Object.values(it).toString()
    }).join('\n')
  }

  const createCSVFile = (data) => {
    const csvString = convertToCSV(data)
    const blob = new Blob([csvString], { type: 'text/csv;charset=utf-8;' })
    const fileUrl = URL.createObjectURL(blob)
    return fileUrl
  }

  const csvFileUrl = createCSVFile(data)

  useEffect(() => {
    return () => {
      URL.revokeObjectURL(csvFileUrl)
    }
  }, [csvFileUrl])

  return (
    <div>
      <a href={csvFileUrl} download="data.csv">Download CSV</a>
    </div>
  )
}
