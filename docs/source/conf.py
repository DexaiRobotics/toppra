# -*- coding: utf-8 -*-
#
# TOPP-RA documentation build configuration file, created by
# sphinx-quickstart on Sat Nov 18 00:03:54 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import toppra
try:
    import pathlib2 as pathlib
except ImportError:
    import pathlib
# sys.path.insert(0, os.path.abspath('../../toppra/'))


# -- General configuration ------------------------------------------------
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.napoleon',
              'sphinx_autodoc_typehints',
              'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx',
              "recommonmark",
              'nbsphinx']

intersphinx_mapping = {
    'urllib3': ('http://urllib3.readthedocs.org/en/latest', None),
    'python': ('http://docs.python.org/3', None),
    "scipy": ('http://docs.scipy.org/doc/scipy/reference', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None)
}

napoleon_google_docstring = False
napoleon_use_param = True
napoleon_use_ivar = True
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = ['.rst', '.md']

master_doc = 'index'

# General information about the project.
project = 'toppra'
copyright = '2020, Hung Pham'
author = 'Hung Pham'

version = pathlib.Path('./../../VERSION').read_text()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**.ipynb_checkpoints']


# pygments_style = 'friendly'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
# html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'github_user': 'hungpham2511',
    'github_repo': 'toppra',
    'github_button': True,
    'github_type': 'star',
    'github_banner': True,
    'travis_button': True,
    'description': 'A robotic motion planning library for path-parametrization',
    'fixed_sidebar': True,
    "sidebar_width": "270px",
    "page_width": "1240px",
    "show_related": True
}

html_static_path = ['_static']


# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
show_related = True
html_sidebars = {
    '**': [
        'about.html',
        'localtoc.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}
sidebar_collapse = True

htmlhelp_basename = 'TOPP-RAdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'TOPP-RA.tex', 'TOPP-RA Documentation',
     'Hung Pham', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'topp-ra', 'TOPP-RA Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)


texinfo_documents = [
    (master_doc, 'TOPP-RA', 'TOPP-RA Documentation',
     author, 'TOPP-RA', 'One line description of project.',
     'Miscellaneous'),
]
