@echo off

:: Change directory to the Project_Bar folder
cd /d %~dp0

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python to proceed.
    pause
    exit /b
)

:: Check and install required dependencies
if exist requirements.txt (
    echo Installing required dependencies...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Failed to install some dependencies. Please check the error messages above.
        pause
        exit /b
    )
    echo All dependencies installed successfully.
) else (
    echo requirements.txt not found. Please ensure it exists in the Project_Bar folder.
    pause
    exit /b
)

pause
