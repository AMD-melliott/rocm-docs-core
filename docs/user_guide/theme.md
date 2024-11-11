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
   - Version-aware header showing current ROCm version
   - Secondary navigation with GitHub, Community, and Support links
   - Version list in header

2. **rocm-blogs**
   - Blog-oriented layout
   - Simplified navigation without version controls
   - Focus on article metadata
   - Custom header linking to ROCm Blogs
   - Modified secondary navigation for blog context
   - No version list or branch indicators

3. **rocm-docs-home**
   - Landing page style
   - Grid layout for main sections
   - Optimized for documentation hubs
   - Simplified header without version information
   - Focus on cross-project navigation
   - Documentation-specific secondary navigation

4. **generic**
   - Highly configurable theme for non-ROCm projects
   - Customizable header, navigation, and links
   - Flexible branding options
   - Version control integration (optional)
   - Configurable secondary navigation
   - Suitable for any technical documentation

### Creating Custom Flavors

To create a custom flavor for your project:

1. Create a new directory under `src/rocm_docs/rocm_docs_theme/flavors/your-flavor-name/`
2. Create the following required files:

```text
your-flavor-name/
├── header.jinja         # Header template
└── left-side-menu.jinja # Left sidebar template
```

#### Header Template Structure

The header.jinja file must define these macros:

```jinja
{% macro top_level_header(branch, latest_version, release_candidate_version) -%}
    {# Define your custom header here #}
    <a class="klavika-font hover-opacity" href="{{ your_link }}">
        Your Custom Header Title
    </a>
{%- endmacro -%}

{% macro version_list() -%}
    {# Optional: Define version list behavior #}
{%- endmacro -%}

{# Define secondary navigation items #}
{%
set nav_secondary_items = {
    "Link 1": "url1",
    "Link 2": "url2"
}
%}
```

Parameters available to `top_level_header`:
- `branch`: Current git branch or version
- `latest_version`: Latest released version
- `release_candidate_version`: Current release candidate version (if any)

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

### Using the Generic Flavor

The generic flavor provides a flexible template system for projects outside the ROCm ecosystem. It allows complete customization of headers, navigation, and branding while maintaining the core functionality of the documentation system.

#### Basic Configuration

Minimal configuration in conf.py:

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

#### Full Configuration Example

```python
html_theme_options = {
    "flavor": "generic",

    # Header Configuration
    "header_title": "AMD GPU Operator 1.0.0",
    "header_link": "https://docs.myproject.org",

    # Version Control
    "version_list_link": "https://docs.myproject.org/versions",  # Optional version list

    # Left Sidebar Configuration
    "main_doc_link": ("Project Home", "https://docs.myproject.org"),  # Sidebar title and link

    # Top Navigation Links
    "nav_secondary_items": {
        "GitHub": "https://github.com/myorg/myproject",
        "Documentation": "https://docs.myproject.org",
        "Support": "https://github.com/myorg/myproject/issues",
        "Community": "https://community.myproject.org"
    },

    # Footer Configuration
    "license_link": "https://www.myproject.org/license",
    "license_text": "Project License"
}
```

#### Configuration Options Reference

| Option | Description | Default | Example |
|--------|-------------|---------|---------|
| `header_title` | Main title in top header | `{project} {version}` | `"My Project 1.0"` |
| `header_link` | Header title destination | `#` | `"https://docs.myproject.org"` |
| `version_list_link` | Link to version list | None | `"https://docs.myproject.org/versions"` |
| `main_doc_link` | Sidebar title and link | `(project, "#")` | `("Project Home", "https://docs.myproject.org")` |
| `nav_secondary_items` | Top navigation links | Basic GitHub links | See example below |
| `license_link` | License page URL | None | `"https://www.myproject.org/license"` |
| `license_text` | License link text | `"License"` | `"View Project License"` |

#### Navigation Items Example

```python
"nav_secondary_items": {
    "GitHub": "https://github.com/myorg/myproject",
    "Documentation": "https://docs.myproject.org",
    "Support": "https://github.com/myorg/myproject/issues",
    "API Reference": "https://api.myproject.org",
    "Community": "https://community.myproject.org"
}
```

#### Best Practices for Generic Flavor

1. **Header Configuration**
   - Use clear, descriptive titles
   - Include version information if relevant
   - Link to main documentation landing page

2. **Navigation Setup**
   - Include essential links only
   - Order links by importance
   - Ensure all links are valid and accessible

3. **Version Control**
   - Add version list link if multiple versions exist
   - Use consistent version numbering
   - Link to a clear version overview page

4. **Branding**
   - Maintain consistent project naming
   - Use appropriate links for your project ecosystem
   - Consider your target audience when customizing
