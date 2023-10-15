import Container from 'react-bootstrap/Container'
import Nav from 'react-bootstrap/Nav'

import Navbar from 'react-bootstrap/Navbar'

import { Link } from 'react-router-dom'


export default function NavBar( { user, userName } ) {

  return (
    <Navbar expand="lg" className="bg-body-tertiary shadow-lg">
      <Container className='navbar'>
        <Nav className="me-auto">
          <Link to="/login/">Login</Link>
          <Link to="/register/">Register</Link>

          {/* If the user is logged in, then the analyze link will lead to the user page, if not it will lead to the guest page */}
          { user ? <Link to={`/analyze/${user}/`}>Analyze</Link> :  <Link to="/analyze/guest/">Analyze</Link> }
          { user && <Link to={`/profile/${user}/`}>Profile {userName}</Link> }
        </Nav>
      </Container>
    </Navbar>
  )
}