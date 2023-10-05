# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pandas_go_to_space'
copyright = '2023, Kristian Rother'
author = 'Kristian Rother'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    "sphinx.ext.intersphinx",
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ls'

# -- intersphinx configuration -----------------------------------------------

intersphinx_mapping = {
    "jupyter-tutorial": ("https://jupyter-tutorial.readthedocs.io/de/latest/", None),
    "python": ("https://docs.python.org/3", None),
    "ipython": ("https://ipython.readthedocs.io/en/latest/", None),
    "jupyter-notebook": ("https://jupyter-notebook.readthedocs.io/en/stable/", None),
    "pandas": ("https://pandas.pydata.org/pandas-docs/stable/", None),
    "pyviz": ("https://pyviz-tutorial.readthedocs.io/de/latest/", None),
    "python-basics": ("https://python-basics-tutorial.readthedocs.io/de/latest/", None),
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_path = ['themes']
html_static_path = ['_static']
html_logo = "_static/banner_wide.svg"
html_favicon = "_static/logo.svg"


html_theme_options = {
    "sidebar_hide_name": True,
    "source_repository": "https://github.com/krother/pandas_go_to_space/",
    "source_branch": "main",
    "source_directory": "/",

    "light_css_variables": {
        # see https://github.com/pradyunsg/furo/tree/main/src/furo/assets/styles/variables
        "color-card-background": "#ffbb88",
    },
}

todo_include_todos = True
