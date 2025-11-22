@echo off
setlocal

pushd "%~dp0.."

:: ===== CONFIG =====
set "REPO_URL=git+https://github.com/Precipitating/FastNeuTTS"
set "PYTHON=py -3.10"
set "VENV_DIR=fastneuttsVenv"

echo =========================================
echo Checking for virtual environment...
echo =========================================

if exist "%VENV_DIR%" (
    echo Virtual environment already exists. Skipping creation.
    echo Activating existing virtual environment...
    call "%VENV_DIR%\Scripts\activate"
) else (
    echo Creating virtual environment with Python 3.10...
    %PYTHON% -m venv "%VENV_DIR%"
    echo Activating new virtual environment...
    call "%VENV_DIR%\Scripts\activate"

    :: Check if activation failed
    if not defined VIRTUAL_ENV (
        echo ERROR: Failed to activate the virtual environment. Aborting.
        popd
        exit /b 1
    )

    echo =========================================
    echo Installing dependencies...
    echo =========================================

    python -m pip install --upgrade pip
    python -m pip install %REPO_URL%
    python -m pip install soundfile
    start /wait winget install -e --id eSpeak-NG.eSpeak-NG
    python -m pip install hf_xet
    python -m pip install torchao==0.13.0

    echo =========================================
    echo NeuTTS Installation Done!
    echo Installing PyTorch (SET MANUALLY TO YOUR COMPATIBLE VERSION)
)

echo =========================================
echo =========================================

popd
endlocal
