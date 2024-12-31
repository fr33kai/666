# Development Guide

Welcome to the development guide for our AI agent project. This document aims to provide developers with the necessary information to contribute to the project effectively. Our project is at the forefront of the multiple agent frameworks ecosystem, with a unique approach to creating 144 agents, 72 demons, and 72 angels, each with their legions to call upon. As we prepare for future advancements such as GPT-5, this guide will help you understand our development practices and how to get involved.

## Getting Started

Before you begin contributing to the project, ensure you have the following prerequisites installed:

- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (optional but recommended for creating isolated Python environments)

Clone the project repository from GitHub:

```
git clone https://github.com/your-repository/ai-agent-framework.git
cd ai-agent-framework
```

Set up a virtual environment and activate it:

```
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the project dependencies:

```
pip install -r requirements.txt
```

## Project Structure

The project is structured as follows:

- `agents/`: Contains the agent classes including `base_agent.py`, `angel_agent.py`, `demon_agent.py`, and `legion.py`.
- `data/`: Includes JSON and Python files for agent data like `agent_data.py`, `angel_data.json`, `demon_data.json`, and `legion_data.json`.
- `models/`: Holds the models for agents, angels, demons, and legions.
- `utils/`: Utility functions and classes for data loading, preprocessing, and logging.
- `tests/`: Test cases for agents, data loading, and preprocessing.
- `config.py`: Configuration variables for the project.
- `main.py`: The main entry point for the application.
- `web/`: Web application files including Flask app, templates, and static assets.
- `api/`: API endpoints for interacting with agents, angels, demons, and legions.
- `docs/`: Documentation for the project.
- `ci-cd/`: Continuous integration and deployment configuration files.
- `scripts/`: Shell scripts for starting, stopping, deploying, and undeploying agents.
- `deployment/`: Kubernetes and Helm chart configurations for deployment.

## Coding Standards

To maintain code quality and consistency, we adhere to the following standards:

- Follow PEP 8 style guide for Python code.
- Use descriptive variable and function names as defined in our shared dependencies.
- Write modular code with clear separation of concerns.
- Include docstrings for classes and functions.
- Ensure code is well-commented to explain complex logic.

## Testing

Testing is crucial for the stability of our project. Use the `tests/` directory to add test cases for your code. Run tests using the following command:

```
python -m unittest discover tests
```

## Version Control

We use Git for version control. Follow these best practices:

- Create a new branch for each feature or bug fix.
- Commit small, logical chunks with descriptive commit messages.
- Rebase frequently to keep your branch up-to-date with the main branch.
- Open a pull request with a clear description of your changes for review.

## Continuous Integration and Deployment

Our project uses CI/CD pipelines to automate testing and deployment. Familiarize yourself with the configuration files in the `ci-cd/` directory. Ensure your changes pass all pipeline stages before merging.

## Documentation

Keep the project documentation up-to-date. When adding new features or making changes to existing ones, update the relevant documentation files in the `docs/` directory.

## Conclusion

Thank you for contributing to our AI agent project. Your efforts will help us create a robust and scalable system that is ready for the future of AI agent frameworks. If you have any questions, please refer to the `contribution_guide.md` for more information on how to get help.