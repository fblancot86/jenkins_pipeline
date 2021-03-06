import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="kctest_francesc",
    version="0.0.1",
    author="keepcoder",
    author_email="kcpypitest@gmail.com",
    description="Aplicación de ejemplo",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
    install_requires=[
       'build',
       'twine',
       'coloredlogs'
   ],
)