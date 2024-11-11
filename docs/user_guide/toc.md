# Table of Contents Guide

This guide explains how to organize your documentation structure using the table of contents (TOC) configuration in ROCm Docs Core.

## Overview

ROCm Docs Core uses an external YAML file (`_toc.yml`) to define the documentation structure. This file must be located at `docs/sphinx/_toc.yml`.

## Basic Structure

A minimal `_toc.yml` file:

```yaml
root: index
subtrees:
  - caption: User Guide
    entries:
      - file: user_guide/getting_started
      - file: user_guide/basic_usage
```

### Key Components

- `root`: The main landing page (usually `index.md`)
- `subtrees`: Groups of related documentation
  - `caption`: Section heading in the navigation
  - `entries`: List of pages in the section

## Advanced Features

### Nested Sections

Create hierarchical navigation:

```yaml
root: index
subtrees:
  - caption: User Guide
    entries:
      - file: user_guide/index
        subtrees:
          - entries:
              - file: user_guide/getting_started
              - file: user_guide/basic_usage

  - caption: API Reference
    entries:
      - file: api/overview
      - file: api/reference
        subtrees:
          - entries:
              - file: api/classes/index
              - file: api/functions/index
```

### External Links

Include links to external documentation:

```yaml
root: index
subtrees:
  - caption: Documentation
    entries:
      - file: user_guide/index
      - url: https://rocm.docs.amd.com/
        title: ROCm Documentation
```

### Hidden Pages

Pages that should be accessible but not shown in navigation:

```yaml
root: index
subtrees:
  - caption: User Guide
    entries:
      - file: user_guide/index
        subtrees:
          - entries:
              - file: user_guide/getting_started
              - file: user_guide/basic_usage
              - file: user_guide/advanced
                hidden: true
```

## Best Practices

### Organization

1. **Logical Grouping**
   - Group related content under meaningful captions
   - Keep navigation depth reasonable (2-3 levels)
   - Put frequently accessed content at top levels

2. **File Naming**
   - Use descriptive, URL-friendly names
   - Maintain consistent naming conventions
   - Avoid spaces and special characters

3. **Structure**
   - Start with broad categories
   - Use consistent organization across sections
   - Consider user navigation patterns

### Common Patterns

#### Documentation Site

```yaml
root: index
subtrees:
  - caption: Getting Started
    entries:
      - file: getting_started/installation
      - file: getting_started/quickstart

  - caption: User Guide
    entries:
      - file: user_guide/index
      - file: user_guide/basic_concepts
      - file: user_guide/advanced_usage

  - caption: API Reference
    entries:
      - file: api/overview
      - file: api/reference

  - caption: Development
    entries:
      - file: development/contributing
      - file: development/building
```

#### API Documentation

```yaml
root: index
subtrees:
  - caption: API Documentation
    entries:
      - file: api/overview
      - file: api/classes/index
        subtrees:
          - entries:
              - file: api/classes/class1
              - file: api/classes/class2
      - file: api/functions/index
        subtrees:
          - entries:
              - file: api/functions/group1
              - file: api/functions/group2
```

## Common Issues

1. **Missing Files**
   - Ensure all referenced files exist
   - Use relative paths from docs directory
   - Check file extensions (.md)

2. **Invalid YAML**
   - Maintain correct indentation
   - Use consistent spacing
   - Validate YAML syntax

3. **Broken Links**
   - Test all navigation paths
   - Verify external URLs
   - Check case sensitivity

## Examples

See complete examples in the templates:

- [Minimal template TOC](../../templates/minimal/docs/sphinx/_toc.yml)
- [Standard template TOC](../../templates/standard/docs/sphinx/_toc.yml)
