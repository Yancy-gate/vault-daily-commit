#!/usr/bin/env python3
"""Build vault-daily-commit + cursor-daily-log release zips."""
from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

VERSION = "1.1.0"
ROOT = Path(__file__).resolve().parent.parent
RELEASE = ROOT / "release"
DIST = RELEASE / "dist"
CDL = ROOT / "cursor-daily-log"

VDC_CORE = [
    "SKILL.md",
    "vault-config.md",
    "prompts.md",
    "README.md",
    "CHANGELOG.md",
]

CDL_CORE = [
    "SKILL.md",
    "prompts.md",
    "README.md",
    "config.example.json",
    "install.ps1",
    "scripts/capture.py",
    "scripts/run.ps1",
    "scripts/install-schedule.ps1",
]

VDC_INSTALL = {
    "cursor": RELEASE / "INSTALL-cursor.md",
    "claude-code": RELEASE / "INSTALL-claude-code.md",
    "opencode": RELEASE / "INSTALL-opencode.md",
    "codex": RELEASE / "INSTALL-codex.md",
}

CDL_INSTALL = {
    "cursor": RELEASE / "INSTALL-cursor-daily-log-cursor.md",
    "claude-code": RELEASE / "INSTALL-cursor-daily-log-claude-code.md",
    "opencode": RELEASE / "INSTALL-cursor-daily-log-opencode.md",
    "codex": RELEASE / "INSTALL-cursor-daily-log-codex.md",
}


def write_zip(zip_path: Path, folder_name: str, files: dict[str, Path]) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for arc_name, src in files.items():
            if not src.is_file():
                raise SystemExit(f"missing {src}")
            zf.write(src, f"{folder_name}/{arc_name}")
    print(f"  {zip_path.name} ({zip_path.stat().st_size // 1024} KB)")


def build_vdc() -> None:
    core = {name: ROOT / name for name in VDC_CORE}
    universal = dict(core)
    universal["install.sh"] = ROOT / "install.sh"
    universal["install.ps1"] = ROOT / "install.ps1"
    for plat in VDC_INSTALL:
        universal[f"platforms/{plat}.md"] = ROOT / "platforms" / f"{plat}.md"
    write_zip(
        DIST / f"vault-daily-commit-universal-v{VERSION}.zip",
        "vault-daily-commit",
        universal,
    )
    for plat, install_doc in VDC_INSTALL.items():
        files = dict(core)
        files["INSTALL.md"] = install_doc
        write_zip(
            DIST / f"vault-daily-commit-{plat}-v{VERSION}.zip",
            "vault-daily-commit",
            files,
        )


def build_cdl() -> None:
    core: dict[str, Path] = {}
    for name in CDL_CORE:
        core[name] = CDL / name
    # include a short changelog pointer
    core["CHANGELOG.md"] = ROOT / "CHANGELOG.md"

    universal = dict(core)
    for plat in CDL_INSTALL:
        universal[f"platforms/{plat}.md"] = CDL / "platforms" / f"{plat}.md"
    write_zip(
        DIST / f"cursor-daily-log-universal-v{VERSION}.zip",
        "cursor-daily-log",
        universal,
    )
    for plat, install_doc in CDL_INSTALL.items():
        files = dict(core)
        files["INSTALL.md"] = install_doc
        write_zip(
            DIST / f"cursor-daily-log-{plat}-v{VERSION}.zip",
            "cursor-daily-log",
            files,
        )


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    build_vdc()
    build_cdl()
    print(f"\nBuilt {len(list(DIST.glob('*.zip')))} zips in {DIST}")


if __name__ == "__main__":
    main()
