# Endpoint Hygiene CLI

A lightweight Python-based endpoint security automation project demonstrating alert filtering, unit testing, Git version control, Pull Requests, and continuous integration using GitHub Actions.

This project uses simulated security alert data inspired by Microsoft Graph and CrowdStrike FalconPy responses. No live endpoint connections, API credentials, or Azure subscription are required.

## Features

- Filters security alerts based on severity.
- Identifies high and critical severity alerts.
- Uses mock JSON data to simulate endpoint security API responses.
- Includes automated unit tests using Pytest.
- Uses Ruff for Python linting.
- Implements GitHub Actions for continuous integration (CI).

## Project Structure

```text
endpoint-hygiene-cli/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── .gitignore
├── app.py
├── test_app.py
└── README.md
```

## Requirements

- Python 3.11 or later
- Git
- pip

## Installation

Clone the repository:

```bash
git clone https://github.com/ParthVala/endpoint-hygiene-cli.git
```

Navigate to the project directory:

```bash
cd endpoint-hygiene-cli
```

Install the development dependencies:

```bash
pip install ruff pytest
```

## Running the Application

Execute:

```bash
python app.py
```

The application processes simulated endpoint security alerts and returns only high and critical severity alerts.

Example output:

```json
[
  {
    "id": "101",
    "title": "Suspicious PowerShell",
    "severity": "high"
  },
  {
    "id": "103",
    "title": "Mimikatz Detected",
    "severity": "critical"
  }
]
```

## Running Unit Tests

Execute:

```bash
pytest
```

The unit tests validate that the alert filtering function correctly identifies high-severity alerts.

## Code Quality

Run Ruff to check Python code quality:

```bash
ruff check .
```

## Continuous Integration (GitHub Actions)

This repository uses GitHub Actions to automate code quality checks and unit testing.

The CI workflow is triggered when:

- Code is pushed to the `main` branch.
- A Pull Request is opened or updated targeting the `main` branch.

The pipeline performs the following operations:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs Ruff and Pytest.
4. Executes Ruff linting.
5. Runs automated unit tests using Pytest.

This helps identify potential code quality issues and test failures before changes are merged into the main branch.

## Git Workflow

This project follows a feature-branch development workflow:

1. Create a feature branch.
2. Implement the required changes.
3. Stage and commit changes.
4. Push the feature branch to GitHub.
5. Open a Pull Request targeting `main`.
6. Review changes and verify CI checks.
7. Merge the Pull Request into `main`.

Example:

```bash
git checkout -b feature/new-functionality

git add .
git commit -m "Add new functionality"

git push -u origin feature/new-functionality
```

## Security Considerations

- No real API credentials or secrets are stored in this repository.
- No live endpoint operations are performed.
- Security alert data is simulated for demonstration purposes.
- `.gitignore` excludes common environment and Python cache files.

## Technologies Used

- Python
- Git and GitHub
- GitHub Actions
- Pytest
- Ruff
- JSON

## Disclaimer

This project is intended for educational purposes and demonstrates fundamental endpoint security automation and software development practices. It does not perform live endpoint detection, remediation, or security monitoring.