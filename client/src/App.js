import { useEffect } from 'react'
import { BrowserRouter, Routes, Route, useParams } from 'react-router-dom'

import Footer from './components/Footer'
import NavBar from './components/NavBar'

import Landing from './components/Landing'

import Login from './components/Login'
import Register from './components/Register'
import Profile from './components/Profile'


import AnalyzerGuest from './components/AnalyzerGuest'
import AnalyzerUser from './components/AnalyzerUser'


export default function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element= {<Landing />} />
          <Route path='/login/' element= {<Login />} />
          <Route path='/register/' element= {<Register />} />
          <Route path='/profile/:userid/' element= {<Profile />} />

          <Route path='/analyze/guest/' element= {<AnalyzerGuest />} />
          <Route path='/analyze/:userid/' element= {<AnalyzerUser />} />

        </Routes>
      </BrowserRouter>
    </>
  )
}
