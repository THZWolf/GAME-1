@echo off
cd /d "%~dp0"
start "NEON FRONTIER" http://localhost:8000
py -m http.server 8000
if errorlevel 1 python -m http.server 8000
pause
