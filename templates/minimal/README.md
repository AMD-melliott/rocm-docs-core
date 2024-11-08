# ROCm Docs Core - Minimal Documentation Template

This is a minimal working template for creating documentation with ROCm Docs Core.

## Using This Template

1. Copy this entire directory structure to your project
2. Update the following files:
   - `docs/conf.py`: Change project name, version, and other metadata
   - `docs/index.md`: Add your project's introduction and overview
   - `docs/sphinx/_toc.yml`: Adjust the table of contents to match your content
   - `requirements.txt`: Add any additional dependencies your project needs

## Building the Documentation

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Build the documentation:

```bash
cd docs
python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```

- View the documentation:
  - Open `docs/_build/html/index.html` in your web browser

## Template Structure

```text
.
├── README.md               # This file
├── docs/
│   ├── conf.py            # Sphinx configuration
│   ├── index.md           # Documentation homepage
│   ├── reference/         # Reference documentation
│   ├── user_guide/        # User guide content
│   └── sphinx/
│       └── _toc.yml      # Table of contents
├── requirements.txt       # Python dependencies
└── .gitignore            # Git ignore rules
```

## Next Steps

1. Replace the placeholder content in:
   - `docs/user_guide/getting_started.md`
   - `docs/user_guide/basic_usage.md`
   - `docs/reference/configuration.md`

2. Add more documentation pages as needed by:
   - Creating new `.md` files in the appropriate directories
   - Adding them to `docs/sphinx/_toc.yml`

3. Preview your changes locally by rebuilding the documentation
