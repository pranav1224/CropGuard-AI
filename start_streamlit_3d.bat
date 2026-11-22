@echo off
title CropGuard AI - 3D Streamlit Platform
echo ========================================================
echo       Starting CropGuard AI 3D Streamlit Studio
echo       (OpenCV + WebGL 3D Topography + ReportLab PDF)
echo ========================================================
echo.
cd /d "%~dp0"
start "" http://localhost:8501
streamlit run app.py --server.port 8501 --server.headless false --browser.gatherUsageStats false
pause
