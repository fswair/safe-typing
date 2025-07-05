from setuptools import setup
from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name='safe-typing',
    version='0.2.3',
    packages=['safe_typing'],
    url='https://github.com/fswair/safe-typing',
    license='MIT',
    author='Mert Sirakaya',
    maintainer='fswair',
    maintainer_email="contact@tomris.dev",
    python_requires='>=3.10',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='safe-typing is a module that provides a safe way to access types within the typing/typing_extensions namespaces.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13'
    ],
    install_requires=[],
)