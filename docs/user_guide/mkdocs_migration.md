# Converting from MkDocs to ROCm Docs Core

This guide helps you migrate your documentation from MkDocs to ROCm Docs Core.

## Overview

Key differences between MkDocs and ROCm Docs Core:
- Different configuration format (mkdocs.yml vs conf.py)
- Different directory structure
- Different extension system
- Different theme configuration

## Migration Steps

### 1. Project Structure

#### MkDocs Structure
```
your-project/
├── docs/
│   └── *.md
├── mkdocs.yml
└── requirements.txt
```

#### ROCm Docs Core Structure
```
your-project/
├── docs/
│   ├── conf.py
│   ├── *.md
│   └── sphinx/
│       └── _toc.yml
└── requirements.txt
```

### 2. Configuration Migration

#### From mkdocs.yml
```yaml
site_name: Your Project
site_description: Project description
theme:
  name: material
  features:
    - navigation.tabs
nav:
  - Home: index.md
  - User Guide: 
    - Getting Started: guide/getting-started.md
    - Usage: guide/usage.md
```

#### To conf.py and _toc.yml

conf.py:
```python
project = "Your Project"
version = "1.0.0"
release = "1.0.0"
html_theme = "rocm_docs_theme"
extensions = ["rocm_docs"]
```

_toc.yml:
```yaml
root: index
subtrees:
  - caption: User Guide
    entries:
      - file: guide/getting-started
      - file: guide/usage
```

### 3. Content Migration

#### Markdown Syntax Updates

MkDocs:
```markdown
# Page Title

!!! note
    Important information

[Link to page](../other-page.md)
```

ROCm Docs Core:
```markdown
# Page Title

```{note}
Important information
```

[Link to page](../other-page)
```

#### Admonitions

| MkDocs                | ROCm Docs Core          |
|--------------------|----------------------|
| `!!! note`         | ````{note}`         |
| `!!! warning`      | ````{warning}`      |
| `!!! tip`          | ````{tip}`          |

### 4. Extensions

Common MkDocs extensions and their ROCm Docs Core equivalents:

| MkDocs Extension     | ROCm Docs Core Solution                    |
|---------------------|-------------------------------------------|
| `pymdownx.highlight` | Built into MyST-Parser                    |
| `pymdownx.superfences`| Built into MyST-Parser                   |
| `pymdownx.tabbed`   | `sphinx-design` tabs                      |
| `pymdownx.details`  | `sphinx-design` dropdowns                 |

### 5. Theme Customization

#### MkDocs Material Theme:
```yaml
theme:
  name: material
  palette:
    primary: red
  features:
    - navigation.tabs
```

#### ROCm Docs Core Theme:
```python
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "rocm",
    "show_navbar_depth": 2
}
```

## Common Issues

### 1. Navigation Structure
- MkDocs uses `nav` in mkdocs.yml
- ROCm Docs Core uses `_toc.yml` in sphinx directory
- Ensure all files are referenced correctly

### 2. File Extensions
- Remove `.md` from internal links
- Update image references to use relative paths

### 3. Code Blocks
- Update code block syntax
- Add language identifiers
- Convert tabs to spaces

### 4. Special Content
- Convert MkDocs-specific features to Sphinx equivalents
- Update mathematical notation if used
- Convert custom HTML to Sphinx directives

## Migration Checklist

1. [ ] Create new project structure
2. [ ] Convert configuration files
3. [ ] Update Markdown syntax
4. [ ] Migrate extensions
5. [ ] Update theme configuration
6. [ ] Test build
7. [ ] Check all links
8. [ ] Verify formatting
9. [ ] Update deployment scripts

## Examples

### Navigation Conversion

MkDocs:
```yaml
nav:
  - Home: index.md
  - User Guide:
    - Installation: guide/install.md
    - Configuration: guide/config.md
  - API: api.md
```

ROCm Docs Core:
```yaml
root: index
subtrees:
  - caption: User Guide
    entries:
      - file: guide/install
      - file: guide/config
  - caption: Reference
    entries:
      - file: api
```

## Additional Resources

- [MyST Markdown Reference](https://myst-parser.readthedocs.io/)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [ROCm Docs Core Templates](../../templates/) 