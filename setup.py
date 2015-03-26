from setuptools import setup, find_packages

setup(
    name='dc-workspaces',
    version='0.1',
    description=('Worflow implementation from DC'),
    author='',
    author_email='proyectogestion-devel@dc.uba.ar',
    packages=find_packages(exclude=['tests']),
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)



