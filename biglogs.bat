@echo off

setlocal enabledelayedexpansion

set "SEARCH_DIR=%~1"
set "FILE_SIZE=%~2"

echo "%FILE_SIZE%" | findstr "\"[0-9][0-9]*\"" > NUL
if errorlevel 1 (
    echo Usage: %~nx0 directory file_size_in_bytes .5G = 500000000
    echo Lists all files in given directory and its subdirectories larger than given size.
    exit /b 1
)

if not exist "%SEARCH_DIR%" (
    echo "%SEARCH_DIR%" does not exist.
    exit /b 1
)

for /R "%SEARCH_DIR%" %%F in (*) do (
    if exist "%%F" if %%~zF GEQ %FILE_SIZE% echo %%F
)
