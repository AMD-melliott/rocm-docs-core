# Project Structure Guide

This guide explains the required structure for ROCm documentation projects and provides examples for common use cases.

## Minimum Required Structure

A basic ROCm documentation project requires the following structure:

```text
your-project/
├── docs/
│   ├── conf.py                 # Sphinx configuration
│   ├── index.md                # Documentation homepage
│   └── sphinx/
│       └── _toc.yml            # Table of contents
├── requirements.txt            # Python dependencies
└── .gitignore                  # Git ignore file
```

### Required Files Explained

#### conf.py

The Sphinx configuration file. See the [Configuration Guide](configuration.md) for details.

#### index.md

Your documentation homepage. Example:

```markdown
# Project Name

Brief project description and introduction.

## Overview

Main documentation content...
```

#### sphinx/_toc.yml

Defines your documentation structure. Example:

```yaml
root: index
subtrees:
  - caption: User Guide
    entries:
      - file: user_guide/getting_started
      - file: user_guide/basic_usage
      - file: user_guide/advanced_features

  - caption: API Reference
    entries:
      - file: api/overview
      - file: api/reference
```

#### requirements.txt

Must include rocm-docs-core and any additional dependencies:

```text
rocm-docs-core>=1.8.3
sphinx>=5.3.0
```

## Common Project Structures

### Basic Documentation Site

```text
your-project/
├── docs/
│   ├── conf.py
│   ├── index.md
│   ├── user_guide/
│   │   ├── getting_started.md
│   │   └── basic_usage.md
│   └── sphinx/
│       └── _toc.yml
├── requirements.txt
└── .gitignore
```

### API Documentation with Doxygen

```text
your-project/
├── docs/
│   ├── conf.py
│   ├── index.md
│   ├── api/
│   │   └── overview.md
│   ├── doxygen/
│   │   ├── Doxyfile           # Doxygen configuration
│   │   └── xml/               # Generated API documentation
│   └── sphinx/
│       └── _toc.yml
├── requirements.txt
└── .gitignore
```

Additional Doxygen requirements in conf.py:

```python
extensions += ["rocm_docs.doxygen", "sphinxcontrib.doxylink"]
doxygen_root = "doxygen"
doxysphinx_enabled = True
```

### Multi-Project Documentation

```text
your-project/
├── docs/
│   ├── conf.py
│   ├── index.md
│   ├── project1/
│   │   ├── overview.md
│   │   └── usage.md
│   ├── project2/
│   │   ├── overview.md
│   │   └── usage.md
│   └── sphinx/
│       └── _toc.yml
├── requirements.txt
└── .gitignore
```

Additional cross-project settings in conf.py:

```python
external_projects_current_project = "your_project"
external_projects = ["other_project1", "other_project2"]
```

## Common Mistakes to Avoid

1. **Incorrect File Locations**: Keep all documentation files under the `docs/` directory.

2. **Missing TOC**: The `_toc.yml` file must be in `docs/sphinx/` directory.

3. **Invalid Markdown Files**: Use `.md` extension for Markdown files (not `.markdown` or `.mdown`).

4. **Wrong Doxygen Structure**: When using Doxygen, maintain the expected directory structure for proper integration.
