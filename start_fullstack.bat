@echo off
title CropGuard AI - Full-Stack MERN Platform
echo ========================================================
echo       Starting CropGuard AI Full-Stack Platform
echo   (React 18 + Node.js Express + MongoDB + Python ML)
echo ========================================================
echo.
cd /d "%~dp0backend"
start "" http://localhost:5000
echo Serving MERN Application at http://localhost:5000 ...
node server.js
pause
