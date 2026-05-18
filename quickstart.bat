@echo off
echo ========================================
echo Divine AI Suite - Quick Start
echo ========================================
echo.

REM Check Python
py --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Please install Python 3.8+ and try again.
    pause
    exit /b 1
)

REM Install dependencies if not already installed
echo [1/4] Installing dependencies...
py -m pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b 1
)

REM Run agent check
echo [2/4] Checking project integrity...
py agent.py check
if errorlevel 1 (
    echo [ERROR] Integrity check failed.
    pause
    exit /b 1
)

REM Run all demos
echo [3/4] Running all demos...
py run_all_demos.py
if errorlevel 1 (
    echo [WARNING] Some demos may have failed. Check output above.
)

REM Build docs optionally
REM py agent.py build-docs

echo.
echo [4/4] Done!
echo.
echo Next steps:
echo   - Explore each project folder (1.TES, 2.NBCD, ...)
echo   - Read README_MAIN.md for details
echo   - Edit demo.py to experiment
echo.
pause
