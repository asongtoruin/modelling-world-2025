# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Open All The Way Down'
copyright = '2025, Adam Ruszkowski'
author = 'Adam Ruszkowski'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_revealjs"
]

templates_path = ['_templates']
exclude_patterns = [".venv", "_build", "Thumbs.db", ".DS_Store", "_sections"]

revealjs_static_path = ["_static"]
revealjs_css_files = [
    "https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next",
    "https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Mono",
    "css/font.css",
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
