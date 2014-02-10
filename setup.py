##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for quick.theme.sample package

$Id$
"""
import sys, os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version='0.1'


setup(name='quick.theme.sample',
      version=version,
      description="Quick Aero open source theme.",
      long_description=(
          'Detailed Documentation\n' +
          '======================\n'
          + '\n\n' +
          read('README.rst')
          + '\n\n' +
          read('docs', 'CHANGES.txt')
          ),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
      author='Dmitry Suvorov',
      author_email='suvdim@gmail.com',
      url='https://github.com/Zojax/quick.theme.sample',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['quick', 'quick.theme'],
      install_requires = ['setuptools',

                          'zojax.ui.portaltabs',
                          'zojax.ui.simplettw',
                          'zojax.ui.servicealert',
                          'zojax.widget.dropdowndate',
                          'zojax.askexpert',
                          'zojax.content.textannotation',
                          'zojax.personal.tagging',
                          'zojax.sitemap',
                          'zojax.jquery.clock',
                          'zojax.jquery.fancybox',
                          'zojax.jquery.ui',
                          'zojax.contenttype.media',
                          ],
      extras_require = dict(test=['zope.app.testing',
                                  'zope.testing',
                                  'zope.testbrowser',
                                  'zope.securitypolicy',
                                  'zojax.portal',
                                  'zojax.autoinclude',
                                  'zojax.skintool',
                                  #'zojax.filefield',
                                  ]),
      include_package_data = True,
      zip_safe = False
      )
