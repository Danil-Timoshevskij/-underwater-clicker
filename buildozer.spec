[app]

# (str) Title of your application
title = Underwater Clicker

# (str) Package name
package.name = underwaterclicker

# (str) Package domain (needed for android/ios packaging)
package.domain = org.underwater

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,wav,mp3,ogg

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,assets/*/*

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Presplash image file (якщо маєте сплеш-скрін у папці assets, розкоментуйте)
#presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon file (якщо маєте іконку у папці assets, розкоментуйте)
#icon.filename = %(source.dir)s/assets/icon.png

# (str) Supported orientations (одне з: landscape, sensorLandscape, portrait або all)
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions (розкоментуйте, якщо потрібен доступ до інтернету або пам'яті)
#android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (bool) Enable AndroidX support.
android.enable_androidx = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enables Android auto backup feature (Android API >= 23)
android.allow_backup = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = ignore, 1 = warn, 2 = error)
warn_on_root = 1