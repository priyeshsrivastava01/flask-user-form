@echo off
echo Setting up environment variables for deployment...

set /p DB_SERVER="Enter your computer's public IP address: "
set /p DB_USERNAME="Enter SQL Server username: "
set /p DB_PASSWORD="Enter SQL Server password: "

echo.
echo Environment variables set:
echo DB_SERVER=%DB_SERVER%
echo DB_USERNAME=%DB_USERNAME%
echo DB_PASSWORD=[HIDDEN]
echo.

call deploy.bat