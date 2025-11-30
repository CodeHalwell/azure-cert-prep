# Copilot Instructions

This repository contains an Azure Certifications Study Guide - a comprehensive collection of learning resources for Microsoft Azure and Microsoft 365 certifications, with focus on AI/ML, agentic AI, and cloud technologies.

## Repository Structure

- `azure-certifications-study-guide/` - Main study guide content organized by certification
- `main.py` - Python application entry point
- `pyproject.toml` - Python project configuration
- `.python-version` - Python version specification
- `uv.lock` - Dependency lock file (using uv package manager)
- `.gitignore` - Git ignore patterns
- `.github/` - GitHub configuration files

## Development Guidelines

### Python Development

- Use Python 3.13 or later (as specified in `.python-version`)
- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Keep functions focused and well-documented

### Documentation

- Use Markdown for all documentation files
- Include badges and visual elements where appropriate
- Keep links updated and pointing to official Microsoft resources
- Follow the existing structure in certification directories:
  - `README.md` - Overview and quick links
  - `study-guide.md` - Detailed study plan
  - `learning-modules.md` - Module-by-module breakdown
  - `practice-resources.md` - Practice tests and exercises
  - `labs/` - Hands-on lab exercises

### Content Guidelines

- Focus on official Microsoft Learn resources
- Include practical, hands-on examples
- Organize content by certification level (Fundamentals, Associate, Expert)
- Keep exam information current (costs, passing scores, status)

## Testing

When adding Python code:
- Write unit tests for new functionality
- Ensure existing tests pass before committing

## Common Tasks

### Adding a New Certification

1. Create a new directory under `azure-certifications-study-guide/`
2. Follow the existing folder structure with required files
3. Update the main README.md with the new certification entry
4. Add appropriate badges and links

### Updating Study Materials

- Verify all external links are current
- Check Microsoft Learn for updated content
- Update "Last Updated" dates in documentation
