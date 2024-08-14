# webapp/backend/routes/teams.py

from flask import Blueprint, jsonify
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import Team, PlayerStatistics, Player

teams = Blueprint('teams', __name__)

@teams.route('/teams', methods=['GET'])
def get_all_teams():
    db = next(get_db())
    teams = db.query(Team).all()
    return jsonify([{"teamCode": team.teamCode, "teamName": team.teamName} for team in teams])

@teams.route('/team/<teamCode>', methods=['GET'])
def get_team_detail(teamCode):
    db = next(get_db())
    team = db.query(Team).filter(Team.teamCode == teamCode).first()
    if not team:
        return jsonify({"error": "Team not found"}), 404

    players_stats = db.query(PlayerStatistics).filter(PlayerStatistics.teamCode == teamCode).all()
    players_data = [{
        "playerId": stat.playerId,
        "playerName": db.query(Player).filter(Player.playerId == stat.playerId).first().playerName,
        "season": stat.season,
        "points": stat.points,
        "assists": stat.assists
    } for stat in players_stats]

    return jsonify({
        "teamCode": team.teamCode,
        "teamName": team.teamName,
        "players": players_data
    })

@teams.route('/team/<teamCode>/season/<season>', methods=['GET'])
def get_team_players_by_season(teamCode, season):
    db = next(get_db())
    players_stats = db.query(PlayerStatistics).filter(PlayerStatistics.teamCode == teamCode, PlayerStatistics.season == season).all()
    players_data = [{
        "playerId": stat.playerId,
        "playerName": db.query(Player).filter(Player.playerId == stat.playerId).first().playerName,
        "points": stat.points,
        "assists": stat.assists
    } for stat in players_stats]

    return jsonify({
        "teamCode": teamCode,
        "season": season,
        "players": players_data
    })