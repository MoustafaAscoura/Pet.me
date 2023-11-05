import { BrowserRouter } from "react-router-dom";
import Router from "./router/Router";
import Header from "./components/header/Header";
import './app.css'


function App() {
  return (
    <BrowserRouter>
      <Header />
      <div className="container main">
        <Router />
      </div>
    </BrowserRouter>
  );
}

export default App;
