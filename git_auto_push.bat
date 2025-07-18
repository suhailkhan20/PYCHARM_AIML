@echo off
cd /d "%~dp0"

REM Check if there are changes
git diff --quiet && git diff --cached --quiet
IF ERRORLEVEL 1 (
    git add .
    git commit -m "Auto commit on %date% %time%"
)

git pull --rebase
git push

pause