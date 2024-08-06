# Databricks notebook source
# MAGIC %run ./01-Params

# COMMAND ----------

from pyspark.sql.functions import col, monotonically_increasing_id, row_number
from pyspark.sql.window import Window
from pyspark.sql.types import *

# Set Azure Storage account key
spark.conf.set(
  "fs.azure.account.key.sportsanalyticsplstg.dfs.core.windows.net",
  access_key
)

# Read the JSON data with multiline option
df = spark.read.option("multiline", "true").json(input_path)

# Show the schema and some sample rows
df.printSchema()
df.show(5, truncate=False)

# Verify that data is read correctly
print(f"Number of records read: {df.count()}")

teams_data = [(k, v) for k, v in team_dict.items()]
teams_df = spark.createDataFrame(teams_data, ["teamCode", "teamName"])

# Save the Teams DataFrame to Azure Blob Storage
teams_df.write.mode("overwrite").json(output_path_teams)
print("Teams data written to Azure Blob Storage")

# Join the parsed data with the team mappings
parsed_df = df.join(teams_df, df.team == teams_df.teamCode, "inner").drop("team")

# Verify the joined DataFrame
print(f"Number of records after join: {parsed_df.count()}")
parsed_df.show(5, truncate=False)

# Define the schema for PlayerStatistics DataFrame
player_stats_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("playerId", StringType(), True),
    StructField("teamCode", StringType(), True),
    StructField("season", IntegerType(), True),
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
    StructField("points", IntegerType(), True)
])

# Select and cast columns to match the SQL schema for PlayerStatistics
stats_df = parsed_df.select(
    col("id").cast(IntegerType()).alias("id"),
    col("playerId").cast(StringType()).alias("playerId"),
    col("teamCode").cast(StringType()).alias("teamCode"),
    col("season").cast(IntegerType()).alias("season"),
    col("games").cast(IntegerType()).alias("games"),
    col("gamesStarted").cast(IntegerType()).alias("gamesStarted"),
    col("minutesPg").cast(FloatType()).alias("minutesPg"),
    col("fieldGoals").cast(IntegerType()).alias("fieldGoals"),
    col("fieldAttempts").cast(IntegerType()).alias("fieldAttempts"),
    col("fieldPercent").cast(FloatType()).alias("fieldPercent"),
    col("threeFg").cast(IntegerType()).alias("threeFg"),
    col("threeAttempts").cast(IntegerType()).alias("threeAttempts"),
    col("threePercent").cast(FloatType()).alias("threePercent"),
    col("twoFg").cast(IntegerType()).alias("twoFg"),
    col("twoAttempts").cast(IntegerType()).alias("twoAttempts"),
    col("twoPercent").cast(FloatType()).alias("twoPercent"),
    col("effectFgPercent").cast(FloatType()).alias("effectFgPercent"),
    col("ft").cast(IntegerType()).alias("ft"),
    col("ftAttempts").cast(IntegerType()).alias("ftAttempts"),
    col("ftPercent").cast(FloatType()).alias("ftPercent"),
    col("offensiveRb").cast(IntegerType()).alias("offensiveRb"),
    col("defensiveRb").cast(IntegerType()).alias("defensiveRb"),
    col("totalRb").cast(IntegerType()).alias("totalRb"),
    col("assists").cast(IntegerType()).alias("assists"),
    col("steals").cast(IntegerType()).alias("steals"),
    col("blocks").cast(IntegerType()).alias("blocks"),
    col("turnovers").cast(IntegerType()).alias("turnovers"),
    col("personalFouls").cast(IntegerType()).alias("personalFouls"),
    col("points").cast(IntegerType()).alias("points")
)

# Save the PlayerStatistics data to Azure Blob Storage
stats_df.write.mode("overwrite").json(output_path_playerstats)
print("PlayerStatistics data written to Azure Blob Storage")

# Verify the PlayerStatistics DataFrame
print(f"Number of player statistics records: {stats_df.count()}")
stats_df.show(5, truncate=False)

# Create a window specification to get the most recent age for each player
window_spec = Window.partitionBy("playerId").orderBy(col("season").desc())

# Add a row number to each row within the window
ranked_players_df = parsed_df.withColumn("row_number", row_number().over(window_spec))

# Filter to get only the most recent record for each player
most_recent_players_df = ranked_players_df.filter(col("row_number") == 1).drop("row_number")

# Select and cast columns to match the SQL schema for Players
players_df = most_recent_players_df.select(
    col("playerId").cast(StringType()).alias("playerId"),
    col("playerName").cast(StringType()).alias("playerName"),
    col("position").cast(StringType()).alias("position"),
    col("age").cast(IntegerType()).alias("age")
).distinct()

# Save the Players data to Azure Blob Storage
players_df.write.mode("overwrite").json(output_path_player)
print("Players data written to Azure Blob Storage")

# Verify the Players DataFrame
print(f"Number of unique players: {players_df.count()}")
players_df.show(5, truncate=False)

