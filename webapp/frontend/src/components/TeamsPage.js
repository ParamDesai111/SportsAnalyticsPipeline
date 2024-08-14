// webapp/frontend/src/components/TeamsPage.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function TeamsPage() {
    const [teams, setTeams] = useState([]);

    useEffect(() => {
        fetch('/teams')
            .then(res => res.json())
            .then(data => setTeams(data));
    }, []);

    return (
        <div>
            <h1>All Teams</h1>
            <ul>
                {teams.map(team => (
                    <li key={team.teamCode}>
                        <Link to={`/team/${team.teamCode}`}>{team.teamName}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TeamsPage;
