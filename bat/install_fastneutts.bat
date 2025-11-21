@echo off
setlocal

:: Move to the PARENT directory of the BAT file
pushd "%~dp0.."

:: ===== CONFIG =====
set "REPO_URL=git+https://github.com/ysharma3501/FastNeuTTS.git"
set "PYTHON=py -3.11"

echo =========================================
echo Checking for virtual environment...
echo =========================================

if exist "fastneuttsVenv" (
    echo Virtual environment already exists. Skipping creation.
) else (
    echo Creating virtual environment with Python 3.11...
    %PYTHON% -m venv fastneuttsVenv    

    echo Activating virtual environment...
    call fastneuttsVenv\Scripts\activate

    echo =========================================
    echo Installing FastNeutts from GitHub...
    echo =========================================

    python -m pip install %REPO_URL%
    python -m pip install soundfile
    choco install espeak-ng
    pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu128

    echo =========================================
    echo Done!
)

popd
