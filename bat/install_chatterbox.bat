@echo off
setlocal

:: Move to the PARENT directory of where the BAT file is located
pushd "%~dp0.."

:: ===== CONFIG =====
set "REPO_URL=https://github.com/petermg/Chatterbox-TTS-Extended"
set "FOLDER=Chatterbox-TTS-Extended"
set "PYTHON=py -3.10"

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
        popd
        exit /b 1
    )
)


echo =========================================
echo Checking for virtual environment...
echo =========================================

if exist "chatterboxVenv" (
    echo Virtual environment already exists. Skipping creation.
) else (
    echo Creating virtual environment...
    %PYTHON% -m venv chatterboxVenv    

    echo Activating virtual environment...
    call chatterboxVenv\Scripts\activate

    echo =========================================
    echo Installing requirements...
    echo =========================================

    python -m pip install -r ChatterboxRequirements.txt

    echo =========================================
    echo Done!
)

popd
