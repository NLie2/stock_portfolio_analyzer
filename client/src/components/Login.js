import { useEffect } from 'react'
import axiosAuth from '../lib/axios'

import { setToken } from '../lib/auth'


export default function Login() {

  useEffect(() => {
    async function getData(){
      try {
        const { data } = await axiosAuth.post('/api/auth/login/')
        console.log(data)
      } catch (error) {
        console.log(error.response.data)
      }
    }
    getData()
  }, [])

  return (
    <h1>LOGIN</h1>
  )
}