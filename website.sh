#!/bin/sh
echo "--- WEBSITE STARTED ---"

# Clean up old locks
rm -f .watcher_marker
touch .watcher_marker

while true; do
  echo "Starting MkDocs server..."
  # Run in background
  mkdocs serve --dev-addr=0.0.0.0:8000 -f mkdocs.yml &
  PID=$!

  # Watch loop
  while true; do
    sleep 2
    # Check if files changed (Comparing against the CORRECT filename now)
    if [ -n "$(find docs mkdocs.yml -type f -newer .watcher_marker 2>/dev/null)" ]; then
       echo "File change detected. Reloading..."
       break
    fi
  done

  # Reset marker and kill server to restart loop
  touch .watcher_marker
  if kill -0 $PID 2>/dev/null; then
    kill $PID
    wait $PID
  fi
done
