# Python Dependency Management

## Dependency Declaration

### Requirements Files
```
# requirements.txt
requests==2.28.1
numpy>=1.22.0
pandas~=1.4.0
```

Version specifiers:
- `==`: Exact version
- `>=`: Minimum version
- `<=`: Maximum version
- `~=`: Compatible release (equivalent to `>=1.4.0,<1.5.0`)
- `!=`: Excluded version

### Dependency Groups
```
# requirements/
# ├── base.txt          # Core dependencies
# ├── dev.txt           # Development dependencies
# ├── test.txt          # Testing dependencies
# └── docs.txt          # Documentation dependencies

# requirements/dev.txt
-r base.txt             # Include base dependencies
pytest>=7.0.0
black==22.3.0
```

## Environment Management

### Virtual Environments (venv)
```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate

# Activate on Unix/macOS
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Deactivate
deactivate
```

### Conda Environments
```bash
# Create conda environment
conda create -n myenv python=3.10

# Activate environment
conda activate myenv

# Install packages
conda install numpy pandas
pip install -r requirements.txt

# Deactivate
conda deactivate
```

## Dependency Isolation

### Docker Containers
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

### Project-Specific Tools

```bash
# Install development tools in project environment only
pip install black flake8 mypy pytest
```

## Dependency Locking

### pip-compile (pip-tools)
```bash
# Generate locked requirements from pyproject.toml/setup.py
pip-compile --output-file=requirements.txt pyproject.toml

# Install exact versions
pip install -r requirements.txt
```

### Poetry Lock
```bash
# Generate poetry.lock file
poetry lock

# Install exact versions
poetry install
```

## Automatic Updates

### pip-upgrade-tool
```bash
pip install pip-upgrader
pip-upgrade requirements.txt
```

### Pre-commit
```yaml
# .pre-commit-config.yaml
repos:
-   repo: https://github.com/jazzband/pip-tools
    rev: 6.12.3
    hooks:
    -   id: pip-compile
        name: pip-compile
        args: [--output-file=requirements.txt, pyproject.toml]
```

## Dependency Visualization

### pipdeptree
```bash
pip install pipdeptree
pipdeptree
```

### pip-audit
```bash
pip install pip-audit
pip-audit
```

## Advanced Tools

### Poetry
```bash
# Initialize project
poetry init

# Add dependencies
poetry add requests numpy
poetry add --dev pytest black

# Install dependencies
poetry install

# Update dependencies
poetry update
```

### Pipenv
```bash
# Initialize project
pipenv install

# Add dependencies
pipenv install requests numpy
pipenv install --dev pytest black

# Install dependencies
pipenv install

# Update dependencies
pipenv update
```

### PDM
```bash
# Initialize project
pdm init

# Add dependencies
pdm add requests numpy
pdm add -d pytest black

# Install dependencies
pdm install

# Update dependencies
pdm update
```