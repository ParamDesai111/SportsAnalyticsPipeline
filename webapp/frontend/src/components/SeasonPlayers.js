import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import './styles/SeasonPlayers.css'; // Assuming you create a corresponding CSS file for styling

function SeasonPlayers() {
    const { season } = useParams();
    const [players, setPlayers] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`/players/season/${season}`)
            .then(res => {
                if (res.headers.get('content-type')?.includes('application/json')) {
                    return res.json();
                } else {
                    return res.text().then(text => { 
                        throw new Error(`Expected JSON, got: ${text}`); 
                    });
                }
            })
            .then(data => {
                // Remove duplicate players based on playerId
                const uniquePlayers = data.reduce((acc, player) => {
                    if (!acc.some(p => p.playerId === player.playerId)) {
                        acc.push(player);
                    }
                    return acc;
                }, []);
                setPlayers(uniquePlayers);
            })
            .catch(error => {
                console.error('Error:', error);
                setError(error.message);
            });
    }, [season]);

    if (error) {
        return <div>Error: {error}</div>;
    }

    if (players.length === 0) return <div>No players found for this season.</div>;

    return (
        <div className="season-players-container">
            <h1>Players for Season {season}</h1>
            <div className="player-cards">
                {players.map(player => (
                    <div key={player.playerId} className="player-card">
                        <Link to={`/player/${player.playerId}`}>
                            <h3 className="player-name">{player.playerName}</h3>
                        </Link>
                        {/* Add more player details if needed */}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default SeasonPlayers;
