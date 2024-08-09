import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function SeasonPlayers({ match }) {
    const [players, setPlayers] = useState([]);

    useEffect(() => {
        fetch(`/players/season/${match.params.season}`)
            .then(res => res.json())
            .then(data => setPlayers(data));
    }, [match.params.season]);

    return (
        <div>
            <h1>Players for Season {match.params.season}</h1>
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
