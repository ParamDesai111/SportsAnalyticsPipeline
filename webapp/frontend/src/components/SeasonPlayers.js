import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';

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
