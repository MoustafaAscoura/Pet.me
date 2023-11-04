import { faComments } from "@fortawesome/free-regular-svg-icons";
import {faMagnifyingGlass,faPaw} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import "./style.css";

function Header() {
  return (
    <nav className="navbar navbar-expand-lg fixed-top">
      <div className="container">
        <div
          className="navbar-brand me-auto fw-bold"
          style={{ color: "#8c594d" }}
        >
          <FontAwesomeIcon icon={faPaw} className="me-2" />
          Pet.me
        </div>
        <div
          className="offcanvas offcanvas-end"
          tabindex="-1"
          id="offcanvasNavbar"
          aria-labelledby="offcanvasNavbarLabel"
        >
          <div className="offcanvas-header">
            <h5 className="offcanvas-title" id="offcanvasNavbarLabel">
              Pet.me
            </h5>
            <button
              type="button"
              className="btn-close"
              data-bs-dismiss="offcanvas"
              aria-label="Close"
            ></button>
          </div>
          <div className="offcanvas-body">
            <ul className="navbar-nav justify-content-center flex-grow-1 pe-3">
              <li className="nav-item">
                <a
                  className="nav-link mx-lg-2 active"
                  aria-current="page"
                  href="#"
                >
                  Home
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link mx-lg-2" href="#">
                  Explore
                </a>
              </li>
              <li className="nav-item">
                <a className="nav-link mx-lg-2" href="#">
                  About
                </a>
              </li>
              <li className="nav-item">
                <form class="input-group">
                  <input
                    type="text"
                    placeholder="Search here ..."
                    class="form-control"
                    id="inputGroupFile04"
                  />
                  <button
                    class="btn bg-white "
                    type="button"
                    id="inputGroupFileAddon04"
                  >
                    <FontAwesomeIcon icon={faMagnifyingGlass} />
                  </button>
                </form>
              </li>
              <li className="nav-item">
                <a className="nav-link mx-lg-2 fs-4" href="#">
                  <FontAwesomeIcon
                    icon={faComments}
                    style={{ color: "#8c594d" }}
                  />
                </a>
              </li>
            </ul>
          </div>
        </div>

        <a href="#" className="login-button">
          Login
        </a>
        <button
          className="navbar-toggler pe-0"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasNavbar"
          aria-controls="offcanvasNavbar"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
      </div>
    </nav>
  );
}

export default Header;
