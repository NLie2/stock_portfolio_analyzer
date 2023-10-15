export default function NetworthTable( { networths } ){
  return (
    <div className="shadow-lg table-container">
      <h1> Networths </h1>
      {networths && <div className='table'>
        <table>
          <thead>
            <tr>
              <th>owner</th>
              <th>date</th>
              <th>networth</th>
            </tr>
          </thead>
          <tbody>
            {networths.map((row, index) => (
              <tr key={index}>
                <td>{row.owner}</td>
                <td>{row.date}</td>
                <td>{row.net_worth}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div> }
    </div>
  )
}