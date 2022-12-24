import os

from setuptools import find_packages
from setuptools import setup

import django_xmlrpc


setup(name='django-xmlrpc',
      version=django_xmlrpc.__version__,

      description='XML-RPC Server App for the Django framework.',
      long_description='\n'.join([open('README.rst').read(),
                                  open('CHANGELOG').read()]),
      long_description_content_type='text/x-rst',
      keywords='django, service, xmlrpc',

      author=django_xmlrpc.__author__,
      author_email=django_xmlrpc.__author_email__,
      maintainer=django_xmlrpc.__maintainer__,
      maintainer_email=django_xmlrpc.__maintainer_email__,
      url=django_xmlrpc.__url__,
      license=django_xmlrpc.__license__,

      packages=find_packages(),
      classifiers=[
          'Framework :: Django',
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules'],

      include_package_data=True,
      zip_safe=False,
      install_requires=['Django>=3.2']
      )
