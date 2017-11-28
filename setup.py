from setuptools import setup, find_packages

setup(
    name='pylint-pmd',
    version='0.0.1',
    description='Generate PMD compatible reports for pylint',
    author='Jorge Dias',
    author_email='jorge@mrdias.com',
    url='https://github.com/diasjorge/pylint-pmd',
    keywords=['Pylint', 'PMD'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    install_requires=[
        'pylint',
    ],
    license="FreeBSD License",
    packages=find_packages(exclude=["test*"]),
    zip_safe=False,
    extras_require={
        'dev': [
            'zest.releaser[recommended]'
        ]
    },
)
