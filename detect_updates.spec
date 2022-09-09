# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['detect_updates.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=["requests","schedule","bs4"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
a.datas += [("soya.txt", ".//soya.txt", "DATA")]
a.datas += [("hidaka.txt", ".//hidaka.txt", "DATA")]
a.datas += [("hiyama1.txt", ".//hiyama1.txt", "DATA")]
a.datas += [("hiyama2.txt", ".//hiyama2.txt", "DATA")]
a.datas += [("iburi.txt", ".//iburi.txt", "DATA")]
a.datas += [("ishikari.txt", ".//ishikari.txt", "DATA")]
a.datas += [("kamikawa.txt", ".//kamikawa.txt", "DATA")]
a.datas += [("kushiro.txt", ".//kushiro.txt", "DATA")]
a.datas += [("nemuro.txt", ".//nemuro.txt", "DATA")]
a.datas += [("ohotsuku.txt", ".//ohotsuku.txt", "DATA")]
a.datas += [("oshima.txt", ".//oshima.txt", "DATA")]
a.datas += [("rumoi.txt", ".//rumoi.txt", "DATA")]
a.datas += [("shiribeshi.txt", ".//shiribeshi.txt", "DATA")]
a.datas += [("sorachi.txt", ".//sorachi.txt", "DATA")]
a.datas += [("tokachi.txt", ".//tokachi.txt", "DATA")]
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='detect_updates',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='detect_updates',
)
