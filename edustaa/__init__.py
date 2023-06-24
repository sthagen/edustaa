"""Represent (Finnish: edustaa) markdown text parts as a whole in markdown, html, pdf, and troff format guided by conventions."""
# [[[fill git_describe()]]]
__version__ = '2023.6.21+parent.090d802f'
# [[[end]]] (checksum: b2d5ee748ed63dc0bc63eda72fbc118d)
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
