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
                    <li key={stat.season}>
                        <div>Season: {stat.season}</div>
                        <div>Games: {stat.games}</div>
                        <div>Games Started: {stat.gamesStarted}</div>
                        <div>Minutes per Game: {stat.minutesPg}</div>
                        <div>Field Goals: {stat.fieldGoals}</div>
                        <div>Field Attempts: {stat.fieldAttempts}</div>
                        <div>Field Percent: {stat.fieldPercent}</div>
                        <div>Three FG: {stat.threeFg}</div>
                        <div>Three Attempts: {stat.threeAttempts}</div>
                        <div>Three Percent: {stat.threePercent}</div>
                        <div>Two FG: {stat.twoFg}</div>
                        <div>Two Attempts: {stat.twoAttempts}</div>
                        <div>Two Percent: {stat.twoPercent}</div>
                        <div>Effective FG Percent: {stat.effectFgPercent}</div>
                        <div>Free Throws: {stat.ft}</div>
                        <div>Free Throw Attempts: {stat.ftAttempts}</div>
                        <div>Free Throw Percent: {stat.ftPercent}</div>
                        <div>Offensive Rebounds: {stat.offensiveRb}</div>
                        <div>Defensive Rebounds: {stat.defensiveRb}</div>
                        <div>Total Rebounds: {stat.totalRb}</div>
                        <div>Assists: {stat.assists}</div>
                        <div>Steals: {stat.steals}</div>
                        <div>Blocks: {stat.blocks}</div>
                        <div>Turnovers: {stat.turnovers}</div>
                        <div>Personal Fouls: {stat.personalFouls}</div>
                        <div>Points: {stat.points}</div>
                    </li>
                ))}
            </ul>
            <h4>Predictions:</h4>
            <ul>
                {player.predictions.map(pred => (
                    <li key={pred.season}>
                        <div>Season: {pred.season}</div>
                        <div>Predicted Field Goals: {pred.predicted_fieldGoals}</div>
                        <div>Predicted Field Attempts: {pred.predicted_fieldAttempts}</div>
                        <div>Predicted Field Percent: {pred.predicted_fieldPercent}</div>
                        <div>Predicted Three FG: {pred.predicted_threeFg}</div>
                        <div>Predicted Three Attempts: {pred.predicted_threeAttempts}</div>
                        <div>Predicted Three Percent: {pred.predicted_threePercent}</div>
                        <div>Predicted Two FG: {pred.predicted_twoFg}</div>
                        <div>Predicted Two Attempts: {pred.predicted_twoAttempts}</div>
                        <div>Predicted Two Percent: {pred.predicted_twoPercent}</div>
                        <div>Predicted Effective FG Percent: {pred.predicted_effectFgPercent}</div>
                        <div>Predicted Free Throws: {pred.predicted_ft}</div>
                        <div>Predicted Free Throw Attempts: {pred.predicted_ftAttempts}</div>
                        <div>Predicted Free Throw Percent: {pred.predicted_ftPercent}</div>
                        <div>Predicted Offensive Rebounds: {pred.predicted_offensiveRb}</div>
                        <div>Predicted Defensive Rebounds: {pred.predicted_defensiveRb}</div>
                        <div>Predicted Total Rebounds: {pred.predicted_totalRb}</div>
                        <div>Predicted Assists: {pred.predicted_assists}</div>
                        <div>Predicted Steals: {pred.predicted_steals}</div>
                        <div>Predicted Blocks: {pred.predicted_blocks}</div>
                        <div>Predicted Turnovers: {pred.predicted_turnovers}</div>
                        <div>Predicted Personal Fouls: {pred.predicted_personalFouls}</div>
                        <div>Predicted Points: {pred.predicted_points}</div>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default PlayerProfile;
