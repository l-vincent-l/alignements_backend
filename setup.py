import glob
import sys
from codecs import open  # To use a consistent encoding
from os import path

from setuptools import Extension, find_packages, setup

import aligments_backend

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def is_pkg(line):
    return line and not line.startswith(('--', 'git', '#'))


def list_modules(dirname):
    filenames = glob.glob(path.join(dirname, '*.py'))

    module_names = []
    for name in filenames:
        module, ext = path.splitext(path.basename(name))
        if module != '__init__':
            module_names.append(module)

    return module_names


with open('requirements.txt', encoding='utf-8') as reqs:
    install_requires = [l for l in reqs.read().split('\n') if is_pkg(l)]

try:
    from Cython.Distutils import build_ext
    CYTHON = True
except ImportError:
    sys.stdout.write('\nNOTE: Cython not installed. Addok will '
                     'still work fine, but may run a bit slower.\n\n')
    CYTHON = False
    cmdclass = {}
    ext_modules = []
else:
    ext_modules = [
        Extension('aligments_backend.' + ext, [path.join('aligments_backend', ext + '.py')])
        for ext in list_modules(path.join(here, 'aligments_backend'))]
    cmdclass = {'build_ext': build_ext}

setup(
    name='aligments_backend',
    version=addok.__version__,
    description=addok.__doc__,
    long_description=long_description,
    url=addok.__homepage__,
    author=addok.__author__,
    author_email=addok.__contact__,
    license='WTFPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='Impots, code-is-law',
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    extras_require={'test': ['pytest'], 'docs': 'mkdocs'},
    include_package_data=True,
    ext_modules=ext_modules,
    entry_points={
        #'console_scripts': ['addok=addok.bin:main'],
        #'pytest11': ['addok=addok.pytest'],
    },
    cmdclass=cmdclass,
)

