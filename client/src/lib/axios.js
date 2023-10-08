import axios from 'axios'
import { getToken, setToken, isTokenValid } from './auth'

const axiosAuth = axios.create()

axiosAuth.interceptors.request.use( async (config) => {
  
  //check if token is valid 
  if (!isTokenValid('access-token')) {
    if (isTokenValid('refresh-token')) {
      //Make an request to get new access token
      const { data } = await axios.post('/api/auth/refresh/', {
        refresh: getToken('refresh-token'), 
      })
      //save token to token variable
      setToken('access-token', data.access)
    } else { 
      //if the refresh token is expired as well, the user needs to log in again. 
      throw new axios.Cancel('Session expired. Please sign in again. ')
    }
  }

  //Add authorization header before sending
  config.headers.Authorization = `Bearer ${getToken('access-token')}`


  return config
})

export default axiosAuth




