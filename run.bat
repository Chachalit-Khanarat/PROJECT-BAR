@echo off

:: Change directory to the Project_Bar folder
cd /d %~dp0

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python to run the game.
    pause
    exit /b
)

:: Check if PyQt5 is installed
pip show PyQt5 >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing PyQt5...
    pip install PyQt5
)

:: Check and install required dependencies
if exist requirements.txt (
    echo Installing required dependencies...
    pip install -r requirements.txt
)

:: Run the game
python game/run.py

pause
