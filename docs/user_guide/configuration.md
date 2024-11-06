# Configuration Guide

This guide explains the configuration options available in ROCm Docs Core and how to use them effectively.

## Required Configuration

These settings must be included in your `conf.py` file:

### Basic Project Information
```python
project = "Your Project Name"
version = "1.0.0"
release = "1.0.0"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved."
```

### Theme Configuration
```python
html_theme = "rocm_docs_theme"
extensions = ["rocm_docs"]
```

## Optional Configuration

### Doxygen Integration
Enable API documentation generation with Doxygen:

```python
extensions += ["rocm_docs.doxygen", "sphinxcontrib.doxylink"]
doxygen_root = "path/to/doxygen"
doxysphinx_enabled = True
doxygen_project = {
    "name": "project_name",
    "path": "path/to/doxygen/xml"
}
```

### Article Metadata
Configure metadata for documentation pages:

```python
# Default metadata for all pages
setting_all_article_info = True
all_article_info_os = ["linux", "windows"]

# Page-specific metadata
article_pages = [
    {
        "file": "index",
        "os": ["linux", "windows"],
        "author": "Author Name",
        "date": "2024-03-20",
        "read-time": "5 min read"
    }
]
```

### Cross-Project References
Configure links to other ROCm projects:

```python
external_projects_current_project = "your_project_name"
external_projects = ["hipify", "python", "rocm"]
```

### Table of Contents
Specify the location of your table of contents file:

```python
external_toc_path = "./sphinx/_toc.yml"
```

## Common Configuration Mistakes

1. **Missing Required Extensions**: Always include `"rocm_docs"` in your extensions list.

2. **Incorrect Theme Name**: The theme name must be exactly `"rocm_docs_theme"`.

3. **Invalid Doxygen Paths**: When using Doxygen integration, ensure all paths are relative to your documentation root.

4. **Mixing Legacy and Modern Setup**: Don't mix the legacy setup (`setup_rocm_docs()`) with modern configuration. Choose one approach.

## Theme Flavors

ROCm Docs Core supports different theme flavors:

```python
html_theme_options = {
    "flavor": "rocm"  # Options: "rocm", "rocm-blogs", "rocm-docs-home"
}
```

## Advanced Configuration

### Search Settings
```python
html_search_language = "en"
html_search_options = {
    "type": "default"
}
```

### Output Options
```python
html_show_sourcelink = False
html_show_sphinx = False
html_copy_source = False
```

For more examples, see the [test configurations](../../tests/sites/) in the ROCm Docs Core repository. 