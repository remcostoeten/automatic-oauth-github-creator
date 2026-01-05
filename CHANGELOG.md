# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased] - Feature Branch: `feature/multi-creation`

### Added
- **Dual Environment Creation**: New menu option to generate both DEV and PROD OAuth applications simultaneously.
- **Split Environment Configuration**: 
    - Support for saving credentials to separate files (e.g., `.env.local` for DEV, `.env.production` for PROD).
    - "Combined Mode" to save both to `.env` with `_PROD` suffixes.
- **Smart Credential Handling**:
    - **Archive Logic**: Option to comment out old keys (`# OLD_GITHUB_CLIENT_ID`) instead of overwriting.
    - **Prefix Logic**: Fallback to `GENERATED_` prefixes if keys exist.
    - **Clipboard Support**: Automatically copy generated credentials to clipboard (macOS/Linux).
- **Test Mode**: Post-generation prompt to immediately delete created apps (useful for testing).
- **Enhanced Deletion**: Added timeouts and robust verification to `interactive_delete` to prevent hanging on bulk deletions.
- **URL Sanitization**: Automatically strips trailing slashes from homepage URLs to prevent malformed callback paths (e.g., `//api/auth`).
- **Production Config**: Added `OAUTH_PROD_BASE_URL` and `OAUTH_PROD_CALLBACK_URL` to `.env.example`.

### Changed
- Updated interactive menu ordering.
- Refactored `interactive_main` to accommodate new workflows.

---

## [0.1.0] - Initial MVP

### Added
- **Automated OAuth Creation**: Uses Playwright to automate the GitHub OAuth application creation form.
- **Credential Extraction**: Scrapes Client ID and generates Client Secret automatically.
- **Environment Management**: Writes `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` to a local `.env` file.
- **Sudo Mode Handling**: Detects GitHub's password confirmation prompts and handles them interactively.
- **Browser Session Management**: Reuses browser profile to avoid 2FA/login repetition.
- **Basic Verification**: Interactive script to verify generated credentials against the GitHub API.
- **App Deletion**: Utility to delete existing OAuth apps.
