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
player_stats_pd = player_stats_df.toPandas()

# COMMAND ----------

# MAGIC %md
# MAGIC Prepare the Data

# COMMAND ----------

# Handle missing values
player_stats_pd.fillna(0, inplace=True)

# Create lag features
player_stats_pd['points_lag_1'] = player_stats_pd.groupby('playerId')['points'].shift(1)
player_stats_pd['points_lag_2'] = player_stats_pd.groupby('playerId')['points'].shift(2)
player_stats_pd['points_lag_3'] = player_stats_pd.groupby('playerId')['points'].shift(3)

# Create rolling average features
player_stats_pd['points_rolling_mean_5'] = player_stats_pd.groupby('playerId')['points'].transform(lambda x: x.rolling(window=5).mean())
player_stats_pd['assists_rolling_mean_5'] = player_stats_pd.groupby('playerId')['assists'].transform(lambda x: x.rolling(window=5).mean())

# Fill missing values created by lag and rolling operations
player_stats_pd.fillna(0, inplace=True)

# Select features for the model
features = [
    'games', 'minutesPg', 'fieldGoals', 'fieldAttempts', 'fieldPercent',
    'threeFg', 'threeAttempts', 'threePercent', 'twoFg', 'twoAttempts', 'twoPercent',
    'effectFgPercent', 'ft', 'ftAttempts', 'ftPercent', 'offensiveRb', 'defensiveRb',
    'totalRb', 'assists', 'steals', 'blocks', 'turnovers', 'personalFouls', 'points',
    'points_lag_1', 'points_lag_2', 'points_lag_3', 'points_rolling_mean_5', 'assists_rolling_mean_5'
]

# Prepare the target variable
target = 'points'


# COMMAND ----------

# MAGIC %md
# MAGIC Train the Machine Learning Model

# COMMAND ----------

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Split data into features (X) and target (y)
X = player_stats_pd[features]
y = player_stats_pd[target]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"RMSE: {rmse}")


# COMMAND ----------

# MAGIC %md
# MAGIC Predict Future Performance

# COMMAND ----------

# Function to predict future performance
def predict_future_performance(model, data, seasons):
    predictions = []
    for season in seasons:
        # Prepare data for the next season prediction
        data['season'] = season
        future_data = data.copy()

        # Make predictions
        future_data['predicted_points'] = model.predict(future_data[features])
        
        # Store predictions
        predictions.append(future_data[['playerId', 'season', 'predicted_points']])
        
        # Use predicted data for the next season's prediction
        data = future_data
    
    return pd.concat(predictions)

# Prepare initial data for 2024 prediction
initial_data = player_stats_pd[player_stats_pd['season'] == 2023].copy()

# Predict for 2024, 2025, and 2026
future_predictions = predict_future_performance(model, initial_data, [2024, 2025, 2026])


# COMMAND ----------

# Display the predictions for all years and any player ID
print(future_predictions)

# To filter predictions for a specific player, e.g., playerId = 'some_player_id'
player_id = 'doncilu01'
player_predictions = future_predictions[future_predictions['playerId'] == player_id]
print(player_predictions)


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

