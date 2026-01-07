#!/bin/bash
# Google OAuth Automator Runner

# Load .env file if it exists
if [ -f .env ]; then
  while IFS='=' read -r key value; do
    # Skip comments and empty lines
    if [[ "$key" =~ ^#.*$ ]] || [[ -z "$key" ]]; then
      continue
    fi
    # Trim quotes if present (optional, but good practice if mixed styles)
    # value="${value%\"}"
    # value="${value#\"}"
    
    # Export securely
    export "$key=$value"
  done < .env
fi

# Run the Google OAuth automator
python3 google_oauth_automator.py "$@"
