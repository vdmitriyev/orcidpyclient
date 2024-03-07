@echo off
cd ..
setlocal
:PROMPT
SET AREYOUSURE=N
SET /P AREYOUSURE=Do you want to create a new virtual environment (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

SET PATH=C:\Compilers\Python311\Scripts\;C:\Compilers\Python311\;%PATH%
python -m venv .venv
call .\.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install uv
uv pip install -r requirements/requirements.txt
uv pip install -r requirements/requirements-dev.txt
uv pip install -r requirements/requirements-docs.txt

:END
endlocal
