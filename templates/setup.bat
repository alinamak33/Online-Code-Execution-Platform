@echo off
echo ==== Project Setup (Windows) ====

:: 1) Python check
where python >nul 2>&1
if %errorlevel% neq 0 (
  echo Python not found. Please install Python 3 and re-run.
  pause
  exit /b 1
)
python --version

:: Create virtualenv
set VENV_DIR=.venv
if not exist "%VENV_DIR%\" (
  echo Creating virtualenv...
  python -m venv %VENV_DIR%
)

call "%VENV_DIR%\Scripts\activate.bat"
echo Virtualenv activated.

pip install --upgrade pip setuptools wheel
if exist "requirements.txt" (
  echo Installing Python packages...
  pip install -r requirements.txt
) else (
  echo requirements.txt not found. Skipping.
)

:: Node/npm
where npm >nul 2>&1
if %errorlevel% equ 0 (
  npm --version
  if exist "package.json" (
    echo Installing npm packages...
    npm install
  ) else (
    echo package.json not found. Skipping npm install.
  )
) else (
  echo npm not found. Install Node.js from https://nodejs.org/ and re-run.
)

:: PHP & Composer
where php >nul 2>&1
if %errorlevel% equ 0 (
  php -v
  where composer >nul 2>&1
  if %errorlevel% equ 0 (
    composer --version
    if exist "composer.json" (
      composer install --no-interaction
    )
  ) else (
    echo Composer not found. Download and install Composer for Windows: https://getcomposer.org/download/
  )
) else (
  echo PHP not found. Skipping Composer.
)

echo.
echo Setup finished.
pause
