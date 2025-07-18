@echo off
cd /d "%~dp0"

REM Stage and commit changes if needed
git diff --quiet && git diff --cached --quiet
IF ERRORLEVEL 1 (
    git add .
    git commit -m "Auto commit on %date% %time%"
)

REM Check if upstream is set
git rev-parse --abbrev-ref --symbolic-full-name @{u} >nul 2>&1
IF ERRORLEVEL 1 (
    echo Setting upstream branch to origin/main...
    git branch --set-upstream-to=origin/main main
)

REM Pull latest changes and rebase
git pull --rebase

REM Push changes
git push

pause