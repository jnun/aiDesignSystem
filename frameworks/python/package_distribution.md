# Python Package Distribution

## Project Configuration

### pyproject.toml (Modern Approach)
```toml
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
description = "A brief description"
readme = "README.md"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
license = {text = "MIT"}
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
requires-python = ">=3.8"
dependencies = [
    "requests>=2.25.0",
    "numpy>=1.20.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=6.0.0",
    "black>=22.1.0",
]

[project.urls]
"Homepage" = "https://github.com/yourusername/my_package"
"Bug Tracker" = "https://github.com/yourusername/my_package/issues"

[project.scripts]
my-command = "my_package.cli:main"
```

### setup.py (Traditional Approach)
```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "numpy>=1.20.0",
    ],
    extras_require={
        "dev": ["pytest>=6.0.0", "black>=22.1.0"],
    },
    entry_points={
        "console_scripts": [
            "my-command=my_package.cli:main",
        ],
    },
)
```

## Package Structure Best Practices

### Standard Layout
```
my_package/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── module1.py
│       └── module2.py
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
├── docs/
├── pyproject.toml
├── LICENSE
└── README.md
```

### Using src Layout
Benefits of src/ directory:
- Ensures installed package is used during development
- Prevents accidental imports from development directory
- Matches how package will be installed

## Version Management

### Version in __init__.py
```python
# my_package/__init__.py
__version__ = "0.1.0"
```

### Dynamic Versioning
```python
# setup.py
import os
from setuptools import setup

def read_version():
    with open(os.path.join("src", "my_package", "__init__.py")) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"\'')
    raise RuntimeError("Version not found")

setup(
    name="my_package",
    version=read_version(),
    # ...
)
```

## Publishing to PyPI

### Build Commands
```bash
# Build distribution packages
python -m pip install --upgrade build
python -m build

# This creates:
# - dist/my_package-0.1.0-py3-none-any.whl (wheel)
# - dist/my_package-0.1.0.tar.gz (source)
```

### Upload to PyPI
```bash
# Install twine
python -m pip install --upgrade twine

# Upload to TestPyPI first
python -m twine upload --repository testpypi dist/*

# Upload to PyPI
python -m twine upload dist/*
```

## Dependency Management

### Pinned Requirements
```
# requirements.txt
requests==2.28.1
numpy==1.23.3
```

### Development Requirements
```
# requirements-dev.txt
-r requirements.txt
pytest==7.0.1
black==22.3.0
mypy==0.950
```

### Dependency Groups
```
# requirements/
# ├── base.txt
# ├── dev.txt
# ├── test.txt
# └── docs.txt
```

## Distribution Types

### Pure Python Wheels
For packages without compiled extensions:
```
my_package-0.1.0-py3-none-any.whl
```

### Binary Wheels
For packages with compiled extensions:
```
my_package-0.1.0-cp39-cp39-manylinux_2_17_x86_64.whl
```

### Source Distribution
```
my_package-0.1.0.tar.gz
```