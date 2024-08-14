import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import PlayerProfile from './components/PlayerProfile';
import SeasonPlayers from './components/SeasonPlayers';
import PowerBIDashboard from './components/PowerBIDashboard';
import SeasonsPage from './components/SeasonsPage';
import TeamsPage from './components/TeamsPage';
import TeamDetailPage from './components/TeamDetailPage';

function App() {
    return (
        <Router>
            <div>
                <Navbar />
                <Routes>
                    <Route path="/" element={<div>Home Page</div>} />
                    <Route path="/player/:playerId" element={<PlayerProfile />} />
                    <Route path="/players/season/:season" element={<SeasonPlayers />} />
                    <Route path="/powerbi" element={<PowerBIDashboard />} />
                    <Route path="/seasons" element={<SeasonsPage />} />
                    <Route path="/teams" element={<TeamsPage />} />
                    <Route path="/team/:teamCode" element={<TeamDetailPage />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
