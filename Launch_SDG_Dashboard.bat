@echo off
echo ========================================
echo     SD3 - SDG Companies Dashboard
echo ========================================
echo.
echo Starting server and opening dashboard...
echo.

REM Start the server in background
start /B python -m http.server 8001

REM Wait a moment for server to start
timeout /t 3 /nobreak >nul

REM Open the dashboard in default browser
start http://localhost:8001/sdg_dashboard.html

echo.
echo Dashboard opened at: http://localhost:8001/sdg_dashboard.html
echo.
echo Press any key to stop the server and exit...
pause >nul

REM Kill the python server
taskkill /F /IM python.exe 2>nul
echo Server stopped.
