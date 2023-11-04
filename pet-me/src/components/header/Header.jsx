import { faCartShopping } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link, NavLink } from "react-router-dom";



function Header() {
    
    

  return (
    <>
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
        <div className="container-fluid">
          <NavLink className={({ isActive, isPending }) => {
                return isActive ? "text-success nav-link fw-bold fs-5" : "nav-link fw-bold fs-5";
            }} to="/">
            Pet me
          </NavLink>

          <div className="d-flex">
            <NavLink
              className={({ isActive, isPending }) => {
                return isActive ?"nav-link active m-2 text-success fs-5": "nav-link active m-2";
            }}
              aria-current="page"
              to="/register"
            >
              Register
            </NavLink>
            <NavLink
              className={({ isActive, isPending }) => {
                return isActive ?"text-success nav-link active m-2 fs-5" :"nav-link active m-2";
            }}
              aria-current="page"
              to="/login"
            >
              Login
            </NavLink>
            
          </div>
        </div>
      </nav>
    </>
  );
}

export default Header;