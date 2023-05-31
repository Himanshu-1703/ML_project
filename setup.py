from setuptools import setup,find_packages


def get_requirements(file_path):
    '''
    This function will return the list of requirements
    '''
    hyph_dot = '-e .'
    requirements = []
    with open(file=file_path,mode='r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if hyph_dot in requirements:
            requirements.remove(hyph_dot)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='himanshu',
    author_email='himanshu1703@gmail.com',
    packages=find_packages(),
    install_requires_from='requirements.txt'
    )

