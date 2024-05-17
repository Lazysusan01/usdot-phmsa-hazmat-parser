#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Set environment variables
export FLASK_APP=cfr_tool
export FLASK_RUN_HOST=0.0.0.0
export FLASK_ENV=development

# Initialize the database
flask init-db

sudo systemctl restart nginx
# Run the Flask application
flask run
