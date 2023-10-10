import Container from 'react-bootstrap/Container'
import Nav from 'react-bootstrap/Nav'
import Navbar from 'react-bootstrap/Navbar'


export default function Login( { user } ) {
  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        <Nav className="me-auto">
          <Nav.Link href="/login/">Login</Nav.Link>
          <Nav.Link href="/register/">Register</Nav.Link>

          {/* If the user is logged in, then the analyze link will lead to the user page, if not it will lead to the guest page */}
          { user ? <Nav.Link href="/analyze/user/">Analyze</Nav.Link> :  <Nav.Link href="/analyze/guest/">Analyze</Nav.Link> }
        </Nav>
      </Container>
    </Navbar>
  )
}