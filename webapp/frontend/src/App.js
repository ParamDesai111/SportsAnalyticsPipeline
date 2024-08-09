import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import PlayerProfile from './components/PlayerProfile';
import SeasonPlayers from './components/SeasonPlayers';
import PowerBIDashboard from './components/PowerBIDashboard';

function App() {
    return (
        <Router>
            <div>
                <Navbar />
                <Route path="/player/:playerId" component={PlayerProfile} />
                <Route path="/players/season/:season" component={SeasonPlayers} />
                <Route path="/powerbi" component={PowerBIDashboard} />
            </div>
        </Router>
    );
}

export default App;
