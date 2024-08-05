# Databricks notebook source
# MAGIC %run ./01-Params

# COMMAND ----------

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("InsertTeams").getOrCreate()

# Teams data dictionary
team_dict = {
    "ATL": "Atlanta Hawks",
    "BOS": "Boston Celtics",
    "BRK": "Brooklyn Nets",
    "CHH": "Charlotte Hornets",
    "CHI": "Chicago Bulls",
    "CLE": "Cleveland Cavaliers",
    "DAL": "Dallas Mavericks",
    "DEN": "Denver Nuggets",
    "DET": "Detroit Pistons",
    "GSW": "Golden State Warriors",
    "HOU": "Houston Rockets",
    "IND": "Indiana Pacers",
    "LAC": "Los Angeles Clippers",
    "LAL": "Los Angeles Lakers",
    "MIA": "Miami Heat",
    "MIL": "Milwaukee Bucks",
    "MIN": "Minnesota Timberwolves",
    "NJN": "New Jersey Nets",
    "NYK": "New York Knicks",
    "ORL": "Orlando Magic",
    "PHI": "Philadelphia 76ers",
    "PHO": "Phoenix Suns",
    "POR": "Portland Trail Blazers",
    "SAC": "Sacramento Kings",
    "SAS": "San Antonio Spurs",
    "SEA": "Seattle SuperSonics",
    "TOT": "Various Teams",
    "UTA": "Utah Jazz",
    "WSB": "Washington Bullets",
    "CHA": "Charlotte Bobcats",
    "MEM": "Memphis Grizzlies",
    "VAN": "Vancouver Grizzlies",
    "NOP": "New Orleans Pelicans",
    "NOH": "New Orleans Hornets",
    "OKC": "Oklahoma City Thunder",
    "TOR": "Toronto Raptors",
    "WAS": "Washington Wizards"
}

# Convert team_dict to DataFrame
teams_data = [(k, v) for k, v in team_dict.items()]
teams_df = spark.createDataFrame(teams_data, ["teamCode", "teamName"])

# Define function to upsert teams data
def upsert_teams(df, jdbcUrl, connectionProperties):
    temp_table_name = "temp_teams"
    df.createOrReplaceTempView(temp_table_name)
    upsert_query = f"""
    MERGE INTO Teams AS target
    USING {temp_table_name} AS source
    ON target.teamCode = source.teamCode
    WHEN MATCHED THEN
      UPDATE SET target.teamName = source.teamName
    WHEN NOT MATCHED THEN
      INSERT (teamCode, teamName) VALUES (source.teamCode, source.teamName)
    """
    spark.sql(upsert_query)

# Perform the upsert operation
upsert_teams(teams_df, jdbcUrl, connectionProperties)


# COMMAND ----------

from pyspark.sql.functions import col, from_json
from pyspark.sql.types import *

# Azure SQL Database connection properties
jdbcHostname = "sportsanalyticspipeline-dbs.database.windows.net"
jdbcDatabase = "SportsAnalyticsPipeline-ADB"
jdbcPort = 1433
jdbcUsername = ""
jdbcPassword = ""
jdbcUrl = f"jdbc:sqlserver://{jdbcHostname}:{jdbcPort};database={jdbcDatabase};user={jdbcUsername};password={jdbcPassword}"

connectionProperties = {
  "user" : jdbcUsername,
  "password" : jdbcPassword,
  "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

# Storage Account Configuration Set
spark.conf.set(
  "fs.azure.account.key.sportsanalyticsplstg.dfs.core.windows.net",
  ""
)

# Define the schema for the JSON data
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("playerName", StringType(), True),
    StructField("position", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("games", IntegerType(), True),
    StructField("gamesStarted", IntegerType(), True),
    StructField("minutesPg", FloatType(), True),
    StructField("fieldGoals", IntegerType(), True),
    StructField("fieldAttempts", IntegerType(), True),
    StructField("fieldPercent", FloatType(), True),
    StructField("threeFg", IntegerType(), True),
    StructField("threeAttempts", IntegerType(), True),
    StructField("threePercent", FloatType(), True),
    StructField("twoFg", IntegerType(), True),
    StructField("twoAttempts", IntegerType(), True),
    StructField("twoPercent", FloatType(), True),
    StructField("effectFgPercent", FloatType(), True),
    StructField("ft", IntegerType(), True),
    StructField("ftAttempts", IntegerType(), True),
    StructField("ftPercent", FloatType(), True),
    StructField("offensiveRb", IntegerType(), True),
    StructField("defensiveRb", IntegerType(), True),
    StructField("totalRb", IntegerType(), True),
    StructField("assists", IntegerType(), True),
    StructField("steals", IntegerType(), True),
    StructField("blocks", IntegerType(), True),
    StructField("turnovers", IntegerType(), True),
    StructField("personalFouls", IntegerType(), True),
    StructField("points", IntegerType(), True),
    StructField("team", StringType(), True),
    StructField("season", IntegerType(), True),
    StructField("playerId", StringType(), True)
])

