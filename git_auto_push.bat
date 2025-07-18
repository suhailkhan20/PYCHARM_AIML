@echo off
cd /d "%~dp0"
git checkout main
git pull origin main
git add .
git commit -m "Auto commit on %date% %time%"
git push origin main
pause
