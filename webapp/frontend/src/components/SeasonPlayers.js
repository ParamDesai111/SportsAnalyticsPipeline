import React, { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';

function SeasonPlayers() {
    const { season } = useParams();  // Destructure the season parameter from useParams
    const [players, setPlayers] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`/players/season/${season}`)
            .then(res => {
                // Check if the response is JSON
                if (res.headers.get('content-type')?.includes('application/json')) {
                    return res.json();  // Parse as JSON
                } else {
                    // If not JSON, handle the error
                    return res.text().then(text => { 
                        throw new Error(`Expected JSON, got: ${text}`); 
                    });
                }
            })
            .then(data => setPlayers(data))
            .catch(error => {
                console.error('Error:', error);
                setError(error.message);  // Set error state
            });
    }, [season]);

    if (error) {
        return <div>Error: {error}</div>;  // Display the error message
    }

    return (
        <div>
            <h1>Players for Season {season}</h1>
            <ul>
                {players.map(player => (
                    <li key={player.playerId}>
                        <Link to={`/player/${player.playerId}`}>{player.playerName}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default SeasonPlayers;
