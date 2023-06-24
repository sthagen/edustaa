"""Represent (Finnish: edustaa) markdown text parts as a whole in markdown, html, pdf, and troff format guided by conventions."""
# [[[fill git_describe()]]]
__version__ = '2023.6.24+parent.8fac4d82'
# [[[end]]] (checksum: ec3200952e146896da6d3e4d7785be0a)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

APP_NAME = 'Represent (Finnish: edustaa) markdown text parts as a whole in markdown, html, pdf, and troff format guided by conventions.'
APP_ALIAS = 'edustoa'
APP_ENV = APP_ALIAS.upper()
VERSION = __version__
VERSION_INFO = __version_info__

__all__ = [
    'APP_ALIAS',
    'APP_ENV',
    'APP_NAME',
    'VERSION',
    'VERSION_INFO',
]
