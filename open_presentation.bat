@echo off
title CropGuard - Presentation Launcher
echo ========================================================
echo   Launching CropGuard Project Presentation
echo ========================================================
echo [1] Opening PowerPoint file (.pptx)...
start "" "%~dp0CropGuard_Project_Presentation.pptx"
echo [2] Opening Interactive Browser Slide Deck (.html)...
start "" "%~dp0presentation.html"
echo.
echo Both the PowerPoint file and the Browser slide deck have been opened!
pause
