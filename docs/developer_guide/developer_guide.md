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

- Build the package:

```bash
just build
```

- Install the local build with force-reinstall:

```bash
pip install dist/rocm_docs_core-*.whl --force-reinstall
```

   > **Note:** Using `--force-reinstall` is important during development as it ensures:
   >
   > - Complete removal of the old installation
   > - Fresh installation of all files
   > - No cached files from previous versions
   > - Proper update of all theme assets

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

### Testing Theme Changes with External Documentation

When developing theme changes in rocm-docs-core that you want to test with another documentation project, use the following workflow:

1. Set up your development environment in rocm-docs-core:
   ```bash
   cd rocm-docs-core
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   just devenv
   ```

2. Build and install rocm-docs-core:
   ```bash
   just build
   pip install dist/rocm_docs_core-*.whl --force-reinstall
   ```

3. In a separate directory, set up your external documentation (using the same venv):
   ```bash
   cd ../your-project
   # Still using the same activated venv from rocm-docs-core

   # Create basic doc structure if needed
   mkdir -p docs/sphinx
   touch docs/conf.py docs/index.md docs/sphinx/_toc.yml
   ```

4. Configure your documentation to use the desired theme flavor:
   ```python
   # docs/conf.py
   html_theme = "rocm_docs_theme"
   html_theme_options = {
       "flavor": "generic",  # or "rocm" for ROCm documentation
       "header_title": "Your Project Name",
       "nav_secondary_items": {
           "GitHub": "https://github.com/org/project",
           "Documentation": "https://docs.org/project"
       }
   }
   extensions = ["rocm_docs"]
   ```

5. Start sphinx-autobuild for your documentation:
   ```bash
   cd your-project/docs
   sphinx-autobuild . _build/html
   ```

6. When you make changes to the theme in rocm-docs-core:
   ```bash
   # In rocm-docs-core directory
   just build
   pip install dist/rocm_docs_core-*.whl --force-reinstall

   # The sphinx-autobuild process will detect theme changes
   # and rebuild automatically
   ```

#### Development Tips for Theme Testing

1. Use multiple terminal windows:
   - Terminal 1: rocm-docs-core development (building/installing)
   - Terminal 2: sphinx-autobuild for your documentation
   - Terminal 3: git operations

2. Keep the same venv activated in all terminals:
   ```bash
   source /path/to/rocm-docs-core/.venv/bin/activate
   ```

3. Watch the sphinx-autobuild output for errors after theme changes

4. If styles don't update:
   - Clear your browser cache
   - Stop and restart sphinx-autobuild
   - Verify the new wheel was installed correctly

## Additional Development Topics

- [Python Linting](python_linting.md)
- [Projects YAML](projects_yaml.md)
- [Just Tasks](just.md)
- [Dependabot](dependabot.md)
- [Commitizen](commitizen.md)
