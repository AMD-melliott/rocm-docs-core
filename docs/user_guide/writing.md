# Writing Documentation

This guide covers the basics of writing documentation with ROCm Docs Core.

## Markdown Syntax

ROCm Docs Core uses MyST Markdown, which extends standard Markdown with additional features.

### Basic Formatting

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point
- Another point
  - Sub-point

1. Numbered list
2. Second item
```

### Code Blocks

Code blocks with syntax highlighting:

```python
def example():
    return "Hello, World!"
```

For inline code, use single backticks: `variable_name`

### Links and References

```markdown
[Link text](target.md)
[External link](https://example.com)

{ref}`reference-label`
```

### Notes and Warnings

```{note}
Important information here.
```

```{warning}
Critical warning here.
```

### Tables

```markdown
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

## Best Practices

### Document Structure

1. Start with a clear title and introduction
2. Use descriptive headings
3. Keep sections focused and concise
4. Include examples for complex concepts

### Writing Style

- Use clear, simple language
- Write in active voice
- Keep paragraphs short
- Include code examples where appropriate

### Code Examples

- Always include language identifiers
- Use meaningful variable names
- Add comments for complex code
- Show complete, working examples

### Cross-Referencing

- Use relative links for internal references
- Include section anchors for deep linking
- Reference API documentation appropriately

## ROCm-Specific Features

### OS Compatibility

Mark content with OS compatibility:

```yaml
os: ["linux", "windows"]
```

### Article Metadata

Add metadata to your pages:

```yaml
author: "Author Name"
date: "2024-03-20"
read-time: "5 min read"
```

### API Documentation

Link to API references:

```markdown
See the {doxygen}`MyClass` documentation for details.
```

## Examples

### Basic Documentation Page

```markdown
# Feature Name

Brief description of the feature.

## Overview

Detailed explanation of what the feature does and why it's useful.

## Usage

```python
# Example code
feature.initialize()
feature.do_something()
```

## Configuration

List of configuration options:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| name   | str  | None    | Feature name|

## See Also

- [Related Feature](related.md)
- [API Reference](../api/reference.md)

```

## MyST-Specific Features

### Directives

```markdown
```{directive-name} argument
:option: value

Content
```

```

Common directives:
- `note`, `warning`, `tip`
- `code-block`
- `toctree`
- `figure`

### Cross-References

```markdown
{ref}`label-name`
{doc}`path/to/doc`
{doxygen}`class-or-function`
```

### Math

Inline math: `$E = mc^2$`

Block math:

```markdown
$$
\frac{d}{dx}e^x = e^x
$$
```

## Additional Resources

- [MyST Markdown Reference](https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html)
- [Sphinx Documentation](https://www.sphinx-doc.org/en/master/)
- [Example Documentation](../../templates/standard/)
