# ROCm Documentation Core Utilities

ROCm Docs Core is a documentation framework that provides consistent styling, tooling, and configuration across all ROCm projects. It extends Sphinx with ROCm-specific features, making it easy to create and maintain high-quality documentation that seamlessly integrates with the broader ROCm ecosystem.

## Key Features

- **Unified Theme**: Consistent ROCm styling and branding across all documentation
- **API Documentation**: Built-in Doxygen integration for API documentation
- **Quality Assurance**: Automated spell checking and documentation linting
- **Cross-Project References**: Easy linking between ROCm documentation projects
- **Article Metadata**: Support for OS compatibility, reading time, and other metadata

## Prerequisites

- Python 3.10 or higher
- pip package manager
- (Optional) Doxygen for API documentation

## Installation

```bash
# From PyPI
pip install rocm-docs-core

# Or from GitHub
pip install git+https://github.com/ROCm/rocm-docs-core.git
```

## Basic Configuration

Create a `conf.py` file in your documentation directory:

```python
# Basic project information
project = "Your Project Name"
version = "1.0.0"
release = "1.0.0"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved."

# Required settings
html_theme = "rocm_docs_theme"
extensions = ["rocm_docs"]

# Optional: Enable Doxygen integration
extensions += ["rocm_docs.doxygen", "sphinxcontrib.doxylink"]
doxygen_root = "path/to/doxygen"
doxysphinx_enabled = True
```

For complete examples, see:
- [Modern configuration example](./tests/sites/doxygen/extension/conf.py)
- [Legacy configuration example](./tests/sites/doxygen/legacy/conf.py)

## Documentation

Complete documentation is available at [rocm.docs.amd.com/projects/rocm-docs-core](https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/)

### Essential Guides

- [User Guide](https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/user_guide/user_guide.html): Basic usage and features
- [Developer Guide](https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/developer_guide/developer_guide.html): Development workflow and tooling
- [Doxygen Integration](https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/user_guide/doxygen_integration.html): API documentation setup
- [Documentation Quality](https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/user_guide/spellcheck.html): Spell checking and linting guides

### Build Documentation Locally

```bash
pip install -r requirements.txt
cd docs
python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```

## Getting Help

- [File an Issue](https://github.com/ROCm/rocm-docs-core/issues)
- [ROCm Documentation](https://rocm.docs.amd.com/)
