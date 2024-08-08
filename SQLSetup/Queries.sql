SELECT * 
FROM PlayerStatistics AS PLS
JOIN Players AS P ON PLS.playerId = P.playerId
WHERE P.playerName = 'Lebron James';

(SELECT * FROM PlayerStatistics WHERE season < 2024)

SELECT * FROM PlayerStatistics
WHERE playerId = 'doncilu01'
AND season = 2024

SELECT * FROM Players
WHERE playerId = 'yurtsom01'