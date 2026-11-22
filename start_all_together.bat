@echo off
title CropGuard AI - Complete Multi-Service Stack
echo ========================================================
echo       Starting CropGuard AI Complete Multi-Service Stack
echo       Ports: 5000 (React/Node/MongoDB) ^& 8501 (Streamlit 3D)
echo ========================================================
echo.
echo [1/2] Launching Express Backend ^& React Web App on Port 5000...
start "CropGuard Express Backend" cmd /c "cd /d %~dp0backend && node server.js"

echo [2/2] Launching Streamlit 3D AI Studio on Port 8501...
start "" http://localhost:5000
start "" http://localhost:8501
streamlit run app.py --server.port 8501 --server.headless false --browser.gatherUsageStats false
pause
