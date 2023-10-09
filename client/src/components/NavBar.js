import Navbar from 'react-bootstrap/Navbar'


export default function Login() {
  return (
    <nav className="menu">
      <ul>
        <li><a href="/register">Register</a></li>
        <li><a href="#">Login</a></li>
        <li><a href="#">Analyze</a></li>
      </ul>
    </nav>
  )
}