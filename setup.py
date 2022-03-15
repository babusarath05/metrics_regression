# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    
    name='metrics_regression',  # Required

    
    version='1.0.0',  # Required

    
    description='Metrics for regression',  # Optional

    
    
    author='sarath babu',  # Optional

   
    author_email='babusarath05@gmail.com',  # Optional

   
    classifiers=[ 
        'Development Status :: 3 - Alpha',

       
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License ::  MIT License',
        
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",

        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],

    
    keywords='metrics, regression, Adjusted r2 score,rmse',  # Optional

   
    package_dir={'': 'src'},  # Optional

   
    packages=find_packages(where='src'),  # Required

    python_requires='>=3.6, <4',


    install_requires=['sklearn','math'],  # Optional



   

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[('my_data', ['data/data_file'])],  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    entry_points={  # Optional
        'console_scripts': [
            'sample=sample:main',
        ],
    },

   
    project_urls={  # Optional
        'Source': 'https://github.com/babusarath05/metrics_regression'
    },
)
