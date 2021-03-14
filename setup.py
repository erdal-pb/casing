from distutils.core import setup

setup(
    name='casing',
    version="0.1.2",
    author='Vincent Bénet',
    author_email='vincent.benet@outlook.fr',
    url='https://github.com/vincentBenet/casing',
    description='Easy casing nomenclatures management such as camelCase, snake_case and many others!',
    keywords=['casing', 'snake_case', 'camelCase', 'case', 'python'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
    ],
    packages=["casing"],
    include_package_data=True,
    long_description=open('README.md').read(),
    # scripts=["casing.py"]
)