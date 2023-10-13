import { useEffect, useState } from 'react'
import axiosAuth from '../lib/axios'
import NetworthTable from './NetworthTable'

//charts
import LineChart from './LineChart'
import Chart from 'chart.js/auto'
import { CategoryScale } from 'chart.js'

Chart.register(CategoryScale)


export default function Profile( { user } ) {
  const [ networths, setNetworths ] = useState()
  const [ owners, setOwners ] = useState()

  const [ labels, setLabels ] = useState()
  const [ chartData, setChartData ] = useState()

  const [ ownerToAnalyze, setOwnerToAnalyze ] = useState('')

  useEffect(() => {
    async function getNetworths(){
      try {
        const { data } = await axiosAuth.get('/api/networths/user/') 
        setNetworths( data )
      } catch (error) {
        console.log(error.response.data)
      }
    }
    getNetworths()
    
  }, [])

  useEffect(() => {
    networths && setOwners([... new Set(networths.map( (networth => networth.owner)))])
    networths && setLabels(networths.filter( networth => networth.owner === ownerToAnalyze).map( networth => networth.date ))
    networths && setChartData(networths.filter( networth => networth.owner === ownerToAnalyze).map( networth => networth.net_worth ))
  },[networths, ownerToAnalyze])

  const handleClick = (e) => {
    setOwnerToAnalyze( e.target.value )
  }

  return (
    <>
      <NetworthTable 
        networths={networths}
      />
      
      {owners && owners.map((owner, idx) => (
        <div key={idx}>
          <button onClick={handleClick} value={owner}>generate graph for {owner}&apos; s portfolio </button>
        </div>
      ))}
      
      {
        (networths && ownerToAnalyze) &&    <LineChart 
          chartLabels = {labels}
          chartData={chartData}
          graphLabel={ownerToAnalyze}
          color={'orange'}
        />
      }

    </>
  )
}