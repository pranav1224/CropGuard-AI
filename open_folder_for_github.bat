@echo off
echo ========================================================
echo   Opening CropGuard folder for GitHub Upload...
echo ========================================================
echo.
echo Drag and drop these folders and files into GitHub:
echo   1. engine/   (Folder)
echo   2. assets/   (Folder)
echo   3. app.py    (File)
echo   4. requirements.txt (File)
echo.
start "" "https://github.com/pranav1224/CropGuard-AI/upload/main"
explorer /select,"%~dp0app.py"
pause
