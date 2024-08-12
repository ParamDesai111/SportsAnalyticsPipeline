import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';  // Import useParams from React Router

function PlayerProfile() {
    const { playerId } = useParams();  // Destructure the playerId from useParams
    const [player, setPlayer] = useState(null);
    const [error, setError] = useState(null);  // State for handling errors

    useEffect(() => {
        fetch(`/player/${playerId}`)
            .then(res => {
                // Check if the response is JSON
                if (res.headers.get('content-type')?.includes('application/json')) {
                    return res.json();
                } else {
                    // Handle non-JSON responses
                    return res.text().then(text => { 
                        throw new Error(`Expected JSON, got: ${text}`); 
                    });
                }
            })
            .then(data => setPlayer(data))
            .catch(error => {
                console.error('Error:', error);
                setError(error.message);  // Set the error message
            });
    }, [playerId]);

    if (error) {
        return <div>Error: {error}</div>;  // Display the error message if there's an error
    }

    if (!player) return <div>Loading...</div>;  // Display a loading message while fetching data

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
