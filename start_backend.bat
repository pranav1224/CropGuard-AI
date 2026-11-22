@echo off
title CropGuard - Full Stack MERN Server
echo ========================================================
echo   Starting CropGuard Node.js + Express + React Server
echo ========================================================
cd /d "%~dp0backend"
start "" http://localhost:5000
echo Serving API and React Frontend at http://localhost:5000...
node server.js
pause
