# Sphinx configuration for AQI documentation

import os
import sys

sys.path.insert(0, os.path.abspath('..'))

project = 'AQI - Artificial Quranic Intelligence'
copyright = '2026, Atharia AGI Team'
author = 'Atharia AGI Team'

release = '0.2.0-dev'
version = '0.2.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

root_doc = 'index'
