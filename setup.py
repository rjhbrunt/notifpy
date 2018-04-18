from setuptools import setup,find_packages

setup(
    name='notifpy',
    version='0.1.0',
    description='Notifications for long running functions',
    long_description="",
    long_description_content_type="text/markdown",
    install_requires=['slackclient'],
    packages=find_packages()
    )
