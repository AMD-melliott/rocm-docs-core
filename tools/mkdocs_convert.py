#!/usr/bin/env python3
"""Convert MkDocs documentation to ROCm Docs Core format."""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional

import yaml


class MkDocsConverter:
    """Convert MkDocs documentation to ROCm Docs Core format."""

    def __init__(self, source_dir: Path, target_dir: Path):
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.mkdocs_config = None

    def convert(self):
        """Run the full conversion process."""
        print(f"Converting {self.source_dir} to {self.target_dir}")
        
        # Load MkDocs configuration
        self.mkdocs_config = self._load_mkdocs_config()
        if not self.mkdocs_config:
            sys.exit("Error: Could not find mkdocs.yml")

        # Create target directory structure
        self._create_directory_structure()

        # Convert configuration
        self._convert_configuration()

        # Convert navigation to TOC
        self._convert_navigation()

        # Convert markdown files
        self._convert_markdown_files()

        print("\nConversion complete! Next steps:")
        print("1. Review converted files in", self.target_dir)
        print("2. Check conf.py configuration")
        print("3. Verify _toc.yml structure")
        print("4. Build documentation and check for errors")

    def _load_mkdocs_config(self) -> Optional[Dict]:
        """Load MkDocs configuration file."""
        config_path = self.source_dir / "mkdocs.yml"
        if not config_path.exists():
            return None
        
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def _create_directory_structure(self):
        """Create ROCm Docs Core directory structure."""
        # Create main directories
        (self.target_dir / "docs").mkdir(parents=True, exist_ok=True)
        (self.target_dir / "docs/sphinx").mkdir(parents=True, exist_ok=True)

    def _convert_configuration(self):
        """Convert mkdocs.yml to conf.py."""
        conf_content = [
            '"""Configuration file for the Sphinx documentation builder."""',
            "",
            f"project = \"{self.mkdocs_config.get('site_name', 'Project Name')}\"",
            "version = \"1.0.0\"  # Update this",
            "release = version",
            "author = \"Advanced Micro Devices, Inc.\"",
            "copyright = \"Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved.\"",
            "",
            "# Required settings",
            "html_theme = \"rocm_docs_theme\"",
            "extensions = [\"rocm_docs\"]",
            "",
            "# Table of contents",
            "external_toc_path = \"./sphinx/_toc.yml\"",
        ]

        # Handle theme customization
        theme_config = self.mkdocs_config.get('theme', {})
        if theme_config:
            conf_content.extend([
                "",
                "# Theme options",
                "html_theme_options = {",
                "    \"flavor\": \"rocm\",",
                "}",
            ])

        # Write conf.py
        with open(self.target_dir / "docs/conf.py", 'w') as f:
            f.write("\n".join(conf_content))

    def _convert_navigation(self):
        """Convert MkDocs navigation to ROCm Docs Core TOC."""
        nav = self.mkdocs_config.get('nav', [])
        
        toc = {
            "root": "index",
            "subtrees": self._convert_nav_section(nav)
        }

        # Write _toc.yml
        with open(self.target_dir / "docs/sphinx/_toc.yml", 'w') as f:
            yaml.dump(toc, f, sort_keys=False)

    def _convert_nav_section(self, nav_items: List) -> List[Dict]:
        """Convert a navigation section recursively."""
        result = []
        
        for item in nav_items:
            if isinstance(item, dict):
                for title, content in item.items():
                    if isinstance(content, list):
                        # This is a section with subsections
                        result.append({
                            "caption": title,
                            "entries": self._convert_nav_section(content)
                        })
                    else:
                        # This is a single page
                        result.append({
                            "file": self._clean_path(content)
                        })
            elif isinstance(item, str):
                # This is a section title
                result.append({"caption": item})

        return result

    def _clean_path(self, path: str) -> str:
        """Clean file paths for ROCm Docs Core."""
        # Remove .md extension
        path = re.sub(r'\.md$', '', path)
        return path

    def _convert_markdown_files(self):
        """Convert Markdown files to ROCm Docs Core format."""
        for md_file in self.source_dir.rglob("*.md"):
            # Skip if in site directory (MkDocs output)
            if "site" in md_file.parts:
                continue

            # Determine target path
            rel_path = md_file.relative_to(self.source_dir)
            target_path = self.target_dir / "docs" / rel_path

            # Create parent directories
            target_path.parent.mkdir(parents=True, exist_ok=True)

            # Convert file content
            self._convert_markdown_file(md_file, target_path)

    def _convert_markdown_file(self, source: Path, target: Path):
        """Convert a single Markdown file."""
        with open(source, 'r') as f:
            content = f.read()

        # Convert MkDocs-style admonitions
        content = re.sub(
            r'!!! (\w+)\s*\n([ ]{4}.*\n*)*',
            lambda m: self._convert_admonition(m),
            content
        )

        # Convert links
        content = re.sub(
            r'\[(.*?)\]\((.*?)\.md(#.*?)?\)',
            r'[\1](\2\3)',
            content
        )

        with open(target, 'w') as f:
            f.write(content)

    def _convert_admonition(self, match) -> str:
        """Convert MkDocs admonition to MyST format."""
        lines = match.group(0).split('\n')
        admonition_type = lines[0].split('!!!')[1].strip()
        
        # Remove the 4-space indentation from content
        content = [line[4:] if line.startswith('    ') else line 
                  for line in lines[1:] if line]
        
        return f"```{{{admonition_type}}}\n" + '\n'.join(content) + "\n```\n"


def main():
    parser = argparse.ArgumentParser(
        description="Convert MkDocs documentation to ROCm Docs Core format"
    )
    parser.add_argument(
        "source",
        help="Source directory containing mkdocs.yml"
    )
    parser.add_argument(
        "target",
        help="Target directory for converted documentation"
    )
    
    args = parser.parse_args()
    
    converter = MkDocsConverter(
        Path(args.source).resolve(),
        Path(args.target).resolve()
    )
    converter.convert()


if __name__ == "__main__":
    main() 