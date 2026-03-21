from setuptools import setup, find_packages


REPO_NAME='Chicken-Disease-Classification--Project'
AUTHOR_USER_NAME='Sansi63'
setup(
    name="cnnClassifier",
    version="0.0.0",
    packages=find_packages(where='src'),
    author="Sanket Sinha",
    author_email="sinhasanket160@gmail.com",
    description="A package for CNN app",
    long_description=open('README.md','r',encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}
   
)
