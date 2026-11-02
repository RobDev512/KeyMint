[app]

title = KeyMint
package.name = keymint
package.domain = io.robdev512

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
source.exclude_dirs = .git,.buildozer,bin,__pycache__

version = 1.1.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/assets/KeyMintIcon.png

android.api = 36
android.minapi = 23
android.ndk = 29
android.archs = arm64-v8a
android.accept_sdk_license = True

p4a.branch = develop

[buildozer]

log_level = 2
warn_on_root = 1
