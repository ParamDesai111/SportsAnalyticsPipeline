import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/powerbi">Power BI Dashboard</Link></li>
                <li><Link to="/seasons">Seasons</Link></li>
                <li><Link to="/teams">Teams</Link></li>
            </ul>
        </nav>
    );
}

export default Navbar;
