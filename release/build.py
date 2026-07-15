#!/usr/bin/env python3
"""Build vault-daily-commit release zips for GitHub Releases."""
from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

VERSION = "1.0.0"
ROOT = Path(__file__).resolve().parent.parent
RELEASE = ROOT / "release"
DIST = RELEASE / "dist"

CORE_FILES = [
    "SKILL.md",
    "vault-config.md",
    "prompts.md",
    "README.md",
    "CHANGELOG.md",
]

PLATFORM_INSTALL = {
    "cursor": RELEASE / "INSTALL-cursor.md",
    "claude-code": RELEASE / "INSTALL-claude-code.md",
    "opencode": RELEASE / "INSTALL-opencode.md",
    "codex": RELEASE / "INSTALL-codex.md",
}


def write_zip(zip_path: Path, folder_name: str, files: dict[str, Path]) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for arc_name, src in files.items():
            zf.write(src, f"{folder_name}/{arc_name}")
    print(f"  {zip_path.name} ({zip_path.stat().st_size // 1024} KB)")


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    core = {name: ROOT / name for name in CORE_FILES}

    # universal
    universal_files = dict(core)
    universal_files["install.sh"] = ROOT / "install.sh"
    universal_files["install.ps1"] = ROOT / "install.ps1"
    for plat, doc in PLATFORM_INSTALL.items():
        universal_files[f"platforms/{plat}.md"] = ROOT / "platforms" / f"{plat}.md"
    write_zip(
        DIST / f"vault-daily-commit-universal-v{VERSION}.zip",
        "vault-daily-commit",
        universal_files,
    )

    # per-platform
    for plat, install_doc in PLATFORM_INSTALL.items():
        files = dict(core)
        files["INSTALL.md"] = install_doc
        write_zip(
            DIST / f"vault-daily-commit-{plat}-v{VERSION}.zip",
            "vault-daily-commit",
            files,
        )

    print(f"\nBuilt {len(list(DIST.glob('*.zip')))} zips in {DIST}")


if __name__ == "__main__":
    main()
