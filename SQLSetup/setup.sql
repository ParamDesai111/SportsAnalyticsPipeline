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
