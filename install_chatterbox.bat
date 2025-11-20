@echo off
setlocal

:: ===== CONFIG =====
set REPO_URL=https://github.com/petermg/Chatterbox-TTS-Extended
set FOLDER=Chatterbox-TTS-Extended
set PYTHON=python

echo =========================================
echo Checking if repository is already cloned...
echo =========================================

if exist "%FOLDER%" (
    echo Repo folder "%FOLDER%" already exists. Skipping clone.
) else (
    echo Cloning repository...
    git clone %REPO_URL%
    if errorlevel 1 (
        echo Failed to clone repo!
        exit /b 1
    )
)

cd %FOLDER%

echo =========================================
echo Checking for virtual environment...
echo =========================================

if exist ".venv" (
    echo Virtual environment already exists. Skipping creation.
) else (
    echo Creating virtual environment...
    %PYTHON% -m venv .venv
)

echo Activating virtual environment...
call .venv\Scripts\activate

echo =========================================
echo Installing requirements...
echo =========================================

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo =========================================
echo Done!
pause
