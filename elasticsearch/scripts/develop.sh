#!/bin/bash
echo "Cleaning"
rm -rf deploy
rm -f requirements.txt
rm -rf .venv
echo "Ensuring venv is created within the project"
export PIPENV_VENV_IN_PROJECT=true
echo "Syncing fresh virtual environment with Pipfile.lock file"
pipenv sync --dev --three 

echo "Checking for security vulnerabilities"
pipenv check

echo "Running linter"
pipenv run python -m pylint code

echo "Running tests"
pipenv run python -m pytest

