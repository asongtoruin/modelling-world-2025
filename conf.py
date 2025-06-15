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
    "sphinx_revealjs",
    "sphinx_revealjs.ext.footnotes",
    "sphinx_revealjs.ext.sass"
]

templates_path = ['_templates']
exclude_patterns = [".venv", "_build", "Thumbs.db", ".DS_Store", "_sections"]

revealjs_static_path = ["_static"]

revealjs_script_plugins = [
    {
        "name": "RevealHighlight",
        "src": "revealjs/plugin/highlight/highlight.js",
    },
]

revealjs_script_conf = {
    "controls": True,
    "progress": True,
    "hash": True,
    "width": 1200
}

revealjs_style_theme = "custom.css"

revealjs_sass_src_dir = "_sass"
revealjs_sass_out_dir = "_static"
revealjs_sass_auto_targets = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
