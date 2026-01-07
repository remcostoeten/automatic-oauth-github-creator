#!/bin/bash
# Google OAuth Automator Runner

# Load .env file if it exists
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Run the Google OAuth automator
python3 google_oauth_automator.py "$@"
