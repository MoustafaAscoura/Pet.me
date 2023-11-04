import { BrowserRouter } from "react-router-dom";
import Router from "./router/Router";
import Header from "./components/header/Header";


function App() {
  return (
    <BrowserRouter>
      <Header />
      <div className="container my-5">
        <Router />
      </div>
    </BrowserRouter>
  );
}

export default App;
