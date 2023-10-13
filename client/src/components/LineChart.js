// components/LineChart.js
import React from 'react'
import { Line } from 'react-chartjs-2'

export default function LineChart( { chartLabels, chartData, graphLabel, color } ) {

  const data = {
    labels: chartLabels,
    // datasets is an array of objects where each object represents a set of data to display corresponding to the labels above. for brevity, we'll keep it at one object
    datasets: [
      {
        label: graphLabel,
        data: chartData,
        // you can set indiviual colors for each bar
        backgroundColor: [
          'rgba(255,165,0, 1)',
          'rgba(255,165,0, 1)',
          'rgba(255,165,0, 1)'
        ],
        borderColor: color,
        borderWidth: 4,
      }
    ],
  }
  return (

    <div className="chart-container">
      <h3 style={{ textAlign: 'center' }}>{graphLabel}&apos;s portfolio networth</h3>
      <Line
        data={data}
        options={{
          plugins: {
            title: {
              display: true,
              // text: 'Users Gained between 2016-2020',
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