# webapp/backend/routes/players.py

from flask import Blueprint, jsonify
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Player, PlayerStatistics, PlayerStatisticsPredicted

players = Blueprint('players', __name__)

@players.route('/players', methods=['GET'])
def get_all_players():
    db = next(get_db())
    players = db.query(Player).all()
    return jsonify([{"playerId": player.playerId, "playerName": player.playerName} for player in players])

@players.route('/player/<playerId>', methods=['GET'])
def get_player_profile(playerId):
    db = next(get_db())
    player = db.query(Player).filter(Player.playerId == playerId).first()
    if not player:
        return jsonify({"error": "Player not found"}), 404

    player_stats = db.query(PlayerStatistics).filter(PlayerStatistics.playerId == playerId).all()
    player_predictions = db.query(PlayerStatisticsPredicted).filter(PlayerStatisticsPredicted.playerId == playerId).all()

    return jsonify({
        "player": {
            "playerId": player.playerId,
            "playerName": player.playerName,
            "position": player.position,
            "age": player.age
        },
        "statistics": [{
            "season": stat.season,
            "games": stat.games,
            "gamesStarted": stat.gamesStarted,
            "minutesPg": stat.minutesPg,
            "fieldGoals": stat.fieldGoals,
            "fieldAttempts": stat.fieldAttempts,
            "fieldPercent": stat.fieldPercent,
            "threeFg": stat.threeFg,
            "threeAttempts": stat.threeAttempts,
            "threePercent": stat.threePercent,
            "twoFg": stat.twoFg,
            "twoAttempts": stat.twoAttempts,
            "twoPercent": stat.twoPercent,
            "effectFgPercent": stat.effectFgPercent,
            "ft": stat.ft,
            "ftAttempts": stat.ftAttempts,
            "ftPercent": stat.ftPercent,
            "offensiveRb": stat.offensiveRb,
            "defensiveRb": stat.defensiveRb,
            "totalRb": stat.totalRb,
            "assists": stat.assists,
            "steals": stat.steals,
            "blocks": stat.blocks,
            "turnovers": stat.turnovers,
            "personalFouls": stat.personalFouls,
            "points": stat.points
        } for stat in player_stats
        ],
        "predictions": [
            {
                "season": pred.season,
                "predicted_fieldGoals": pred.predicted_fieldGoals,
                "predicted_fieldAttempts": pred.predicted_fieldAttempts,
                "predicted_fieldPercent": pred.predicted_fieldPercent,
                "predicted_threeFg": pred.predicted_threeFg,
                "predicted_threeAttempts": pred.predicted_threeAttempts,
                "predicted_threePercent": pred.predicted_threePercent,
                "predicted_twoFg": pred.predicted_twoFg,
                "predicted_twoAttempts": pred.predicted_twoAttempts,
                "predicted_twoPercent": pred.predicted_twoPercent,
                "predicted_effectFgPercent": pred.predicted_effectFgPercent,
                "predicted_ft": pred.predicted_ft,
                "predicted_ftAttempts": pred.predicted_ftAttempts,
                "predicted_ftPercent": pred.predicted_ftPercent,
                "predicted_offensiveRb": pred.predicted_offensiveRb,
                "predicted_defensiveRb": pred.predicted_defensiveRb,
                "predicted_totalRb": pred.predicted_totalRb,
                "predicted_assists": pred.predicted_assists,
                "predicted_steals": pred.predicted_steals,
                "predicted_blocks": pred.predicted_blocks,
                "predicted_turnovers": pred.predicted_turnovers,
                "predicted_personalFouls": pred.predicted_personalFouls,
                "predicted_points": pred.predicted_points
            } for pred in player_predictions
]    })

@players.route('/players/season/<season>', methods=['GET'])
def get_players_by_season(season):
    db = next(get_db())
    players_stats = db.query(PlayerStatistics).filter(PlayerStatistics.season == season).all()
    players_data = [{"playerId": stat.playerId, "playerName": db.query(Player).filter(Player.playerId == stat.playerId).first().playerName} for stat in players_stats]
    return jsonify(players_data)
