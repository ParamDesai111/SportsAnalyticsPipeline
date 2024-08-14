// webapp/frontend/src/components/TeamDetailPage.js
import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';

function TeamDetailPage() {
    const { teamCode } = useParams();
    const [team, setTeam] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`/team/${teamCode}`)
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
                const groupedPlayers = data.players.reduce((acc, player) => {
                    if (!acc[player.playerId]) {
                        acc[player.playerId] = {
                            playerName: player.playerName,
                            seasons: []
                        };
                    }
                    acc[player.playerId].seasons.push({
                        season: player.season,
                        points: player.points,
                        assists: player.assists
                    });
                    return acc;
                }, {});
                setTeam({
                    ...data,
                    players: Object.entries(groupedPlayers).map(([playerId, playerData]) => ({
                        playerId,
                        playerName: playerData.playerName,
                        seasons: playerData.seasons
                    }))
                });
            })
            .catch(error => {
                console.error('Error:', error);
                setError(error.message);
            });
    }, [teamCode]);

    if (error) {
        return <div>Error: {error}</div>;
    }

    if (!team) return <div>Loading...</div>;

    return (
        <div>
            <h1>{team.teamName}</h1>
            <h2>Players:</h2>
            <ul>
                {team.players.map(player => (
                    <li key={player.playerId}>
                        <Link to={`/player/${player.playerId}`}>
                            <div>Player Name: {player.playerName}</div>
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TeamDetailPage;
