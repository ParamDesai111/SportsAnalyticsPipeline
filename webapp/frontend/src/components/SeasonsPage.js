// webapp/frontend/src/components/SeasonsPage.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './styles/SeasonsPage.css'; // Assuming you create a corresponding CSS file for styling

function SeasonsPage() {
    const [seasons, setSeasons] = useState([]);

    useEffect(() => {
        // Assuming the seasons data is from 1993 to 2024
        const allSeasons = [];
        for (let year = 1993; year <= 2024; year++) {
            allSeasons.push(year);
        }
        setSeasons(allSeasons);
    }, []);

    return (
        <div className="seasons-container">
            <h1>All Seasons</h1>
            <div className="season-cards">
                {seasons.map(season => (
                    <div key={season} className="season-card">
                        <Link to={`/players/season/${season}`}>
                            <h3 className="season-name">Season {season}</h3>
                        </Link>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default SeasonsPage;
