# Databricks notebook source
# MAGIC %run ./01-Params

# COMMAND ----------

# MAGIC %md
# MAGIC Connect to Azure SQL Tables

# COMMAND ----------

# Connection to Azure SQL Tables
jdbcHostname = "sportsanalyticspipeline-dbs.database.windows.net"
jdbcDatabase = "SportsAnalyticsPipeline-ADB"
jdbcPort = 1433
jdbcUsername = "SAPDBAdmin"
jdbcPassword = "sqladminParam!"
jdbcUrl = f"jdbc:sqlserver://{jdbcHostname}:{jdbcPort};database={jdbcDatabase};user={jdbcUsername};password={jdbcPassword}"

connectionProperties = {
  "user" : "SAPDBAdmin",
  "password" : "sqladminParam!",
  "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}


# COMMAND ----------

# MAGIC %md
# MAGIC Extract Data from Database

# COMMAND ----------

# Read data from Azure SQL Database
query = "(SELECT * FROM PlayerStatistics WHERE season < 2024) AS PlayerStatistics"

player_stats_df = spark.read \
    .format("jdbc") \
    .option("url", jdbcUrl) \
    .option("dbtable", query) \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .load()

# Convert to Pandas DataFrame
df = player_stats_df.toPandas()

# COMMAND ----------

# MAGIC %md
# MAGIC Prepare the Data

# COMMAND ----------

import pandas as pd
from sklearn.impute import SimpleImputer

# Handle missing values
df.fillna(0, inplace=True)

# Create lag features
lag_features = ['points', 'assists', 'steals', 'blocks', 'turnovers', 'personalFouls']
for feature in lag_features:
    df[f'{feature}_lag_1'] = df.groupby('playerId')[feature].shift(1)
    df[f'{feature}_lag_2'] = df.groupby('playerId')[feature].shift(2)
    df[f'{feature}_lag_3'] = df.groupby('playerId')[feature].shift(3)

# Create rolling average features
rolling_features = ['points', 'assists']
for feature in rolling_features:
    df[f'{feature}_rolling_mean_5'] = df.groupby('playerId')[feature].transform(lambda x: x.rolling(window=5).mean())

# Fill missing values created by lag and rolling operations
df.fillna(0, inplace=True)

# Player-specific averages over the previous seasons
player_avg_features = ['points', 'assists', 'steals', 'blocks', 'turnovers', 'personalFouls']
for feature in player_avg_features:
    df[f'{feature}_player_avg'] = df.groupby('playerId')[feature].transform(lambda x: x.expanding().mean().shift(1))

# Interaction features
df['points_assists_interaction'] = df['points'] * df['assists']
df['steals_blocks_interaction'] = df['steals'] * df['blocks']

# Select features for the model
features = [
    'games', 'minutesPg', 'fieldGoals', 'fieldAttempts', 'fieldPercent',
    'threeFg', 'threeAttempts', 'threePercent', 'twoFg', 'twoAttempts', 'twoPercent',
    'effectFgPercent', 'ft', 'ftAttempts', 'ftPercent', 'offensiveRb', 'defensiveRb',
    'totalRb', 'assists', 'steals', 'blocks', 'turnovers', 'personalFouls',
    'points_lag_1', 'points_lag_2', 'points_lag_3', 'points_rolling_mean_5', 'assists_rolling_mean_5',
    'assists_lag_1', 'assists_lag_2', 'assists_lag_3', 'steals_lag_1', 'steals_lag_2', 'steals_lag_3',
    'blocks_lag_1', 'blocks_lag_2', 'blocks_lag_3', 'turnovers_lag_1', 'turnovers_lag_2', 'turnovers_lag_3',
    'personalFouls_lag_1', 'personalFouls_lag_2', 'personalFouls_lag_3', 'points_player_avg', 'assists_player_avg',
    'steals_player_avg', 'blocks_player_avg', 'turnovers_player_avg', 'personalFouls_player_avg',
    'points_assists_interaction', 'steals_blocks_interaction'
]

# Prepare the target variables
targets = [
    'fieldGoals', 'fieldAttempts', 'fieldPercent',
    'threeFg', 'threeAttempts', 'threePercent', 'twoFg', 'twoAttempts', 'twoPercent',
    'effectFgPercent', 'ft', 'ftAttempts', 'ftPercent', 'offensiveRb', 'defensiveRb',
    'totalRb', 'assists', 'steals', 'blocks', 'turnovers', 'personalFouls', 'points'
]

# Initialize the imputer
imputer = SimpleImputer(strategy='mean')

# COMMAND ----------

# MAGIC %md
# MAGIC Train the Machine Learning Model

# COMMAND ----------

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Train and evaluate models for each target variable
models = {}
for target in targets:
    X = df[features]
    y = df[target]

    # Impute missing values
    X = imputer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    models[target] = model
    
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    print(f"{target} RMSE: {rmse}")

# Prepare data for the 2024 season prediction
future_data = df[df['season'] == 2023].copy()
future_data['season'] = 2024

# Impute missing values for future data
future_data_features = imputer.transform(future_data[features])

# Make predictions for each target variable
for target in targets:
    future_data[f'predicted_{target}'] = models[target].predict(future_data_features)

# Prepare data for insertion
predictions = future_data[['playerId', 'season'] + [f'predicted_{target}' for target in targets]].copy()


# COMMAND ----------

# MAGIC %md
# MAGIC Predict Future Performance

# COMMAND ----------

# Prepare data for the 2024 season prediction
future_data = df[df['season'] == 2023].copy()
future_data['season'] = 2024

# Impute missing values for future data
future_data_features = imputer.transform(future_data[features])

# Make predictions for each target variable
for target in targets:
    future_data[f'predicted_{target}'] = models[target].predict(future_data_features)

# Prepare data for insertion
predictions = future_data[['playerId', 'season'] + [f'predicted_{target}' for target in targets]].copy()


# COMMAND ----------

# Display the predictions for all years and any player ID

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# print(predictions)
# To filter predictions for a specific player, e.g., playerId = 'some_player_id'
player_id = 'doncilu01'
player_predictions = predictions[predictions['playerId'] == player_id]
# print(player_predictions)
display(player_predictions)


# COMMAND ----------

query = "(SELECT * FROM PlayerStatistics WHERE season = 2024 AND playerId = 'doncilu01') AS PlayerStatistics"

playerdf = spark.read \
    .format("jdbc") \
    .option("url", jdbcUrl) \
    .option("dbtable", query) \
    .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
    .load()

# Convert to Pandas DataFrame
doncilu01_pd = playerdf.toPandas()
display(doncilu01_pd)

# COMMAND ----------

# Create a connection to Azure SQL Database
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={jdbcHostname};DATABASE={jdbcDatabase};UID={jdbcUsername};PWD={jdbcPassword}'
)
cursor = conn.cursor()

# Create a new table for storing predictions
cursor.execute("""
    IF OBJECT_ID('PlayerPredictions', 'U') IS NULL
    CREATE TABLE PlayerPredictions (
        playerId VARCHAR(1000),
        season INT,
        predictedPoints FLOAT,
        PRIMARY KEY (playerId, season)
    )
""")
conn.commit()

# Insert predictions into the PlayerPredictions table
for _, row in future_predictions.iterrows():
    cursor.execute("""
        INSERT INTO PlayerPredictions (playerId, season, predictedPoints)
        VALUES (?, ?, ?)
        ON DUPLICATE KEY UPDATE predictedPoints = ?
    """, (row['playerId'], row['season'], row['predicted_points'], row['predicted_points']))
conn.commit()

# Close the connection
conn.close()

