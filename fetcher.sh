#!/bin/sh
echo "--- FETCHER STARTED ---"

# 1. Trust this directory
git config --global --add safe.directory /content
cd /content

# 2. Check if we are connected to Git
if [ ! -d .git ]; then
  echo "Folder not empty. Initializing in-place..."
  git init
  # Force-add the remote (ignore error if it exists)
  git remote add origin https://${GIT_USERNAME}:${GIT_TOKEN}@github.com/${GIT_USERNAME}/${GIT_REPO}.git || true
  
  echo "Fetching data..."
  git fetch origin
  
  echo "Resetting to match GitHub..."
  # This makes your local folder match GitHub exactly
  git checkout -b main
  git branch --set-upstream-to=origin/main main
  git reset --hard origin/main
fi

# 3. The Update Loop
while true; do
  echo "Checking for updates..."
  git pull origin main
  sleep 60
done
