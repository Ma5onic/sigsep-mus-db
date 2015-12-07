import setuptools

if __name__ == "__main__":
    setuptools.setup(
        # Name of the project
        name='dsdeval',

        # Version
        version="0.1.0",

        # Description
        description='Evaluate source separation methods using the Demixing Secrets Datasets',

        # Your contact information
        author='Fabian-Robert Stöter',
        author_email='fabian-robert.stoeter@audiolabs-erlangen.de',

        # License
        license='MIT',

        # Packages in this project
        # find_packages() finds all these automatically for you
        packages=setuptools.find_packages(),

        # Dependencies, this installs the entire Python scientific
        # computations stack
        install_requires=[
            'numpy>=1.7',
            'scipy>=0.9',
            'progressbar2',
            'pyaml',
            'PySoundFile>=0.8'
        ],

        extras_require={
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
            ],
        },

        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
        ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Environment :: Plugins',
            'Intended Audience :: Telecommunications Industry',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Topic :: Multimedia :: Sound/Audio :: Analysis',
            'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis'
            'Topic :: Scientific/Engineering :: Information Analysis',
        ],

        zip_safe=False,
    )