raw_df = (spark.readStream.format("cloudFiles")
          .option("cloudFiles.format", "json")
          .option("cloudFiles.schemaLocation", schema_checkpoint)
          .option("cloudFiles.checkpointLocation", file_checkpoint)
          .schema(schema)
          .load(seasonal_data_players_location))

# Parse the JSON data and apply schema
parsed_df = raw_df

# Create a streaming DataFrame for teams
team_dict = {
    "ATL": "Atlanta Hawks",
    "BOS": "Boston Celtics",
    "BRK": "Brooklyn Nets",
    "CHH": "Charlotte Hornets",
    "CHI": "Chicago Bulls",
    "CLE": "Cleveland Cavaliers",
    "DAL": "Dallas Mavericks",
    "DEN": "Denver Nuggets",
    "DET": "Detroit Pistons",
    "GSW": "Golden State Warriors",
    "HOU": "Houston Rockets",
    "IND": "Indiana Pacers",
    "LAC": "Los Angeles Clippers",
    "LAL": "Los Angeles Lakers",
    "MIA": "Miami Heat",
    "MIL": "Milwaukee Bucks",
    "MIN": "Minnesota Timberwolves",
    "NJN": "New Jersey Nets",
    "NYK": "New York Knicks",
    "ORL": "Orlando Magic",
    "PHI": "Philadelphia 76ers",
    "PHO": "Phoenix Suns",
    "POR": "Portland Trail Blazers",
    "SAC": "Sacramento Kings",
    "SAS": "San Antonio Spurs",
    "SEA": "Seattle SuperSonics",
    "TOT": "Various Teams",
    "UTA": "Utah Jazz",
    "WSB": "Washington Bullets",
    "CHA": "Charlotte Bobcats",
    "MEM": "Memphis Grizzlies",
    "VAN": "Vancouver Grizzlies",
    "NOP": "New Orleans Pelicans",
    "NOH": "New Orleans Hornets",
    "OKC": "Oklahoma City Thunder",
    "TOR": "Toronto Raptors",
    "WAS": "Washington Wizards"
}

teams_data = [(k, v) for k, v in team_dict.items()]
teams_df = spark.createDataFrame(teams_data, ["teamCode", "teamName"])

# Write the Teams DataFrame to Azure SQL (upsert logic)
def upsert_teams(batch_df, batch_id):
    temp_table_name = "temp_teams"
    batch_df.createOrReplaceTempView(temp_table_name)
    query = f"""
    MERGE INTO Teams AS target
    USING {temp_table_name} AS source
    ON target.teamCode = source.teamCode
    WHEN MATCHED THEN
      UPDATE SET target.teamName = source.teamName
    WHEN NOT MATCHED THEN
      INSERT (teamCode, teamName) VALUES (source.teamCode, source.teamName)
    """
    batch_df.sparkSession.sql(query)

# Read the Teams table to get team ID mappings
team_id_mapping = spark.read.jdbc(url=jdbcUrl, table="Teams", properties=connectionProperties).select("teamCode", "teamId")

# Join the parsed data with the team ID mappings
parsed_df = parsed_df.join(team_id_mapping, parsed_df.team == team_id_mapping.teamCode).drop("team")

# Insert Players data into Players table
players_df = parsed_df.select("playerId", "playerName", "position", "age").distinct()
players_df.writeStream.format("jdbc").option("url", jdbcUrl).option("dbtable", "Players").option("checkpointLocation", "/mnt/checkpoints/players").option("user", jdbcUsername).option("password", jdbcPassword).start()

# Insert PlayerStatistics data into PlayerStatistics table
stats_df = parsed_df.select(
    "id", "playerId", "teamId", "season", "games", "gamesStarted", "minutesPg", "fieldGoals", "fieldAttempts", 
    "fieldPercent", "threeFg", "threeAttempts", "threePercent", "twoFg", "twoAttempts", "twoPercent", "effectFgPercent", 
    "ft", "ftAttempts", "ftPercent", "offensiveRb", "defensiveRb", "totalRb", "assists", "steals", "blocks", "turnovers", 
    "personalFouls", "points"
)
stats_df.writeStream.format("jdbc").option("url", jdbcUrl).option("dbtable", "PlayerStatistics").option("checkpointLocation", "/mnt/checkpoints/player_statistics").option("user", jdbcUsername).option("password", jdbcPassword).start()

