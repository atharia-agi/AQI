# Sphinx configuration for Divine AI Suite documentation

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Divine AI Suite'
copyright = '2025, Tawhid-AI Research Collective'
author = 'Tawhid-AI Research Collective'

release = '0.1.0-dev'
version = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

master_doc = 'index'
