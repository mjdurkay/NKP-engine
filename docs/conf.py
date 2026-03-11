import os
import sys

# Add project root so autodoc can find nkp/
sys.path.insert(0, os.path.abspath('..'))

project = 'NKP Reporting Engine'
author = 'Michael Durkay'
release = '1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode'
]

autosummary_generate = True

autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': False,
}

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
