# Theme Customization

ROCm Docs Core provides a customizable theme based on the Sphinx Book Theme with ROCm-specific enhancements.

## Theme Flavors

ROCm Docs Core supports different theme flavors for different documentation purposes:

```python
html_theme_options = {
    "flavor": "rocm"  # Options: "rocm", "rocm-blogs", "rocm-docs-home"
}
```

### Available Flavors

1. **rocm** (default)
   - Standard ROCm documentation theme
   - Full navigation sidebar
   - API documentation support

2. **rocm-blogs**
   - Blog-oriented layout
   - Simplified navigation
   - Focus on article metadata

3. **rocm-docs-home**
   - Landing page style
   - Grid layout for main sections
   - Optimized for documentation hubs

## Basic Theme Configuration

### Colors and Styling

```python
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#ED1C24",
        "color-brand-content": "#ED1C24"
    },
    "dark_css_variables": {
        "color-brand-primary": "#FF4D54",
        "color-brand-content": "#FF4D54"
    }
}
```

### Navigation Options

```python
html_theme_options = {
    "show_navbar_depth": 2,
    "show_toc_level": 2,
    "navigation_with_keys": True
}
```

### Footer Configuration

```python
html_theme_options = {
    "footer_content": {
        "links": [
            {"title": "ROCm Documentation", "url": "https://rocm.docs.amd.com/"},
            {"title": "AMD Developer Central", "url": "https://developer.amd.com/"}
        ]
    }
}
```

## Advanced Customization

### Custom CSS

Create a custom CSS file in your documentation:

```css
/* docs/_static/custom.css */
.bd-main {
    background-color: var(--pst-color-background);
}

.bd-sidebar-primary {
    background-color: var(--pst-color-surface);
}
```

Add it to your configuration:

```python
html_static_path = ['_static']
html_css_files = ['custom.css']
```

### Custom Templates

1. Create a `_templates` directory in your docs folder
2. Add custom template files
3. Configure in conf.py:

```python
templates_path = ['_templates']
```

Example template override (`_templates/layout.html`):

```html
{% extends "sphinx_book_theme/layout.html" %}

{% block extrahead %}
    {{ super() }}
    <!-- Add custom head content -->
{% endblock %}
```

## Common Customizations

### Sidebar Width

```python
html_theme_options = {
    "sidebar_width": "300px"
}
```

### Search Bar Position

```python
html_theme_options = {
    "search_bar_position": "navbar"  # or "sidebar"
}
```

### Repository Links

```python
html_theme_options = {
    "repository_url": "https://github.com/username/project",
    "repository_branch": "main",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True
}
```

## Best Practices

1. **Brand Consistency**
   - Use official ROCm colors
   - Maintain consistent styling across projects
   - Follow AMD branding guidelines

2. **Accessibility**
   - Ensure sufficient color contrast
   - Test with screen readers
   - Support keyboard navigation

3. **Responsive Design**
   - Test on multiple devices
   - Verify mobile navigation
   - Check sidebar behavior

## Examples

See complete theme implementations in the templates:

- [Minimal theme example](../../templates/minimal/docs/conf.py)
- [Standard theme example](../../templates/standard/docs/conf.py)

## Troubleshooting

1. **CSS Not Loading**
   - Verify paths in `html_static_path`
   - Check file permissions
   - Clear browser cache

2. **Template Issues**
   - Check template inheritance
   - Verify template paths
   - Look for syntax errors

3. **Theme Options**
   - Validate option names
   - Check value types
   - Consult theme documentation
