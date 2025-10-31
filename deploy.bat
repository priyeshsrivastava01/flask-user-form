@echo off
echo Starting Railway deployment...

echo Step 1: Login to Railway
railway login

echo Step 2: Initialize Railway project
railway init

echo Step 3: Set environment variables
railway variables set DB_SERVER=%DB_SERVER%
railway variables set DB_NAME="Practice DB"
railway variables set DB_USERNAME=%DB_USERNAME%
railway variables set DB_PASSWORD=%DB_PASSWORD%
railway variables set SECRET_KEY=flask-prod-secret-2024
railway variables set FLASK_DEBUG=false

echo Step 4: Deploy application
railway up

echo Deployment complete!
echo Your app will be available at the URL shown above.
pause