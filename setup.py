import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nakamapy",
    version="0.1",
    author="JeromeK13",
    author_email="jerome.krell@bluewin.ch",
    description="Python Wrapper for the NakamaServer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JeromeK13/nakamapy",
    packages=setuptools.find_packages(exclude=['docs', 'test']),
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
)
