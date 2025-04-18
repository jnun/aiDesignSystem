# Python Project Structure

## Directory Organization
```
project_name/
├── project_name/         # Main package
│   ├── __init__.py
│   ├── core/             # Core functionality
│   ├── utils/            # Utility modules
│   └── cli/              # Command-line interfaces
├── tests/                # Test suite
├── docs/                 # Documentation
├── pyproject.toml        # Project metadata and dependencies
├── README.md             # Project overview
└── .gitignore            # Git ignore patterns
```

## File Naming
- Use lowercase with underscores: `file_name.py`
- Test files prefixed with `test_`: `test_module.py`
- Interface files suffixed with `_interface`: `storage_interface.py`

## Import Organization
- Standard library imports first
- Third-party imports second
- Local/package imports third
- Sort alphabetically within each group