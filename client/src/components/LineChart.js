// components/LineChart.js
import React from 'react'
import { Line } from 'react-chartjs-2'

export default function LineChart( { chartLabels, chartData } ) {

  console.log('chart data', chartLabels, chartData)



  const data = {
    labels: chartLabels,
    // datasets is an array of objects where each object represents a set of data to display corresponding to the labels above. for brevity, we'll keep it at one object
    datasets: [
      {
        label: 'Popularity of colours',
        data: chartData,
        // you can set indiviual colors for each bar
        backgroundColor: [
          'rgba(255,165,0, 1)',
          'rgba(255,165,0, 1)',
          'rgba(255,165,0, 1)'
        ],
        borderWidth: 1,
      }
    ],
  }
  return (

    <div className="chart-container">
      <h2 style={{ textAlign: 'center' }}>Line Chart</h2>
      <Line
        data={data}
        options={{
          plugins: {
            title: {
              display: true,
              text: 'Users Gained between 2016-2020',
            },
            legend: {
              display: false,
            },
          },
        }}
      />
    </div>
  )
}