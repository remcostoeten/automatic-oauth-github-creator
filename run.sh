#!/bin/bash

# GitHub OAuth Automator - Runner
# Uses uv to handle all dependencies automatically.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MAIN_SCRIPT="${SCRIPT_DIR}/github_oauth_automator.py"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${BLUE}[INFO]${NC} $1"; }

# Check uv exists
if ! command -v uv &> /dev/null; then
    echo "uv not found. Run ./setup.sh first, or install: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

log_info "Launching GitHub OAuth Automator..."
echo ""

# uv run handles everything: creates temp venv, installs deps, runs script
exec uv run --with playwright --with python-dotenv --with requests python "$MAIN_SCRIPT" "$@"
