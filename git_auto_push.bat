@echo off
cd /d "%~dp0"
git checkout main
git pull --rebase
git add .
git commit -m "Auto commit on %date% %time%"
git push
pause
