#!/bin/bash

# Install ODBC Driver for SQL Server on Linux (Ubuntu)
sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
exit
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
sudo apt-get install -y unixodbc-dev


#pip install -r requirements.txt
#chmod +x post_install.sh
#./post_install.sh