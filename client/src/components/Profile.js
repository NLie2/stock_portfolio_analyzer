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
    networths && setLabels(networths.filter( networth => networth.owner === 'nathalie').map( networth => networth.date ))
    networths && setChartData(networths.filter( networth => networth.owner === 'nathalie').map( networth => networth.net_worth ))
  },[networths])
  console.log(networths, owners, labels, chartData)

  return (
    <>
      <NetworthTable 
        networths={networths}
      />
      
      {owners && owners.map((owner, idx) => (
        <div key={idx}>
          <button>generate graph for {owner}&apos; s portfolio </button>
        </div>
      ))}
      
      {
        networths &&    <LineChart 
          chartLabels = {labels}
          chartData={chartData}
        />
      }

    </>
  )
}