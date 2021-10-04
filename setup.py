from setuptools import find_packages, setup

setup(
    name='student_registered_system',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'flask',
    ],
)
