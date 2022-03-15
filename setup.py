# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    
    name='metricsregr',  # Required

    
    version='0.0.1',  # Required

    
    description='Metrics for regression',  # Optional

    
    
    author='sarath babu',  # Optional

   
    author_email='babusarath05@gmail.com',  # Optional

   
    classifiers=[ 
        'Development Status :: 3 - Alpha',

       
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        
        'License :: OSI Approved :: MIT License',
        
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


    #install_requires=['sklearn','math'],  # Optional
   
    project_urls={  # Optional
        'Source': 'https://github.com/babusarath05/metrics_regression'
    },
)
