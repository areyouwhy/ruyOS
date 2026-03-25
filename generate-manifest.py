#!/usr/bin/env python3
"""
Generate .ruyos-manifest.json from scaffold.json.

Run this from the dist/ directory before each release.
It hashes every distributable file so the update skill can
compare two small JSON files instead of reading every file.

Usage:
    cd dist/
    python3 generate-manifest.py
"""

import hashlib
import json
import os
import sys

def sha256_file(filepath):
    """SHA-256 hash of a file's contents."""
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()[:12]  # Short hash — enough for diff detection

def sha256_string(content):
    """SHA-256 hash of a string (for generated files)."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:12]

def render_generated_file(entry):
    """Render a generated file's content from its scaffold definition."""
    if "raw_content" in entry:
        return entry["raw_content"]

    parts = []
    if "frontmatter" in entry:
        fm = entry["frontmatter"]
        parts.append("---")
        parts.append(f"title: {fm['title']}")
        if "tags" in fm:
            parts.append("tags:")
            for tag in fm["tags"]:
                parts.append(f"  - {tag}")
        parts.append("date: <install-date>")
        parts.append("---")
        parts.append("")

    if "heading" in entry:
        parts.append(f"# {entry['heading']}")
        parts.append("")

    if "body" in entry:
        parts.append(entry["body"])

    return "\n".join(parts)

def main():
    dist_dir = os.path.dirname(os.path.abspath(__file__))
    scaffold_path = os.path.join(dist_dir, "scaffold.json")

    if not os.path.exists(scaffold_path):
        print("Error: scaffold.json not found. Run from dist/ directory.", file=sys.stderr)
        sys.exit(1)

    with open(scaffold_path) as f:
        scaffold = json.load(f)

    manifest = {
        "version": scaffold["version"],
        "files": {}
    }

    # --- Content files (actual files on disk) ---
    content_files = scaffold.get("content_files", {})

    # System files
    for entry in content_files.get("system", []):
        repo_path = entry["repo_path"]
        install_path = entry["install_path"]
        full_path = os.path.join(dist_dir, repo_path)
        if os.path.exists(full_path):
            manifest["files"][install_path] = {
                "hash": sha256_file(full_path),
                "merge_strategy": entry["merge_strategy"],
                "source": "content_file"
            }

    # Skills
    for entry in content_files.get("skills", []):
        repo_path = entry["repo_path"]
        install_path = entry["install_path"]
        full_path = os.path.join(dist_dir, repo_path)
        if os.path.exists(full_path):
            manifest["files"][install_path] = {
                "hash": sha256_file(full_path),
                "merge_strategy": entry["merge_strategy"],
                "source": "content_file"
            }

    # Commands
    for entry in content_files.get("commands", []):
        repo_path = entry["repo_path"]
        install_path = entry["install_path"]
        full_path = os.path.join(dist_dir, repo_path)
        if os.path.exists(full_path):
            manifest["files"][install_path] = {
                "hash": sha256_file(full_path),
                "merge_strategy": entry["merge_strategy"],
                "source": "content_file"
            }

    # Obsidian config files
    obsidian = content_files.get("obsidian", {})
    if obsidian:
        obs_repo = obsidian["repo_path"]
        obs_install = obsidian["install_path"]
        obs_dir = os.path.join(dist_dir, obs_repo)

        if os.path.isdir(obs_dir):
            for root, dirs, files in os.walk(obs_dir):
                for fname in files:
                    full_path = os.path.join(root, fname)
                    rel_path = os.path.relpath(full_path, dist_dir)
                    install_rel = os.path.join(obs_install, os.path.relpath(full_path, obs_dir))
                    manifest["files"][install_rel] = {
                        "hash": sha256_file(full_path),
                        "merge_strategy": obsidian["merge_strategy"],
                        "source": "obsidian"
                    }

    # --- Generated files (content defined in scaffold.json) ---
    for entry in scaffold.get("generated_files", {}).get("files", []):
        content = render_generated_file(entry)
        manifest["files"][entry["path"]] = {
            "hash": sha256_string(content),
            "merge_strategy": entry["merge_strategy"],
            "source": "generated_file"
        }

    # Write manifest
    manifest_path = os.path.join(dist_dir, ".ruyos-manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    # Summary
    total = len(manifest["files"])
    by_source = {}
    for info in manifest["files"].values():
        src = info["source"]
        by_source[src] = by_source.get(src, 0) + 1

    print(f"Generated .ruyos-manifest.json — {total} files tracked")
    for src, count in sorted(by_source.items()):
        print(f"  {src}: {count}")

if __name__ == "__main__":
    main()
