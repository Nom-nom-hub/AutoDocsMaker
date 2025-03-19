# Contributing to AutoDocs

Thank you for your interest in contributing to AutoDocs! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project.

## How to Contribute

1. **Fork the repository**
   - Fork the repository to your GitHub account

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/autodocs.git
   cd autodocs
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Implement your feature or bug fix
   - Add or update tests as necessary
   - Update documentation as needed

5. **Run tests**
   ```bash
   pytest
   ```

6. **Commit your changes**
   ```bash
   git commit -m "Add feature: your feature description"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Go to the original repository and create a pull request from your branch

## Development Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Coding Standards

- Follow PEP 8 style guidelines
- Write docstrings for all functions, classes, and modules
- Add type hints where appropriate
- Include unit tests for new functionality

## Pull Request Process

1. Update the README.md or documentation with details of changes if appropriate
2. Update the CHANGELOG.md with details of changes
3. The PR should work on Python 3.6 and above
4. PRs require approval from at least one maintainer

## License

By contributing to AutoDocs, you agree that your contributions will be licensed under the project's MIT License.