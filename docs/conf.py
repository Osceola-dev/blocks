import os
import sys

sys.path.insert(0, os.path.abspath('.'))

# Project info
project = 'HRA Blocks'
author = 'Dana Cora'
release = '1.0'

# Extensions
extensions = [
    "sphinx_rtd_theme",
]

templates_path = ['_templates']
exclude_patterns = []

# HTML settings
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# ✅ Google Verification (FIXED)
html_meta = {
    "google-site-verification": "c6Qrtpo9mGReY09PT1jUg4zAyx0IN8MgDSjPUbgyRww"
}
