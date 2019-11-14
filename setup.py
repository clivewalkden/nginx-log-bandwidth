from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Nginx ScanLog',
    version='0.1',
    author='Clive Walkden',
    author_email='pypi.clive@mailsanitir.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clivewalkden/nginx-log-bandwidth",
    py_modules=['nginx_scanlog/main'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'Click',
        'tqdm'
    ],
    entry_points='''
        [console_scripts]
        scanlog=nginx_scanlog.main:init
    ''',
)
