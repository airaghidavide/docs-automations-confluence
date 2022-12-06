import os
import sys
import configparser

sys.path.insert(0, os.path.abspath('../../'))

config = configparser.ConfigParser()
config.read('../config.ini')

project = 'Showcase documentation'
copyright = '2022, davide'
author = 'Davide Airaghi'
release = '1.0.0'

extensions = ['sphinx.ext.napoleon',
              'sphinx.ext.autodoc',
              'autoapi.extension',
              'autodocsumm',
              'sphinx_copybutton',
              'myst_parser',
              'sphinxcontrib.confluencebuilder'
]

autoapi_type = 'python'
autoapi_dirs = ['../src']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store','.venv']

html_theme = 'sphinx_rtd_theme'
html_title='Amazing project in Hype'
html_static_path = ['_static']
html_logo='_static/hype_logo.png'
html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 2,
    'includehidden': True,
    'titles_only': False
}

#confluence publishing configuration
confluence_publish = True
confluence_space_key = config['CONFLUENCE']['confluence_space_key']
confluence_parent_page = 'My wiki'
confluence_server_url = config['CONFLUENCE']['confluence_server_url']
confluence_server_user = config['CONFLUENCE']['confluence_server_user']
confluence_server_pass = config['CONFLUENCE']['confluence_server_pass']
confluence_disable_ssl_validation= True