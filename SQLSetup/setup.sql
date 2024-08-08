CREATE TABLE Players (
    playerId VARCHAR(1000) PRIMARY KEY,
    playerName VARCHAR(1000),
    position VARCHAR(1000),
    age INT
);


CREATE TABLE Teams (
    teamId INT PRIMARY KEY IDENTITY(1,1),
    teamCode VARCHAR(1000) UNIQUE,
    teamName VARCHAR(1000) UNIQUE
);

CREATE TABLE PlayerStatistics (
    id INT PRIMARY KEY,
    playerId VARCHAR(1000),
    teamId INT,
    season INT,
    games INT,
    gamesStarted INT,
    minutesPg FLOAT,
    fieldGoals INT,
    fieldAttempts INT,
    fieldPercent FLOAT,
    threeFg INT,
    threeAttempts INT,
    threePercent FLOAT,
    twoFg INT,
    twoAttempts INT,
    twoPercent FLOAT,
    effectFgPercent FLOAT,
    ft INT,
    ftAttempts INT,
    ftPercent FLOAT,
    offensiveRb INT,
    defensiveRb INT,
    totalRb INT,
    assists INT,
    steals INT,
    blocks INT,
    turnovers INT,
    personalFouls INT,
    points INT
);

CREATE TABLE PlayerStatisticsPredicted (
    playerId VARCHAR(1000),
    season INT,
    predicted_fieldGoals FLOAT,
    predicted_fieldAttempts FLOAT,
    predicted_fieldPercent FLOAT,
    predicted_threeFg FLOAT,
    predicted_threeAttempts FLOAT,
    predicted_threePercent FLOAT,
    predicted_twoFg FLOAT,
    predicted_twoAttempts FLOAT,
    predicted_twoPercent FLOAT,
    predicted_effectFgPercent FLOAT,
    predicted_ft FLOAT,
    predicted_ftAttempts FLOAT,
    predicted_ftPercent FLOAT,
    predicted_offensiveRb FLOAT,
    predicted_defensiveRb FLOAT,
    predicted_totalRb FLOAT,
    predicted_assists FLOAT,
    predicted_steals FLOAT,
    predicted_blocks FLOAT,
    predicted_turnovers FLOAT,
    predicted_personalFouls FLOAT,
    predicted_points FLOAT
);
