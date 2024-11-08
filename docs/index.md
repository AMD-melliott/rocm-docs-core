# ROCm Docs Core

ROCm Docs Core provides a comprehensive documentation framework for ROCm projects. It combines documentation tools, consistent styling,  scripts, and standardized layouts to help maintainers create high-quality, uniform documentation across the ROCm ecosystem.

Key features include:
- Sphinx-based documentation generation with Markdown and reStructuredText support
- Integrated API documentation through Doxygen
- Cross-project linking capabilities
- Quality assurance tools for spelling and formatting
- Consistent theme and styling across ROCm projects
- Built-in templates and examples

ROCm Docs Core is distributed as a pip package available from PyPI as
[rocm-docs-core](https://pypi.org/project/rocm-docs-core/).

## Overview

::::{grid} 1 1 2 2
:gutter: 1

:::{grid-item-card} {doc}`User Guide</user_guide/user_guide>`
:class-body: rocm-card-banner rocm-hue-1

Getting Started:
- {doc}`/user_guide/project_structure`
- {doc}`/user_guide/configuration`
- {doc}`/user_guide/building`

Basic Features:
- {doc}`/user_guide/writing`
- {doc}`/user_guide/toc`
- {doc}`/user_guide/article_info`

Advanced Features:
- {doc}`/user_guide/theme`
- {doc}`/user_guide/linking`
- {doc}`/user_guide/doxygen_integration`

Quality Tools:
- {doc}`/user_guide/spellcheck`
- {doc}`/user_guide/linting`
:::

:::{grid-item-card} {doc}`Developer Guide</developer_guide/developer_guide>`
:class-body: rocm-card-banner rocm-hue-6

Resources:
- {doc}`/developer_guide/just`
- {doc}`/developer_guide/python_linting`
- {doc}`/developer_guide/commitizen`
- {doc}`/developer_guide/projects_yaml`
- {doc}`/developer_guide/dependabot`
- {doc}`Doxygen Demo</demo/doxygen/html/index>`

:::

::::
