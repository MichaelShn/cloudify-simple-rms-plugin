

import setuptools

setuptools.setup(
    name='cloudify-simple-rms-plugin',
    version='0.0.1',
    author='Michael Shnizer',
    author_email='michael@cloudify.co',
    description='Resource Management for extending Cloudify',
    packages=['cloudify_simple_rms'],
    license='LICENSE',
    install_requires=[
        'cloudify-plugins-common>=3.4.2',
        'cloudify-rest-client>=4.0',
        'paramiko',  # for ssh netconf connection
        "Jinja2>=2.7.2",  # for template support
        'pycrypto',
        'pyyaml',
        'xmltodict']
)
