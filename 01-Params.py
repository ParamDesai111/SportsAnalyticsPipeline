# Databricks notebook source
# MAGIC %md
# MAGIC # Parameters for Solution

# COMMAND ----------

# Config.ini Example:
# [BlobStorageAccount]
# connection_string = ""
# access_key = ""

# [AzureSQLAdminLogin]
# username = ""
# password = ""
# database = "SportsAnalyticsPipeline-ADB"
# server_name = "sportsanalyticspipeline-dbs.database.windows.net"

import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return {
        'connection_string': config['BlobStorageAccount']['connection_string'],
        'access_key' : config['BlobStorageAccount']['connection_string'],
        'username': config['AzureSQLAdminLogin']['username'],
        'password': config['AzureSQLAdminLogin']['password'],
        'database': config['AzureSQLAdminLogin']['database'],
        'server_name': config['AzureSQLAdminLogin']['server_name']
    }

config_data = read_config()
connection_string = config_data['connection_string']
access_key = config_data['access_key']
username = config_data['username']
password = config_data['password']
database = config_data['database']
server_name = config_data['server_name']


# COMMAND ----------

# Connection to storage account
connection_string = connection_string
container_land_api_response = "land-api-response"

spark.conf.set(
  "fs.azure.account.key.sportsanalyticsplstg.dfs.core.windows.net",
  access_key
)

#Landing to Raw Stream Params

# Teams with Team Code
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

input_path = "abfss://land-api-response@sportsanalyticsplstg.dfs.core.windows.net/playerdata"
output_path_teams = "abfss://raw-data@sportsanalyticsplstg.dfs.core.windows.net/teams/"
output_path_playerstats = "abfss://raw-data@sportsanalyticsplstg.dfs.core.windows.net/playerstats"
output_path_player = "abfss://raw-data@sportsanalyticsplstg.dfs.core.windows.net/player"



# COMMAND ----------

# Connection to Azure SQL Tables
jdbcHostname = server_name
jdbcDatabase = database
jdbcPort = 1433
jdbcUrl = f"jdbc:sqlserver://{jdbcHostname}:{jdbcPort};database={jdbcDatabase};encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30"

connectionProperties = {
  "user" : "SAPDBAdmin",
  "password" : password,
  "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

