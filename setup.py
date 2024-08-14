from setuptools import setup, find_packages

def read_requirements(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

setup(
    name='Marvin Dont-Panic',
    version='0.1.0',
    description='Local AI Asisstant',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Deniz Karhan',
    packages=find_packages(),
    python_requires='>=3.11.7',
    install_requires=read_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'your_command=your_module:main_function',
        ],
    },
)
