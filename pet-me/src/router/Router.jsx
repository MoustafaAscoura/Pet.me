import { Route, Routes } from "react-router-dom";
import Home from "../pages/home-page/Home";
import Login from "../pages/login-page/Login";
import About from "../pages/about-page/About";
import Explore from "../pages/explore-page/Explore";
import Signup from "../pages/signup-page/Signup";
import PetInfo from "../pages/petinfo-page/PetInfo";
import Profile from "../pages/profile-page/Profile";
import PageNotFound from "../pages/notfound-page/PageNotFound";

const Router = () => {
    return ( 
        <Routes>
            <Route path="/" element={<Home />}/>
            <Route path="/login" element={<Login />}/>
            <Route path="/about" element={<About />}/>
            <Route path="/explore" element={<Explore />}/>
            <Route path="/signup" element={<Signup />}/>
            <Route path="/petinfo" element={<PetInfo />}/>
            <Route path="/profile" element={<Profile />}/>
            <Route path="/*" element={<PageNotFound />}/>

        </Routes>
     );
}
 
export default Router;