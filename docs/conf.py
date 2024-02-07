import sys
import os
sys.path.append(os.path.abspath('..'))
project = 'Rest API'
copyright = '2024, Shyshyk'
author = 'Shyshyk'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# autodoc_mock_imports = ["main", "src.repository.users", "src.repository.todos", "src.routes.users", "src.routes.auth", "src.services.auth", "src.services.email"]


extensions = [
    'sphinx.ext.autodoc',
    # other extensions...
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'nature'
html_static_path = ['_static']
