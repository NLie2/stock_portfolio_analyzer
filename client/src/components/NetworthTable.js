export default function NetworthTable( { networths } ){
  return (
    <>
      {networths && <div className='networths'>
        <h1> Networths </h1>
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
      
    </>
  )
}