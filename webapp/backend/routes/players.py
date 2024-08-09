# webapp/backend/routes/players.py

from flask import Blueprint, jsonify
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Player, PlayerStatistics, PlayerStatisticsPredicted

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
        "statistics": [{"season": stat.season, "points": stat.points, "assists": stat.assists} for stat in player_stats],
        "predictions": [{"season": pred.season, "predicted_points": pred.predicted_points} for pred in player_predictions]
    })

@players.route('/players/season/<season>', methods=['GET'])
def get_players_by_season(season):
    db = next(get_db())
    players_stats = db.query(PlayerStatistics).filter(PlayerStatistics.season == season).all()
    players_data = [{"playerId": stat.playerId, "playerName": db.query(Player).filter(Player.playerId == stat.playerId).first().playerName} for stat in players_stats]
    return jsonify(players_data)
