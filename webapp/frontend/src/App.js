import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import PlayerProfile from './components/PlayerProfile';
import SeasonPlayers from './components/SeasonPlayers';
import PowerBIDashboard from './components/PowerBIDashboard';

// Simple Home Component
function Home() {
    return <h1>Welcome to the Sports Analytics Platform</h1>;
}

function App() {
    return (
        <Router>
            <div>
                <Navbar />
                <Routes>
                    <Route path="/" element={<Home />} />  {/* Home route */}
                    <Route path="/player/:playerId" element={<PlayerProfile />} />
                    <Route path="/players/season/:season" element={<SeasonPlayers />} />
                    <Route path="/powerbi" element={<PowerBIDashboard />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
