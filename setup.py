'''
Flask-WePay
------------

Flask-WePay provides a thin wrapper around the WePay Python SDK.
'''

from setuptools import setup

setup(
    name='Flask-WePay',
    version='0.0.4',
    url='https://github.com/maxcountryman/flask-wepay',
    license='BSD',
    author='Max Countryman',
    author_email='maxc@me.com',
    description='WePay API support',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='test_wepay'
)

