#!/bin/bash
echo "Creating deployment..."
#pipenv run pip install --upgrade -r <(pipenv lock -r) --target deploy/
echo "Cleaning virtual environment"
rm -rf .venv
pipenv clean
echo "Syncing fresh virtual environment with Pipfile.lock file"
pipenv sync --three
#creating freeze file
echo "Creating requirements file, removing the editable flag cuz it don't work"
pipenv run pip freeze -l | sed 's/-e //g'> elasticsearch/requirements.txt

pipenv run pip install \
    --upgrade -r elasticsearch/requirements.txt -t elasticsearch/deploy/
echo "Copying code to deploy folder"
cp -Rv elasticsearch/code/* elasticsearch/deploy/
echo "Successfully created 'deploy'"