// webapp/frontend/src/components/SeasonsPage.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

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
        <div>
            <h1>All Seasons</h1>
            <ul>
                {seasons.map(season => (
                    <li key={season}>
                        <Link to={`/players/season/${season}`}>Season {season}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default SeasonsPage;
