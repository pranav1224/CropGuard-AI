@echo off
title CropGuard - React Frontend Server
echo ========================================================
echo   Starting CropGuard React 18 + Vite Development Server
echo ========================================================
cd /d "%~dp0frontend"
if not exist "node_modules\" (
    echo Installing React dependencies (this may take a minute on first run)...
    call npm.cmd install
)
echo Starting local Vite dev server at http://localhost:3000...
call npm.cmd run dev
pause
