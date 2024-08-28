// webapp/frontend/src/components/TeamsPage.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import teamLogos from '../data/teamLogos'; // Import the team logos mapping
import './styles/TeamsPage.css';

function TeamsPage() {
    const [teams, setTeams] = useState([]);

    useEffect(() => {
        fetch('/teams')
            .then(res => res.json())
            .then(data => setTeams(data));
    }, []);

    return (
        <div className="teams-container">
            <h1>All Teams</h1>
            <div className="team-cards">
                {teams.map(team => (
                    <div key={team.teamCode} className="team-card">
                        <Link to={`/team/${team.teamCode}`}>
                            <img 
                                src={teamLogos[team.teamCode]} 
                                alt={`${team.teamName} logo`} 
                                className="team-logo" 
                            />
                            <h3 className="team-name">{team.teamName}</h3>
                        </Link>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default TeamsPage;
