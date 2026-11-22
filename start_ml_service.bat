@echo off
title CropGuard - Python ML Microservice
echo ========================================================
echo   Starting CropGuard FastAPI / PyTorch Inference Server
echo ========================================================
cd /d "%~dp0ml_service"
python main.py
pause
