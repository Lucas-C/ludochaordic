#!/usr/bin/env python3

# Generates a directory containing only files suitable to be served by a Gopher client,
# like https://framagit.org/Mindiell/gaufre

# USAGE: ./build_gopher_dir.py /path/to/base/directory/for/gopher

import sys
from pathlib import Path
from shutil import rmtree

SRC_DIR = Path(__file__).resolve().parent
DST_DIR = Path(sys.argv[1])

def is_published(md_path):
    content = md_path.open().read()
    return not any(f"Status: {status}" in content for status in ("draft", "hidden"))

rmtree(str(DST_DIR), ignore_errors=True)
DST_DIR.mkdir()
for md_article in SRC_DIR.glob("content/*.md"):
    if is_published(md_article):
        (DST_DIR / md_article.name).symlink_to(md_article)
(DST_DIR / "pages").mkdir()
for md_page in SRC_DIR.glob("content/pages/*.md"):
    if is_published(md_page):
        (DST_DIR / "pages" / md_page.name).symlink_to(md_page)
