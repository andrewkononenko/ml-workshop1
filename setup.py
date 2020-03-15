from setuptools import setup, find_packages

setup(
    name="This is ML workshop 1",
    version="0.1",
    packages=find_packages(),
    # scripts=['say_hello.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
        'pandas==1.0.1',
        'matplotlib==3.2.0rc3',
        'altair==4.0.1',
        "numpy==1.18.1",
        'scikit-learn==0.22.2'

    ],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        # '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        # 'hello': ['*.msg'],
    },

    # metadata to display on PyPI
    author="Max",
    author_email="imaxfp@gmail.com",
    description="This is ML workshop 1",
    keywords="ML workshop",
    url="https://...",  # project home page, if any
    project_urls={
        "Bug Tracker": "https://...",
        "Documentation": "https://...",
        "Source Code": "https://...",
    },
    classifiers=['License :: OSI Approved :: Python Software Foundation License']
)
