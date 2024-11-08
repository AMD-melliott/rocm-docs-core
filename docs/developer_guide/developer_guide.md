# Developer Guide

The Developer Guide provides information on the processes and toolchains in `rocm-docs-core`.

## Setting Up Development Environment

### Prerequisites

- Install Python 3.8 or newer
- Install Just command runner:

```bash
# macOS
brew install just

# Linux
# Download from https://github.com/casey/just/releases
# Or use your package manager

# PIP
pip install rust-just
```

### Local Development Setup

- Clone the repository:
   
```bash
git clone https://github.com/ROCm/rocm-docs-core.git
cd rocm-docs-core
```

- Set up the development environment:
  
 ```bash
just devenv
 ```

### Building and Installing Locally

-  Build the package:

```bash
just build
```

- Install the local build:

 ```bash
 pip install dist/rocm_docs_core-*.whl
 ```

### Testing Your Changes

- Create a test documentation project:

```bash
mkdir test-docs
cd test-docs
```

- Create basic documentation structure:

 ```bash
 mkdir docs
 touch docs/conf.py docs/index.md
 mkdir docs/sphinx
 touch docs/sphinx/_toc.yml
 ```

- Configure conf.py with the generic theme:

 ```python
 # docs/conf.py
 html_theme = "rocm_docs_theme"
 html_theme_options = {
     "flavor": "generic",
     "header_title": "Test Documentation",
     "nav_secondary_items": {
         "GitHub": "https://github.com/myorg/myproject"
     }
 }
 extensions = ["rocm_docs"]
 ```

- Build the documentation:
  
 ```bash
 sphinx-build -b html docs docs/_build/html
 ```

- View the results:

```bash
# Python 3
python -m http.server --directory docs/_build/html
# Open http://localhost:8000 in your browser
```

### Development Workflow

- Install sphinx-autobuild in your development environment:

```bash
pip install sphinx-autobuild
```

- Make changes to the theme or core functionality

- Rebuild and reinstall the package:

```bash
just build
pip install dist/rocm_docs_core-*.whl --force-reinstall
```

- Start sphinx-autobuild in your test documentation directory:

```bash
cd test-docs/docs
sphinx-autobuild . _build/html
```

- View your documentation:
   - Open http://127.0.0.1:8000 in your browser
   - Changes to source files will automatically trigger a rebuild
   - Browser will refresh automatically to show your changes

- Iterate on your changes:
   - Edit theme files or core functionality
   - Rebuild and reinstall the package
   - sphinx-autobuild will detect the changes and rebuild
   - Browser will automatically refresh

### Development Tips

- Keep sphinx-autobuild running while making changes
- Use multiple terminal windows:
  - One for rebuilding/reinstalling the package
  - One for running sphinx-autobuild
  - One for git operations
- Check the sphinx-autobuild output for errors
- Clear your browser cache if styles don't update

## Additional Development Topics

- [Python Linting](python_linting.md)
- [Projects YAML](projects_yaml.md)
- [Just Tasks](just.md)
- [Dependabot](dependabot.md)
- [Commitizen](commitizen.md)
