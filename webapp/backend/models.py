# webapp/backend/models.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import engine, Base

Base = declarative_base()

class Player(Base):
    __tablename__ = "Players"
    
    playerId = Column(String(1000), primary_key=True)
    playerName = Column(String(1000))
    position = Column(String(1000))
    age = Column(Integer)

class Team(Base):
    __tablename__ = "Teams"

    teamId = Column(Integer, primary_key=True)
    teamCode = Column(String(1000), unique=True)
    teamName = Column(String(1000), unique=True)

class PlayerStatistics(Base):
    __tablename__ = "PlayerStatistics"

    id = Column(Integer, primary_key=True)
    playerId = Column(String(1000), ForeignKey("Players.playerId"))
    teamCode = Column(String(1000), ForeignKey("Teams.teamCode"))
    season = Column(Integer)
    games = Column(Integer)
    gamesStarted = Column(Integer)
    minutesPg = Column(Float)
    fieldGoals = Column(Integer)
    fieldAttempts = Column(Integer)
    fieldPercent = Column(Float)
    threeFg = Column(Integer)
    threeAttempts = Column(Integer)
    threePercent = Column(Float)
    twoFg = Column(Integer)
    twoAttempts = Column(Integer)
    twoPercent = Column(Float)
    effectFgPercent = Column(Float)
    ft = Column(Integer)
    ftAttempts = Column(Integer)
    ftPercent = Column(Float)
    offensiveRb = Column(Integer)
    defensiveRb = Column(Integer)
    totalRb = Column(Integer)
    assists = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)
    turnovers = Column(Integer)
    personalFouls = Column(Integer)
    points = Column(Integer)

class PlayerStatisticsPredicted(Base):
    __tablename__ = "PlayerStatisticsPredicted"

    playerId = Column(String(1000), ForeignKey("Players.playerId"))
    season = Column(Integer)
    predicted_fieldGoals = Column(Float)
    predicted_fieldAttempts = Column(Float)
    predicted_fieldPercent = Column(Float)
    predicted_threeFg = Column(Float)
    predicted_threeAttempts = Column(Float)
    predicted_threePercent = Column(Float)
    predicted_twoFg = Column(Float)
    predicted_twoAttempts = Column(Float)
    predicted_twoPercent = Column(Float)
    predicted_effectFgPercent = Column(Float)
    predicted_ft = Column(Float)
    predicted_ftAttempts = Column(Float)
    predicted_ftPercent = Column(Float)
    predicted_offensiveRb = Column(Float)
    predicted_defensiveRb = Column(Float)
    predicted_totalRb = Column(Float)
    predicted_assists = Column(Float)
    predicted_steals = Column(Float)
    predicted_blocks = Column(Float)
    predicted_turnovers = Column(Float)
    predicted_personalFouls = Column(Float)
    predicted_points = Column(Float)

# Create all tables
Base.metadata.create_all(bind=engine)
