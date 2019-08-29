import setuptools

def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
	name='summary_export',
    version='0.1',
    author='Maximilian Koslowsky',
    author_email='m_koslowsky@yahoo.de',
    description='Exporting summary text files to excel.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'openpyxl',
    ],
	scripts=['summary_export.py'],
    # entry_points={
    #     'console_scripts': [
	# 		'summary_export=summary_export.summary_export:main'
	# 	],
    # },
)