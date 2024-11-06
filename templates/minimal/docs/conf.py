"""Configuration file for the minimal documentation template."""

project = "My Project"
version = "1.0.0"
release = "1.0.0"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved."

# Required settings
html_theme = "rocm_docs_theme"
extensions = ["rocm_docs"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml" 