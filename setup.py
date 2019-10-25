# Following best practice from https://docs.pytest.org/en/latest/goodpractices.html#test-discovery

from setuptools import setup

setup(
    name="shared-elasticsearch",
    version="0.1.0",
    author="Aperture Labs",
    author_email="##TODO##",
    description="""Post Deployment Scripts for the elasticsearch cluster""",
    url="https://github.com/adamwday/elasticsearch/src/master/",
    package_dir={"": "code"},
    packages=[""],
    python_requires=">=3.7",
    install_requires=["boto3", "botocore", "python-json-logger"]
)
