import setuptools

def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='summary_export',
    version='0.1',
    author='Maximilian Koslowsky',
    author_email='lowsky.coding@gmail.com',
    description='Exporting summary text files to excel.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'openpyxl',
    ],
	scripts=['src/summary_export.py'],
)