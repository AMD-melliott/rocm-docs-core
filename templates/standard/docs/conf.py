"""Configuration file for the standard documentation template."""

project = "My Project"
version = "1.0.0"
release = "1.0.0"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved."

# Required settings
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "rocm"  # Options: "rocm", "rocm-blogs", "rocm-docs-home"
}

# Extensions
extensions = [
    "rocm_docs",
    "rocm_docs.doxygen",
    "sphinxcontrib.doxylink"
]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

# Doxygen settings
doxygen_root = "doxygen"
doxysphinx_enabled = True
doxygen_project = {
    "name": "my_project",
    "path": "doxygen/xml"
}

# Cross-project references
external_projects_current_project = "my_project"
external_projects = ["rocm"]

# Article metadata
setting_all_article_info = True
all_article_info_os = ["linux", "windows"]
article_pages = [
    {
        "file": "index",
        "os": ["linux", "windows"],
        "author": "AMD",
        "date": "2024-03-20",
        "read-time": "5 min read"
    }
]
