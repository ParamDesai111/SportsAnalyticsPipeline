# Databricks notebook source
# MAGIC %md
# MAGIC # Parameters for Solution

# COMMAND ----------

# Config.ini Example:
# [BlobStorageAccount]
# connection_string = ""

# [AzureSQLAdminLogin]
# username = ""
# password = ""
# database = "SportsAnalyticsPipeline-ADB"
# server_name = "sportsanalyticspipeline-dbs.database.windows.net"


import configparser

import configparser

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return {
        'connection_string': config['BlobStorageAccount']['connection_string'],
        'username': config['AzureSQLAdminLogin']['username'],
        'password': config['AzureSQLAdminLogin']['password'],
        'database': config['AzureSQLAdminLogin']['database'],
        'server_name': config['AzureSQLAdminLogin']['server_name']
    }

config_data = read_config()
connection_string = config_data['connection_string']
username = config_data['username']
password = config_data['password']
database = config_data['database']
server_name = config_data['server_name']


# COMMAND ----------

# Connection to storage account
connection_string = connection_string
container_land_api_response = "land-api-response"

