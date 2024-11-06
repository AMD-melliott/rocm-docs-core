# Building Documentation

This guide explains how to build and preview your ROCm documentation locally.

## Prerequisites

Before building your documentation, ensure you have:

1. Python 3.10 or higher installed
2. All dependencies installed via pip:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Doxygen installed if using API documentation

## Basic Build Process

### 1. Build HTML Documentation

From your project root:

```bash
cd docs
python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```

This command:
- `-T`: Shows full traceback for errors
- `-E`: Forces rebuilding of all files
- `-b html`: Builds HTML output
- `-d _build/doctrees`: Sets directory for doctree files
- `-D language=en`: Sets documentation language

### 2. View Documentation

Open `docs/_build/html/index.html` in your web browser.

## Development Workflow

### Live Preview

For faster development, use sphinx-autobuild:

1. Install sphinx-autobuild:
   ```bash
   pip install sphinx-autobuild
   ```

2. Run the auto-builder:
   ```bash
   cd docs
   sphinx-autobuild . _build/html
   ```

3. Open http://127.0.0.1:8000 in your browser
   - Changes to source files will automatically trigger a rebuild
   - Browser will refresh automatically

### Common Build Issues

1. **Missing Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Doxygen XML Not Found**
   ```bash
   cd docs/doxygen
   doxygen Doxyfile
   ```

3. **Broken Cross-References**
   - Check file paths in links
   - Ensure referenced files exist
   - Verify TOC structure in _toc.yml

## Build Options

### Output Formats

Build different formats:
```bash
# PDF output
sphinx-build -b latex . _build/latex
cd _build/latex
make

# Single HTML page
sphinx-build -b singlehtml . _build/singlehtml

# Man pages
sphinx-build -b man . _build/man
```

### Build Configuration

Control build behavior with flags:

```bash
# Quiet output
sphinx-build -Q . _build/html

# Verbose output
sphinx-build -v . _build/html

# Show only warnings and errors
sphinx-build -W . _build/html

# Parallel build
sphinx-build -j auto . _build/html
```

## CI/CD Integration

Example GitHub Actions workflow:

```yaml
name: Documentation

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Build documentation
      run: |
        cd docs
        python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```

## Additional Resources

- [Sphinx Build Configuration](https://www.sphinx-doc.org/en/master/man/sphinx-build.html)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Example Templates](../../templates/) 