import { useEffect } from 'react'
import axiosAuth from '../lib/axios'


export default function Login() {
  useEffect(() => {
    async function getData(){
      try {
        const { data } = await axiosAuth.get('/api/trades/') // <---- Replace with your endpoint to test the proxy
        console.log(data)
      } catch (error) {
        console.log(error.response.data)
      }
    }
    getData()
  }, [])

  return (
    <h1>ANALYZER USER</h1>
  )
}