from setuptools import setup, find_packages

setup(
    name="network-test-app",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask==2.0.1",
        "Werkzeug==2.0.1",
        "python-semantic-release",
    ],
    entry_points={
        'console_scripts': [
            'network-test-app=app.main:main',
        ],
    },
)