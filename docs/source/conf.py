import datetime

project = 'casing'
copyright = '2021, Vincent Bénet'
author = 'Vincent Bénet'
release = 'V 1.0'
version = release
extensions = ['sphinx.ext.autosectionlabel']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "_static/logo.svg"
html_theme_options = {
    'style_nav_header_background': '#1f7863',
    'prev_next_buttons_location': 'both'
}
html_favicon = "_static/favicon.ico"
html_scaled_image_link = False
autosectionlabel_prefix_document = True
html_static_path = ['_static']
html_show_sphinx=True
html_last_updated_fmt=datetime.datetime.now().strftime("%A %d %B %Y - %Hh%M")
html_js_files = ['java.js']
rst_prolog = """
.. image:: /_static/logo.svg
    :align: right
    :width: 20%
"""
rst_epilog = """
.. image:: /_static/header.svg
    :align: center
    :width: 100%
"""