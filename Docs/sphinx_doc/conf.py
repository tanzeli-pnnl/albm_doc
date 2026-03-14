# -*- coding: utf-8 -*-
#
# ALBM documentation build configuration file

# -- General configuration ------------------------------------------------

extensions = ['sphinx.ext.mathjax']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project   = u'ALBM'
copyright = u'Pacific Northwest National Laboratory'
author    = u'Zeli Tan'

version = u'1.0'
release = u'1.0'

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = False

numfig = True
numfig_format = {'figure': '%s', 'table': '%s', 'code-block': '%s'}

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

htmlhelp_basename = 'ALBMdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

latex_documents = [
    (master_doc, 'ALBM.tex', u'ALBM Documentation',
     author, 'manual'),
]

# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'albm', u'ALBM Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, 'ALBM', u'ALBM Documentation',
     author, 'ALBM', 'Advanced Lake Biogeochemistry Model.',
     'Miscellaneous'),
]
