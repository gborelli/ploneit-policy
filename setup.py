from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='ploneit.policy',
      version=version,
      description="Plone.it policy package",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ploneit'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
          'Products.Carousel',
          'Products.ContentWellPortlets',
          'collective.portletpage',
          'redturtle.portletpage.views',
          'plonetheme.ploneit',
          'z3c.jbot',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
      paster_plugins=[],
      )
