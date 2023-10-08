export const getToken = ( tokenName ) => {
  return localStorage.getItem(tokenName)
}

export const setToken = ( tokenName, token) => {
  localStorage.setItem(tokenName, token)
}

export const isTokenValid = ( tokenName ) => {

  //get the token
  const token = getToken(tokenName)

  //get current date and expiration date from token (which is encoded in a JSON web token)
  const exp = JSON.parse(atob(token.split('.')[1])).exp 
  const now = Date.now() / 1000

  return exp > now  // expiry data should be in the future
}