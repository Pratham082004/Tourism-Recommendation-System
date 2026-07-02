import { Link, NavLink } from "react-router-dom";
import "./Navbar.css";

function Navbar(){
    return(
        <header className="navbar">
            <div className="container navbar-container">

                <Link to="/" className="logo">
                    Tourism Recommendation System
                </Link>

                <nav>
                    <ul className="nav-links">
                        <li>
                            <NavLink to="/">Home</NavLink>
                        </li>

                        <li>
                            <NavLink to="/recommendation">
                                Recommendation
                            </NavLink>
                        </li>

                        <li>
                            <NavLink to="/about">
                                About
                            </NavLink>
                        </li>
                    </ul>
                </nav>

            </div>
        </header>
    );
}

export default Navbar;