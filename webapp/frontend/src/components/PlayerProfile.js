import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
// look into the useParams hook from react-router-dom
function PlayerProfile() {
    const { playerId } = useParams();
    const [player, setPlayer] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`/player/${playerId}`)
            .then(res => {
                if (res.headers.get('content-type')?.includes('application/json')) {
                    return res.json();
                } else {
                    return res.text().then(text => { 
                        throw new Error(`Expected JSON, got: ${text}`); 
                    });
                }
            })
            .then(data => setPlayer(data))
            .catch(error => {
                console.error('Error:', error);
                setError(error.message);
            });
    }, [playerId]);

    if (error) {
        return <div>Error: {error}</div>;
    }

    if (!player) return <div>Loading...</div>;

    // Helper function to round numbers to 2 decimal places
    const roundToTwo = (num) => Math.round(num * 100) / 100;

    return (
        <div>
            <h1>{player.player.playerName}</h1>
            <h2>Position: {player.player.position}</h2>
            <h3>Age: {player.player.age}</h3>
            
            <h4>Statistics:</h4>
            <table border="1" cellPadding="5" cellSpacing="0">
                <thead>
                    <tr>
                        <th>Season</th>
                        <th>Games</th>
                        <th>Games Started</th>
                        <th>Minutes per Game</th>
                        <th>Field Goals</th>
                        <th>Field Attempts</th>
                        <th>Field Percent</th>
                        <th>Three FG</th>
                        <th>Three Attempts</th>
                        <th>Three Percent</th>
                        <th>Two FG</th>
                        <th>Two Attempts</th>
                        <th>Two Percent</th>
                        <th>Effective FG Percent</th>
                        <th>Free Throws</th>
                        <th>Free Throw Attempts</th>
                        <th>Free Throw Percent</th>
                        <th>Offensive Rebounds</th>
                        <th>Defensive Rebounds</th>
                        <th>Total Rebounds</th>
                        <th>Assists</th>
                        <th>Steals</th>
                        <th>Blocks</th>
                        <th>Turnovers</th>
                        <th>Personal Fouls</th>
                        <th>Points</th>
                    </tr>
                </thead>
                <tbody>
                    {player.statistics.map(stat => (
                        <tr key={stat.season}>
                            <td>{stat.season}</td>
                            <td>{stat.games}</td>
                            <td>{stat.gamesStarted}</td>
                            <td>{roundToTwo(stat.minutesPg)}</td>
                            <td>{roundToTwo(stat.fieldGoals)}</td>
                            <td>{roundToTwo(stat.fieldAttempts)}</td>
                            <td>{roundToTwo(stat.fieldPercent)}</td>
                            <td>{roundToTwo(stat.threeFg)}</td>
                            <td>{roundToTwo(stat.threeAttempts)}</td>
                            <td>{roundToTwo(stat.threePercent)}</td>
                            <td>{roundToTwo(stat.twoFg)}</td>
                            <td>{roundToTwo(stat.twoAttempts)}</td>
                            <td>{roundToTwo(stat.twoPercent)}</td>
                            <td>{roundToTwo(stat.effectFgPercent)}</td>
                            <td>{roundToTwo(stat.ft)}</td>
                            <td>{roundToTwo(stat.ftAttempts)}</td>
                            <td>{roundToTwo(stat.ftPercent)}</td>
                            <td>{roundToTwo(stat.offensiveRb)}</td>
                            <td>{roundToTwo(stat.defensiveRb)}</td>
                            <td>{roundToTwo(stat.totalRb)}</td>
                            <td>{roundToTwo(stat.assists)}</td>
                            <td>{roundToTwo(stat.steals)}</td>
                            <td>{roundToTwo(stat.blocks)}</td>
                            <td>{roundToTwo(stat.turnovers)}</td>
                            <td>{roundToTwo(stat.personalFouls)}</td>
                            <td>{roundToTwo(stat.points)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <h4>Predictions:</h4>
            <table border="1" cellPadding="5" cellSpacing="0">
                <thead>
                    <tr>
                        <th>Season</th>
                        <th>Predicted Field Goals</th>
                        <th>Predicted Field Attempts</th>
                        <th>Predicted Field Percent</th>
                        <th>Predicted Three FG</th>
                        <th>Predicted Three Attempts</th>
                        <th>Predicted Three Percent</th>
                        <th>Predicted Two FG</th>
                        <th>Predicted Two Attempts</th>
                        <th>Predicted Two Percent</th>
                        <th>Predicted Effective FG Percent</th>
                        <th>Predicted Free Throws</th>
                        <th>Predicted Free Throw Attempts</th>
                        <th>Predicted Free Throw Percent</th>
                        <th>Predicted Offensive Rebounds</th>
                        <th>Predicted Defensive Rebounds</th>
                        <th>Predicted Total Rebounds</th>
                        <th>Predicted Assists</th>
                        <th>Predicted Steals</th>
                        <th>Predicted Blocks</th>
                        <th>Predicted Turnovers</th>
                        <th>Predicted Personal Fouls</th>
                        <th>Predicted Points</th>
                    </tr>
                </thead>
                <tbody>
                    {player.predictions.map(pred => (
                        <tr key={pred.season}>
                            <td>{pred.season}</td>
                            <td>{roundToTwo(pred.predicted_fieldGoals)}</td>
                            <td>{roundToTwo(pred.predicted_fieldAttempts)}</td>
                            <td>{roundToTwo(pred.predicted_fieldPercent)}</td>
                            <td>{roundToTwo(pred.predicted_threeFg)}</td>
                            <td>{roundToTwo(pred.predicted_threeAttempts)}</td>
                            <td>{roundToTwo(pred.predicted_threePercent)}</td>
                            <td>{roundToTwo(pred.predicted_twoFg)}</td>
                            <td>{roundToTwo(pred.predicted_twoAttempts)}</td>
                            <td>{roundToTwo(pred.predicted_twoPercent)}</td>
                            <td>{roundToTwo(pred.predicted_effectFgPercent)}</td>
                            <td>{roundToTwo(pred.predicted_ft)}</td>
                            <td>{roundToTwo(pred.predicted_ftAttempts)}</td>
                            <td>{roundToTwo(pred.predicted_ftPercent)}</td>
                            <td>{roundToTwo(pred.predicted_offensiveRb)}</td>
                            <td>{roundToTwo(pred.predicted_defensiveRb)}</td>
                            <td>{roundToTwo(pred.predicted_totalRb)}</td>
                            <td>{roundToTwo(pred.predicted_assists)}</td>
                            <td>{roundToTwo(pred.predicted_steals)}</td>
                            <td>{roundToTwo(pred.predicted_blocks)}</td>
                            <td>{roundToTwo(pred.predicted_turnovers)}</td>
                            <td>{roundToTwo(pred.predicted_personalFouls)}</td>
                            <td>{roundToTwo(pred.predicted_points)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default PlayerProfile;
