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

seasonal_data_players_location = "abfss://land-api-response@sportsanalyticsplstg.dfs.core.windows.net/playerdata"
schema_checkpoint = "abfss://land-api-response@sportsanalyticsplstg.dfs.core.windows.net/schema_playerdata"
file_checkpoint = "abfss://land-api-response@sportsanalyticsplstg.dfs.core.windows.net/file_checkpoint"
file_checkpoint = "abfss://land-api-response@sportsanalyticsplstg.dfs.core.windows.net/file_checkpoint_stats"

# COMMAND ----------

# Connection to Azure SQL Tables
jdbcHostname = server_name
jdbcDatabase = database
jdbcPort = 1433
jdbcUrl = f"jdbc:sqlserver://{jdbcHostname}:{jdbcPort};database={jdbcDatabase};encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30"

connectionProperties = {
  "user" : "SAPDBAdmin",
  "password" : "",
  "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

