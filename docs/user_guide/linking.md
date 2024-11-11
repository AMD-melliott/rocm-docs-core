# Cross-Project Links

ROCm Docs Core provides features for linking between different ROCm documentation projects.

## Basic Configuration

Enable cross-project linking in your `conf.py`:

```python
# Identify current project
external_projects_current_project = "your_project"

# List projects you want to link to
external_projects = ["hip", "rocm", "rocblas"]
```

## Link Syntax

### Basic Links

Link to another project's documentation:

```markdown
See the [HIP Installation Guide](hip:installation).
```

### Section Links

Link to specific sections:

```markdown
Check the [ROCm Installation Prerequisites](rocm:install/prerequisites#system-requirements).
```

### API References

Link to API documentation:

```markdown
See the [`hipMalloc`](hip:hipMalloc) function reference.
```

## Available Projects

Common ROCm projects you can link to:

```python
external_projects = [
    "rocm",          # Main ROCm documentation
    "hip",           # HIP programming guide
    "rocblas",       # ROCm BLAS library
    "hipfort",       # Fortran interface
    "rocfft",        # FFT library
    "rocrand",       # Random number generation
    "rocsparse",     # Sparse mathematics
    "rocthrust",     # Parallel algorithms
]
```

## Best Practices

1. **Use Descriptive Link Text**

   ```markdown
   # Good
   See the [HIP Installation Guide](hip:installation)

   # Avoid
   Click [here](hip:installation) for HIP installation
   ```

2. **Verify Links**
   - Build documentation locally to test links
   - Use link checkers in CI/CD
   - Keep project references up to date

3. **Version Compatibility**
   - Link to appropriate versions
   - Document version dependencies
   - Consider using version-specific links

## Advanced Features

### Version-Specific Links

```python
# In conf.py
external_projects_versions = {
    "hip": "5.7",
    "rocm": "5.7.1"
}
```

### Custom Project Mapping

```python
# In conf.py
external_projects_mapping = {
    "custom_project": "https://custom.docs.com/en/${version}"
}
```

## Examples

### Documentation Links

```markdown
# Installation
Follow the [ROCm Installation Guide](rocm:install) first, then see the
[HIP Installation Steps](hip:install).

# Programming
Learn about [HIP Programming Concepts](hip:programming_guide) and
[BLAS Routines](rocblas:api).

# Advanced Topics
See [ROCm's Peer-to-Peer Guide](rocm:concepts/p2p) for details on
GPU communication.
```

### API References

```markdown
# Function References
- [`hipMemcpy`](hip:hipMemcpy)
- [`rocblas_dgemm`](rocblas:rocblas_dgemm)

# Type References
- [`hipEvent_t`](hip:hipEvent_t)
- [`rocblas_handle`](rocblas:rocblas_handle)
```

## Troubleshooting

1. **Broken Links**
   - Verify project name is in `external_projects`
   - Check path exists in target documentation
   - Ensure correct version compatibility

2. **Version Mismatches**
   - Check `external_projects_versions`
   - Verify target documentation version exists
   - Update version mappings as needed

3. **Build Errors**
   - Verify project configuration
   - Check network connectivity
   - Update project dependencies

## Additional Resources

- [Sphinx Intersphinx Documentation](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html)
- [ROCm Documentation](https://rocm.docs.amd.com/)
- [Example Templates](../../templates/)
