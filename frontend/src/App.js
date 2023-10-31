import NavBar from './components/NavBar/NavBar';
import { Container } from "react-bootstrap";
import { Route, Switch } from "react-router-dom";
import "./api/axiosDefaults";
import SignUpForm from './pages/auth/SignUpFrom';

function App() {
  return (
    <div>
        <NavBar/>
      <Container>
        {/* Use the Switch component to handle routing */}
        <Switch>
          {/* Route for the pages */}
        <Route path="/" exact render = { () => <h1>Home Page</h1>} />
        <Route path="/login" exact render = { () => <h1>Sign in</h1>} />
        <Route path="/create" exact render = { () => <SignUpForm />} />
        <Route path="/user-favorites/" exact render = { ()=> <h1>My Favorites</h1> }/>
        
        {/* ROute for page not found */}
        <Route render = { () => <p>Page not found!</p>} />
        </Switch>


      </Container>
    </div>
  );
}

export default App;