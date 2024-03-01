# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test'
copyright = '2024, me'
author = 'me'

latex_documents = [
 ('SUMMARY', 'test.tex', 'docsUTM', 'author', 'report'), # можно поменять target name - название выходного файла, title - заголовок, author - автора
]

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
}


language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

latex_engine = 'pdflatex'
latex_elements = {
    'preamble': r'''
\\usepackage{graphicx}
\graphicspath{/}
''',
    'papersize': 'a4paper',
    'inputenc': '\\usepackage[utf8]{inputenc}',
    'babel': '\\usepackage[russian]{babel}',
    'cmappkg': '\\usepackage{cmap}',
    'fontenc': '\\usepackage[T1,T2A]{fontenc}',
    'utf8extra':'\DeclareUnicodeCharacter{00A0}{\nobreakspace}',
    'tableofcontents': '\setcounter{tocdepth}{4}'
}
latex_show_urls = 'footnote'
