import NavBar from "./components/NavBar";
import styles from "./App.module.css";
import { Container } from "react-bootstrap";
import { Route, Switch } from "react-router-dom";

function App() {
  return (
    <div className={styles.App}>
        <NavBar/>
      <Container>
        {/* Use the Switch component to handle routing */}
        <Switch>
          {/* Route for the pages */}
        <Route path="/" exact render = { () => <h1>Home Page</h1>} />
        <Route path="/login" exact render = { () => <h1>Sign in</h1>} />
        <Route path="/create" exact render = { () => <h1>Sign up</h1>} />
        <Route path="/user-favorites/" exact render = { ()=> <h1>My Favorites</h1> }/>
        
        {/* ROute for page not found */}
        <Route render = { () => <p>Page not found!</p>} />
        </Switch>


      </Container>
    </div>
  );
}

export default App;