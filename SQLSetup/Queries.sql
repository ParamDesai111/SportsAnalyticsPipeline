SELECT * 
FROM PlayerStatistics AS PLS
JOIN Players AS P ON PLS.playerId = P.playerId
WHERE P.playerName = 'Luka Doncic';

(SELECT * FROM PlayerStatistics WHERE season < 2024)

SELECT points, season FROM PlayerStatistics
WHERE playerId = 'doncilu01'

SELECT * FROM Players
WHERE playerId = 'yurtsom01'