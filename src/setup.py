#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
Created on 19-07-2012

@version: 0.1
@author: Łukasz 'Pujan' Pelc
@contact: lukasz.pelc.81@gmail.com
@copyright: 2012
@license: open source
'''

from distutils.core import setup

files_html = ['index.html']
#files_doc = ['manual.pdf']

setup(
      name='shortcutlink',
      version='0.1',
      description='Server shortcut link',
      author='Łukasz Pelc',
      author_email='lukasz.pelc.81@gmail.com',
      packages=['modules', 'tests', 'html'],
      package_data={'html':files_html},
      scripts=['shortcutlink.py'],
      classifiers='Topic :: Internet :: WWW/HTTP',
      license='open source',
      platforms='Linux',
      url='http://'
    )


