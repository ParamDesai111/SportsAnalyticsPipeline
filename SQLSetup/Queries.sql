SELECT * 
FROM PlayerStatistics AS PLS
JOIN Players AS P ON PLS.playerId = P.playerId
WHERE P.playerName = 'Luka Doncic';
