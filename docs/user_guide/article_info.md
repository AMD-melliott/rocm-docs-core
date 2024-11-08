# Article Metadata

ROCm Docs Core supports rich metadata for documentation pages, including OS compatibility, reading time, and authorship information.

## Basic Configuration

Enable article metadata in your `conf.py`:

```python
setting_all_article_info = True
```

## Global Metadata Settings

Set default metadata for all pages in `conf.py`:

```python
# OS Compatibility
all_article_info_os = ["linux", "windows"]

# Default Author
all_article_info_author = "AMD"

# Default Reading Time
all_article_info_read_time = "5 min read"
```

## Page-Specific Metadata

Configure metadata for specific pages in `conf.py`:

```python
article_pages = [
    {
        "file": "index",
        "os": ["linux"],
        "author": "Documentation Team",
        "date": "2024-03-20",
        "read-time": "3 min read"
    },
    {
        "file": "user_guide/advanced_features",
        "os": ["linux", "windows"],
        "author": "API Team",
        "date": "2024-03-15",
        "read-time": "10 min read"
    }
]
```

## Available Metadata Fields

### OS Compatibility

- **Key**: `os`
- **Values**: `["linux"]`, `["windows"]`, or `["linux", "windows"]`
- **Purpose**: Indicates which operating systems the content applies to

### Author Information

- **Key**: `author`
- **Value**: String containing author name or team
- **Purpose**: Credits content creators

### Publication Date

- **Key**: `date`
- **Value**: Date string in YYYY-MM-DD format
- **Purpose**: Shows when content was published/updated

### Reading Time

- **Key**: `read-time`
- **Value**: String with estimated reading time
- **Purpose**: Helps users gauge content length

## Best Practices

1. **Consistent Formatting**
   - Use consistent date formats
   - Standardize author attributions
   - Use uniform reading time format

2. **Accurate Information**
   - Keep dates current
   - Update reading times for significant changes
   - Verify OS compatibility

3. **Maintenance**
   - Review metadata periodically
   - Update dates when content changes
   - Verify OS compatibility remains accurate

## Examples

### Basic Article

```python
article_pages = [
    {
        "file": "getting_started",
        "os": ["linux", "windows"],
        "author": "ROCm Team",
        "date": "2024-03-20",
        "read-time": "5 min read"
    }
]
```

### API Documentation

```python
article_pages = [
    {
        "file": "api/reference",
        "os": ["linux"],
        "author": "API Documentation Team",
        "date": "2024-03-18",
        "read-time": "15 min read"
    }
]
```

### Release Notes

```python
article_pages = [
    {
        "file": "release_notes",
        "os": ["linux", "windows"],
        "author": "Release Team",
        "date": "2024-03-01",
        "read-time": "8 min read"
    }
]
```

## Common Issues

1. **Missing Files**
   - Ensure file paths match your documentation structure
   - Use relative paths from docs directory
   - Check file extensions

2. **Invalid Values**
   - Verify OS values are in supported list
   - Check date format
   - Ensure reading time format is consistent

3. **Configuration Conflicts**
   - Global vs page-specific settings
   - Multiple entries for same file
   - Inheritance issues
