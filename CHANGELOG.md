## v0.4.0 (2023-04-13)

### BREAKING CHANGE

- users of the non-legacy API have to set `html_theme` to `rocm_docs_theme` to maintain the current behaviour.

### Fix

- **legacy**: fix builds without doxygen
- **extension**: no longer set the html_theme by default in the extension
- **legacy**: restore custom theme on readthedocs

## v0.3.0 (2023-04-13)

### Feat

- move automatic doxygen and doxysphinx to an extension
- move core settings to a sphinx extension

### Fix

- restore cookie permissions / analytics script

### Refactor

- various formatting and type fixes in util.py

## v0.2.2 (2023-04-13)

### Fix

- various stlysheet fixes

## v0.2.1 (2023-04-13)

### Fix

- update links in header and footer (#87)

## v0.0.1 (2023-03-13)