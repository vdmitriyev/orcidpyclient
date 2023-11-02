@echo off
cd ..
setlocal
:PROMPT
SET AREYOUSURE=N
SET /P AREYOUSURE=Do you want to create a new virtual environment (Y/[N])? 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

SET PATH=C:\Compilers\Python310\Scripts\;C:\Compilers\Python310\;%PATH%
python -m venv .venv
call .\.venv\Scripts\activate.bat
pip install -r requirements/requirements.txt
pip install -r requirements/requirements-dev.txt


:END
endlocal
