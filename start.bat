call hazmat-venv\scripts\activate
set FLASK_APP=cfr_tool
set FLASK_ENV=development
flask init-db
flask run
pause