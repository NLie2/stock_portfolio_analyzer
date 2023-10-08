import axios from 'axios'

import { getToken, setToken, isTokenValid } from './auth'

const axiosAuth = axios.create()

axiosAuth.interceptors.create( async (config) => {
  
  //check if token is valid 
  if (!isTokenValid('accessToken')) {
    if (isTokenValid('refreshToken')) {
      //Make an request to get new access token
      const { data } = await axios.post('/api/auth/refresh', {
        refresh: getToken('refresh-token'), 
      })
      //save token to token variable
      setToken('access-token', data.access)
    } else { 
      //if the refresh token is expired as well, the user needs to log in again. 
      throw new axios.Cancel('Session expired. Please sign in again. ')
    }
  }
})

export default axiosAuth
