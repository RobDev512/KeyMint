# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

PROJECT_ROOT = Path(SPECPATH).resolve().parents[1]

ENTRY_POINT = PROJECT_ROOT / "KeyMint.py"
BRANDING_DIR = PROJECT_ROOT / "assets" / "branding"
ICONS_DIR = PROJECT_ROOT / "assets" / "icons"

a = Analysis(
    [str(ENTRY_POINT)],
    pathex=[str(PROJECT_ROOT)],
    binaries=[],
    datas=[
        (str(BRANDING_DIR / "KeyMintIcon.ico"), "assets/branding"),
        (str(BRANDING_DIR / "KeyMintIcon.png"), "assets/branding"),
        (str(ICONS_DIR / "eye-open.png"), "assets/icons"),
        (str(ICONS_DIR / "eye-closed.png"), "assets/icons"),
    ],
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
    icon=str(BRANDING_DIR / "KeyMintIcon.ico"),
)
