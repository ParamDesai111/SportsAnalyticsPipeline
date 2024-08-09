import React, { useEffect, useState } from 'react';

function PlayerProfile({ match }) {
    const [player, setPlayer] = useState(null);

    useEffect(() => {
        fetch(`/player/${match.params.playerId}`)
            .then(res => res.json())
            .then(data => setPlayer(data));
    }, [match.params.playerId]);

    if (!player) return <div>Loading...</div>;

    return (
        <div>
            <h1>{player.player.playerName}</h1>
            <h2>Position: {player.player.position}</h2>
            <h3>Age: {player.player.age}</h3>
            <h4>Statistics:</h4>
            <ul>
                {player.statistics.map(stat => (
                    <li key={stat.season}>Season: {stat.season}, Points: {stat.points}</li>
                ))}
            </ul>
            <h4>Predictions:</h4>
            <ul>
                {player.predictions.map(pred => (
                    <li key={pred.season}>Season: {pred.season}, Predicted Points: {pred.predicted_points}</li>
                ))}
            </ul>
        </div>
    );
}

export default PlayerProfile;
