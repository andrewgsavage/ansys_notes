# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ansys Notes'
copyright = '2025, Andrew Savage'
author = 'Andrew Savage'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = "sphinx_book_theme"

html_theme_options = {
    "repository_url": "https://github.com/andrewgsavage/ansys_notes",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_issues_button": True,
    "extra_navbar": "",
    "navbar_footer_text": "",
}
html_static_path = ['_static']

extensions = [
    'sphinx_toolbox.collapse',
    'sphinx_copybutton',
    ]