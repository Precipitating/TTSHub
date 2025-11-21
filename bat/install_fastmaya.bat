@echo off
setlocal

:: Move to the PARENT directory of the BAT file
pushd "%~dp0.."

:: ===== CONFIG =====
set "REPO_URL=git+https://github.com/ysharma3501/FastMaya.git"
set "PYTHON=py -3.10"

echo =========================================
echo Checking for virtual environment...
echo =========================================

if exist "fastmayaVenv" (
    echo Virtual environment already exists. Skipping creation.
) else (
    echo Creating virtual environment with Python 3.10...
    %PYTHON% -m venv fastmayaVenv    

    echo Activating virtual environment...
    call fastmayaVenv\Scripts\activate

    echo =========================================
    echo Installing FastMaya from GitHub...
    echo =========================================

    python -m pip install %REPO_URL%
    pip3 install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cu130

    echo =========================================
    echo Done!
)

popd
