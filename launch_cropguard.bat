@echo off
setlocal enabledelayedexpansion
title CropGuard AI - Unified Launch Center
cls

:menu
echo ========================================================================
echo                 CropGuard AI - Precision Agriculture Platform
echo ========================================================================
echo.
echo   [1] Launch 3D Streamlit AI Platform (Port 8501)  [RECOMMENDED]
echo       ^> Computer Vision Pathology, 3D WebGL Topography, Yield AI ^& PDF
echo.
echo   [2] Launch Full-Stack Express ^& React App (Port 5000)
echo       ^> Serves compiled React dashboard + Node.js REST API Gateway
echo.
echo   [3] Open Instant Standalone Dashboard (index.html)
echo       ^> Zero-setup browser dashboard with offline AI engine
echo.
echo   [4] Launch Full Multi-Service Stack (Ports 8501 + 5000)
echo       ^> Starts both Streamlit 3D AI and Express/React servers
echo.
echo   [5] Exit
echo.
echo ========================================================================
set /p choice="Enter choice [1-5]: "

if "%choice%"=="1" goto run_streamlit
if "%choice%"=="2" goto run_express
if "%choice%"=="3" goto run_instant
if "%choice%"=="4" goto run_both
if "%choice%"=="5" exit /b
echo Invalid choice, please try again.
pause
cls
goto menu

:run_streamlit
echo.
echo Starting CropGuard 3D Streamlit Platform on http://localhost:8501...
start "" http://localhost:8501
streamlit run app.py --server.port 8501 --server.headless false --browser.gatherUsageStats false
goto end

:run_express
echo.
echo Starting Express Backend ^& React Web App on http://localhost:5000...
cd /d "%~dp0backend"
start "" http://localhost:5000
node server.js
goto end

:run_instant
echo.
echo Opening standalone CropGuard dashboard in default browser...
start "" "%~dp0index.html"
goto end

:run_both
echo.
echo Starting both services...
start "CropGuard Express Backend" cmd /c "cd /d %~dp0backend && node server.js"
start "" http://localhost:8501
streamlit run app.py --server.port 8501 --server.headless false --browser.gatherUsageStats false
goto end

:end
pause
