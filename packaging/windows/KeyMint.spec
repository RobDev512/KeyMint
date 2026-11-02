# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

PROJECT_ROOT = Path(SPECPATH).resolve().parents[1]

ENTRY_POINT = PROJECT_ROOT / "KeyMint.py"
BRANDING_DIR = PROJECT_ROOT / "assets" / "branding"
ICONS_DIR = PROJECT_ROOT / "assets" / "icons"


def collect_files(source_dir, destination_root):
    """Collect every file recursively preserving its relative structure."""
    collected = []

    for file_path in source_dir.rglob("*"):
        if not file_path.is_file():
            continue

        relative_parent = file_path.parent.relative_to(source_dir)

        if str(relative_parent) == ".":
            destination = destination_root
        else:
            destination = str(
                Path(destination_root)
                / relative_parent
            )

        collected.append(
            (
                str(file_path),
                destination,
            )
        )

    return collected


datas = []

datas += collect_files(
    BRANDING_DIR,
    "assets/branding",
)

datas += collect_files(
    ICONS_DIR,
    "assets/icons",
)


a = Analysis(
    [str(ENTRY_POINT)],
    pathex=[str(PROJECT_ROOT)],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="KeyMint",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(
        BRANDING_DIR
        / "KeyMintIcon.ico"
    ),
)
