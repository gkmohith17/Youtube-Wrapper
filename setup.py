from setuptools import setup, find_packages

setup(
    name='yt_wrapper',
    version='0.1.0',
    description='A wrapper for YouTube Data API and YouTube Transcript API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mohith G K',
    author_email='gkmohith17@gmail.com',
    url='https://github.com/yourusername/yt_wrapper',
    packages=find_packages(),
    install_requires=[
        'google-api-python-client',
        'youtube-transcript-api',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
