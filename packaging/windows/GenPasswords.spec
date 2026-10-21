# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

# El archivo .spec está en:
# PasswGen\packaging\windows\GenPasswords.spec
#
# Por eso subimos dos niveles para llegar a la raíz del proyecto.
PROJECT_ROOT = Path(SPECPATH).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

a = Analysis(
    [str(SRC_DIR / "GenPasswords.py")],
    pathex=[str(SRC_DIR)],
    binaries=[],
    datas=[
        (str(SRC_DIR / "Logo.ico"), "."),
        (str(SRC_DIR / "ver.png"), "."),
        (str(SRC_DIR / "ojo.png"), "."),
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
    name="GenPasswords",
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
    icon=str(SRC_DIR / "Logo.ico"),
)
