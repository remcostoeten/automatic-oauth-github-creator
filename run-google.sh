#!/bin/bash
# Google OAuth Automator Runner

# Load .env file if it exists
if [ -f .env ]; then
  set -a
  # shellcheck disable=SC1091
  . .env
  set +a
fi

# Run the Google OAuth automator
python3 google_oauth_automator.py "$@"
