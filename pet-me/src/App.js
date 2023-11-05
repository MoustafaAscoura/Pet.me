import { BrowserRouter } from "react-router-dom";
import Router from "./router/Router";
import Header from "./components/header/Header";
import './app.css'
import Footer from "./components/footer/Footer";


function App() {
  return (
    <BrowserRouter>
      <Header />
      <div className="container main">
        <Router />
      </div>
      <Footer/>
    </BrowserRouter>
  );
}

export default App;
