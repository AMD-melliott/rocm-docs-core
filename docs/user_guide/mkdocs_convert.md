# MkDocs Conversion Script

ROCm Docs Core provides a conversion script to help automate the migration from MkDocs to ROCm Docs Core.

## Installation

The conversion script is located in the `tools` directory of the ROCm Docs Core repository.

```bash
git clone https://github.com/ROCm/rocm-docs-core.git
cd rocm-docs-core
```

## Usage

```bash
python tools/mkdocs_convert.py /path/to/mkdocs/project /path/to/output
```

### Arguments

- `source`: Directory containing your MkDocs project (with mkdocs.yml)
- `target`: Directory where the converted documentation will be created

### Example

```bash
python tools/mkdocs_convert.py ~/projects/my-docs ~/projects/my-docs-converted
```

## What Gets Converted

The script automatically converts:

1. **Project Structure**
   - Creates appropriate directory structure
   - Maintains existing documentation hierarchy

2. **Configuration**
   - Converts mkdocs.yml to conf.py
   - Preserves project metadata
   - Sets up basic theme configuration

3. **Navigation**
   - Converts MkDocs nav to _toc.yml
   - Maintains section hierarchy
   - Preserves page ordering

4. **Markdown Content**
   - Updates admonition syntax
   - Fixes internal links
   - Maintains content structure

## Manual Steps Required

After running the script, you'll need to:

1. **Review Configuration**
   - Update version numbers in conf.py
   - Add any project-specific extensions
   - Configure theme options

2. **Check Content**
   - Verify converted admonitions
   - Update any complex Markdown features
   - Check all internal links

3. **Test Build**
   - Install dependencies
   - Build documentation
   - Fix any build errors

## Example Conversion

### Before (MkDocs)

```yaml
# mkdocs.yml
site_name: My Project
theme:
  name: material
nav:
  - Home: index.md
  - User Guide:
    - Installation: guide/install.md
    - Usage: guide/usage.md
```

### After (ROCm Docs Core)

```python
# conf.py
project = "My Project"
version = "1.0.0"
html_theme = "rocm_docs_theme"
extensions = ["rocm_docs"]
```

```yaml
# _toc.yml
root: index
subtrees:
  - caption: User Guide
    entries:
      - file: guide/install
      - file: guide/usage
```

## Troubleshooting

### Common Issues

1. **Missing Files**
   - Verify source directory contains mkdocs.yml
   - Check file permissions
   - Ensure target directory is writable

2. **Conversion Errors**
   - Check for unsupported MkDocs features
   - Verify Markdown syntax
   - Look for malformed YAML

3. **Build Errors**
   - Install all required dependencies
   - Check configuration syntax
   - Verify file paths in _toc.yml

## Additional Resources

- [MkDocs Migration Guide](mkdocs_migration.md)
- [Configuration Guide](configuration.md)
- [Project Structure Guide](project_structure.md) 