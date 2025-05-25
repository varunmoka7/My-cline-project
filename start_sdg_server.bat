@echo off
echo Starting SDG Dashboard Server on port 8001...
echo.
echo The SDG Dashboard will be available at:
echo http://localhost:8001/sdg_dashboard.html
echo.
echo Press Ctrl+C to stop the server
echo.
cd /d "%~dp0"
python -m http.server 8001
pause
