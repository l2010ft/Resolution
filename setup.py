from setuptools import setup,find_packages

setup(
    name="resolution",
    version="1.0",
    description="Resuelve todo lo que necesites :) Leo(2025)",
    packages=find_packages(),
    python_requires='>=3.12',
    long_description=open('README.md').read(),  # Asegúrate de llamar a read()
    author='Leo',
    include_package_data=True,
    platforms='Windows',  # Corrige el error de sintaxis, añadiendo la coma
    install_requires=['flask']
)