@echo off
setlocal enabledelayedexpansion

:: Check if Python is installed
echo Checking if Python is installed...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found. Downloading and installing Python...
    
    :: Download Python installer (version 3.9.9 as an example)
    curl -o python-installer.exe https://www.python.org/ftp/python/3.9.9/python-3.9.9-amd64.exe
    
    :: Install Python silently and add to PATH
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    
    :: Check if Python was installed correctly
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Failed to install Python. Please install it manually.
        exit /b
    )
    
    :: Remove the Python installer
    del python-installer.exe
) else (
    echo Python is already installed.
)

:: Check if pip is installed
echo Checking if pip is installed...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip not found. Installing pip...
    python -m ensurepip --upgrade
) else (
    echo pip is already installed.
)

:: Install project dependencies
echo Installing project dependencies...
pip install selenium

:: Variables for geckodriver
set GECKODRIVER_VERSION=v0.33.0
set GECKODRIVER_URL=https://github.com/mozilla/geckodriver/releases/download/%GECKODRIVER_VERSION%/geckodriver-%GECKODRIVER_VERSION%-win64.zip
set GECKODRIVER_FOLDER=C:\geckodriver
set GECKODRIVER_EXE=%GECKODRIVER_FOLDER%\geckodriver.exe

:: Check if geckodriver is already installed
if exist "%GECKODRIVER_EXE%" (
    echo Geckodriver is already installed in %GECKODRIVER_FOLDER%.
) else (
    echo Geckodriver not found. Starting download...

    :: Download geckodriver
    echo Downloading geckodriver version %GECKODRIVER_VERSION%...
    curl -L -o geckodriver.zip %GECKODRIVER_URL%

    :: Create the folder for geckodriver if it does not exist
    if not exist "%GECKODRIVER_FOLDER%" mkdir "%GECKODRIVER_FOLDER%"

    :: Extract geckodriver
    echo Extracting geckodriver...
    powershell -command "Expand-Archive -Path geckodriver.zip -DestinationPath %GECKODRIVER_FOLDER%"

    :: Delete the zip file after extraction
    del geckodriver.zip

    echo Geckodriver installed successfully in %GECKODRIVER_FOLDER%.
)

:: Check if geckodriver is in the PATH
echo Checking if geckodriver is in the PATH...
for %%x in ("%PATH:;=";"%") do (
    if /i "%%~x"=="%GECKODRIVER_FOLDER%" (
        set FOUND_GECKO=1
    )
)

if defined FOUND_GECKO (
    echo Geckodriver is already in the PATH.
) else (
    echo Geckodriver is not in the PATH. Adding to PATH...
    setx PATH "%PATH%;%GECKODRIVER_FOLDER%"
    echo Geckodriver has been added to the PATH.
)

:: Check if Python is in the PATH
echo Checking if Python is in the PATH...
for %%x in ("%PATH:;=";"%") do (
    if /i "%%~x"=="%ProgramFiles%\Python39" (
        set FOUND_PYTHON=1
    )
)

if defined FOUND_PYTHON (
    echo Python is already in the PATH.
) else (
    echo Python is not in the PATH. Adding to PATH...
    setx PATH "%PATH%;%ProgramFiles%\Python39"
    echo Python has been added to the PATH.
)

echo All dependencies have been installed successfully.
pause
