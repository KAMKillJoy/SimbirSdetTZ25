cd "%~dp0"
call .\.venv\Scripts\activate.bat
python -m pytest .\tests\tests.py --alluredir .\results
allure serve .\results
pause