SELECT * 
FROM PlayerStatistics AS PLS
JOIN Players AS P ON PLS.playerId = P.playerId
WHERE P.playerName = 'Seth Curry';

(SELECT count(*) FROM Players)

SELECT COUNT(DISTINCT playerId) AS distinct_player_count
FROM PlayerStatistics
WHERE season = 2023;

SELECT * FROM Players
WHERE playerId = 'yurtsom01'

SELECT * FROM PlayerStatisticsPredicted;

SELECT * 
FROM PlayerStatisticsPredicted AS PLSP
JOIN Players AS P ON PLSP.playerId = P.playerId
WHERE P.playerName = 'Seth Curry';