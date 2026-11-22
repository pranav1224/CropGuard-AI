@echo off
title CropGuard AI - Agricultural Diagnostics & Yield Booster
echo =====================================================================
echo                Starting CropGuard AI Application
echo   Crop Disease Detection, Fertilizer Advisor & Yield Maximization
echo =====================================================================
echo.
streamlit run app.py --server.port 8501 --server.headless false --browser.gatherUsageStats false
pause
