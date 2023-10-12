export default function Table( { tradeData, title }){
  return (
    <div >
      <h1> {title} </h1>
      <table>
        <tr>
          <th>Prices</th>
          <th>Dividents</th>
          <th>Trades</th>
        </tr>
        <tr>
          <td>{tradeData.prices['AAPL.US'][0]['close']}</td>
          <td>{tradeData.dividents['AAPL.US'][0]['close']}</td>
          <td>{tradeData.dividents['AAPL.US'][0]['close']}</td>
        </tr>
        <tr>
          {tradeData.dividents['AAPL.US'][0]['close']}
        </tr>
      </table>
    </div>
  )
}