# Frequently Asked Questions

Common questions and answers about using ROCm Docs Core.

## General Questions

### What is ROCm Docs Core?

ROCm Docs Core is a documentation framework that provides consistent styling, tooling, and configuration across all ROCm projects. It extends Sphinx with ROCm-specific features.

### Why should I use ROCm Docs Core?

- Consistent styling across ROCm documentation
- Built-in Doxygen integration
- Automated quality checks (spelling, linting)
- Cross-project linking capabilities
- Pre-configured theme and extensions

### What are the system requirements?

- Python 3.10 or higher
- pip package manager
- (Optional) Doxygen for API documentation

## Setup and Installation

### How do I start a new documentation project?

1. Install rocm-docs-core: `pip install rocm-docs-core`
2. Copy one of our templates:
   - [Minimal template](../../templates/minimal/) for basic documentation
   - [Standard template](../../templates/standard/) for full features
3. Update configuration and content

### Why isn't my documentation building?

Common issues:

1. Missing dependencies - Run `pip install -r requirements.txt`
2. Incorrect file structure - Check [Project Structure Guide](project_structure.md)
3. Invalid configuration - Verify your `conf.py` settings

### How do I enable Doxygen integration?

1. Add required extensions to `conf.py`:

   ```python
   extensions += ["rocm_docs.doxygen", "sphinxcontrib.doxylink"]
   ```

2. Configure Doxygen settings:

   ```python
   doxygen_root = "path/to/doxygen"
   doxysphinx_enabled = True
   ```

## Content and Formatting

### Which markup language should I use?

ROCm Docs Core supports MyST Markdown, which we recommend for its simplicity and features. See the [Writing Guide](writing.md) for details.

### How do I add code examples?

Use code blocks with language identifiers:

```python
def example():
    return "Hello, World!"
```

### How do I link to other ROCm documentation?

Use cross-project references:

```python
external_projects_current_project = "your_project"
external_projects = ["other_project"]
```

Then link using:

```markdown
See the [HIP documentation](hip:index).
```

## Theme and Customization

### How do I customize the theme?

See the [Theme Customization Guide](theme.md) for detailed options. Basic customization:

```python
html_theme_options = {
    "flavor": "rocm",
    "show_navbar_depth": 2
}
```

### Can I use a different theme?

While possible, we strongly recommend using the ROCm theme for consistency across ROCm documentation.

### How do I add my company logo?

Add your logo to `_static/` and configure in `conf.py`:

```python
html_logo = "_static/logo.png"
```

### How do I use the generic theme for non-ROCm projects?

1. Configure the generic flavor in your conf.py:

```python
html_theme_options = {
    "flavor": "generic",
    "header_title": "My Project Documentation",
    "nav_secondary_items": {
        "GitHub": "https://github.com/myorg/myproject",
        "Documentation": "https://docs.myproject.org"
    }
}
```

2. See the [Theme Customization Guide](theme.md#using-the-generic-flavor) for full configuration options.

### How do I remove ROCm branding from my documentation?

Use the generic theme flavor and customize the header and navigation:
1. Set `flavor` to "generic"
2. Configure custom header title and links
3. Define your own navigation items
4. Set custom footer links

See [Generic Theme Configuration](theme.md#full-configuration-example) for examples.

## Quality and Testing

### How do I check for spelling errors?

ROCm Docs Core includes spell checking. See the [Spell Check Guide](spellcheck.md).

### How do I validate my documentation?

1. Run spell check
2. Use the linter
3. Build documentation locally
4. Check all links work
5. Verify cross-references

### How do I add new words to the spell checker?

Add words to `.wordlist.txt` in your project root.

## Deployment

### How do I deploy my documentation?

Common options:

1. GitHub Pages
2. ReadTheDocs
3. Custom web server

### How do I version my documentation?

Use Git tags and configure your hosting platform to build different versions.

### Can I preview changes before deploying?

Yes, build locally:

```bash
cd docs
python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```

## Troubleshooting

### Common Error Messages

#### "Theme error: no theme named 'rocm_docs_theme'"

```bash
pip install rocm-docs-core
```

#### "Extension 'rocm_docs.doxygen' not found"

```bash
pip install rocm-docs-core[api_reference]
```

#### "File not found: index.md"

Ensure your root document is specified correctly in `_toc.yml`.

### Getting Help

1. Check the [Troubleshooting Guide](troubleshooting.md)
2. Search [GitHub Issues](https://github.com/ROCm/rocm-docs-core/issues)
3. File a new issue if needed

## Additional Resources

- [ROCm Documentation](https://rocm.docs.amd.com/)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [MyST Documentation](https://myst-parser.readthedocs.io/)
